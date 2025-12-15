# backend/scheduler.py
"""
Heuristic scheduler for power repair tasks (completed).
Greedy assignment: for each job (sorted by priority/deadline), find best (group,day)
that respects hard constraints and capacity, using a simple cost function:
  cost = geo_w * distance_km + prio_w * priority_penalty + balance_w * history_penalty + delay_penalty

Returns:
  {
    "plan": { group_id: { day: [ entries... ] } },
    "unassigned": [ job_ids... ],
    "group_state": { group_id: { day: used_person_hours, last_lat, last_lon, entries_count } }
  }
Entry format:
  { "job_id":..., "start": 7.0, "duration_elapsed": 2.5, "person_hours":3.5, "travel_hours":0.25, "notes": "..." }
"""

from math import radians, cos, sin, asin, sqrt
from collections import defaultdict
from copy import deepcopy

WORK_DAYS = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
DAY_START_HOUR = 7.0
DAY_END_HOUR = 15.5
DEFAULT_AVG_SPEED_KMH = 40.0

def haversine_km(lat1, lon1, lat2, lon2):
    if None in (lat1, lon1, lat2, lon2):
        return 0.0
    # convert to radians (preserve lat/lon order)
    lat1_r, lon1_r, lat2_r, lon2_r = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    a = sin(dlat/2)**2 + cos(lat1_r) * cos(lat2_r) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def travel_time_hours(distance_km, avg_speed_kmh=DEFAULT_AVG_SPEED_KMH):
    if distance_km <= 0:
        return 0.0
    return distance_km / avg_speed_kmh

def _job_deadline_score(job):
    cons = job.get('constraints', []) or []
    if 'only_saturday' in cons:
        return 0
    if 'finish_by_monday' in cons:
        return 1
    return 2

def _person_hours_to_elapsed(person_hours, members_count):
    if members_count and members_count > 0:
        return max(0.25, person_hours / members_count)
    return person_hours

def _normalize_skills(sk):
    if not sk:
        return set()
    if isinstance(sk, str):
        return set([s.strip() for s in sk.split(",") if s.strip()])
    if isinstance(sk, (list, tuple)):
        return set(sk)
    return set()

def plan_week(jobs, groups, params=None):
    """
    jobs: list of dicts with keys: id, lat, lon, priority, estimated_person_hours, constraints (list), requires (opt)
    groups: list of dicts with keys: id,label,members_count,daily_capacity_hours,skills (string or list),base_lat,base_lon,history_workload
    params: dict with optional keys: geographic_weight, balance_weight, priority_weight, delay_weight, avg_speed_kmh
    """
    if params is None:
        params = {}
    geo_w = params.get('geographic_weight', 1.0)
    bal_w = params.get('balance_weight', 0.5)
    prio_w = params.get('priority_weight', 5.0)
    delay_w = params.get('delay_weight', 20.0)
    avg_speed = params.get('avg_speed_kmh', DEFAULT_AVG_SPEED_KMH)
    # Use startHour/endHour from working_params if present, else fallback to defaults
    day_start = params.get('startHour', 8.0)
    day_end = params.get('endHour', 14.0)

    # prepare groups state
    group_map = {}
    for g in groups:
        per_member_cap = g.get("daily_capacity_hours", 6)  # هر عضو چند ساعت در روز کار می‌کند
        members = g.get("members_count", 1)
        effective_capacity = members * per_member_cap       # ظرفیت کل روزانه گروه

        gm = {
            "id": g.get("id"),
            "label": g.get("label"),
            "members_count": members,
            "per_member_daily_capacity": per_member_cap,
            "daily_capacity_hours": effective_capacity,      # ← این مقدار را بعداً استفاده می‌کنیم
            "skills": _normalize_skills(g.get("skills")),
            "base_lat": g.get("base_lat"),
            "base_lon": g.get("base_lon"),
            "history_workload": g.get("history_workload", 0.0)
        }
        group_map[gm["id"]] = gm

    # initialize plan and per-group day states
    plan = {gid: {d: [] for d in WORK_DAYS} for gid in group_map.keys()}
    group_state = {
        gid: {
            d: {
                "used_person_hours": 0.0,
                "last_lat": group_map[gid]["base_lat"],
                "last_lon": group_map[gid]["base_lon"],
                "last_end_time": day_start,
                "entries": []
            } for d in WORK_DAYS
        } for gid in group_map.keys()
    }

    # sort jobs: priority asc (1 highest), then deadline score, then arrival_time if present or id
    def job_sort_key(j):
        return (j.get("priority", 3), _job_deadline_score(j), j.get("arrival_time") or j.get("id"))

    jobs_sorted = sorted(jobs, key=job_sort_key)

    unassigned = []

    for job in jobs_sorted:
        jid = job.get("id")
        jlat = job.get("lat")
        jlon = job.get("lon")
        jprio = job.get("priority", 3)
        person_hours = job.get("estimated_person_hours", 1.0)
        cons = job.get("constraints", []) or []
        requires = job.get("requires")  # e.g. 'crane' or None

        # produce candidate (group,day) with cost
        candidates = []
        for gid, g in group_map.items():
            # skill check
            if requires:
                req_skills = _normalize_skills(requires)
                if not req_skills.issubset(g["skills"]):
                    continue

            # if only_saturday, restrict days
            allowed_days = WORK_DAYS[:]
            if 'only_saturday' in cons:
                allowed_days = ["Saturday"]
            # compute max allowed finish day for deadlines
            if 'finish_by_monday' in cons:
                # must be finished by Monday -> allowed days Saturday or Sunday or Monday
                allowed_days = [d for d in allowed_days if d in ["Saturday", "Sunday", "Monday"]]

            for day in allowed_days:
                st = group_state[gid][day]
                
                # capacity check (person-hours)
                capacity = g["daily_capacity_hours"]  # این مقدار حالا ظرفیت کل گروه است (تعداد اعضا × ظرفیت هر عضو)
                if st["used_person_hours"] + person_hours > capacity:
                    continue

                # compute travel distance from last known pos for that day
                last_lat = st["last_lat"]
                last_lon = st["last_lon"]
                dist_km = haversine_km(last_lat, last_lon, jlat, jlon)
                travel_h = travel_time_hours(dist_km, avg_speed)

                # elapsed wall-clock hours to perform job with group size
                elapsed_h = _person_hours_to_elapsed(person_hours, g["members_count"])

                # check if time window fits in the day: last_end_time + travel + elapsed <= day_end
                projected_end = max(st["last_end_time"], day_start) + travel_h + elapsed_h
                if projected_end > day_end + 1e-9:
                    # doesn't fit in working hours
                    continue

                # compute costs
                geo_cost = dist_km
                prio_cost = (jprio - 1)  # 0 for priority 1, 1 for priority 2 ...
                balance_cost = g.get("history_workload", 0.0)

                # deadline penalty: if only_saturday but day != saturday apply huge penalty (should already be filtered),
                # if finish_by_monday but day is later than Monday apply penalty
                delay_pen = 0.0
                if 'only_saturday' in cons and day != "Saturday":
                    delay_pen = delay_w * 10.0
                if 'finish_by_monday' in cons and WORK_DAYS.index(day) > WORK_DAYS.index("Monday"):
                    delay_pen = delay_w * 5.0

                cost = geo_w * geo_cost + prio_w * prio_cost + bal_w * balance_cost + delay_pen

                candidates.append({
                    "group_id": gid,
                    "day": day,
                    "dist_km": dist_km,
                    "travel_h": travel_h,
                    "elapsed_h": elapsed_h,
                    "person_hours": person_hours,
                    "cost": cost,
                    "projected_end": projected_end
                })

        if not candidates:
            # cannot schedule this job in the current week
            unassigned.append(jid)
            continue

        # choose lowest cost candidate (tie-breaker: earliest projected_end)
        candidates.sort(key=lambda c: (c["cost"], c["projected_end"]))
        chosen = candidates[0]
        gid = chosen["group_id"]
        day = chosen["day"]

        # compute start time = max(last_end_time, day_start) + travel_h_before_start
        st = group_state[gid][day]
        start_time = max(st["last_end_time"], day_start) + chosen["travel_h"]
        # safety: ensure start_time + elapsed_h <= day_end
        if start_time + chosen["elapsed_h"] > day_end + 1e-9:
            # this should rarely happen because we filtered earlier; mark unassigned
            unassigned.append(jid)
            continue

        # create entry
        entry = {
            "job_id": jid,
            "start": round(start_time, 3),
            "duration_elapsed": round(chosen["elapsed_h"], 3),
            "person_hours": round(chosen["person_hours"], 3),
            "travel_hours": round(chosen["travel_h"], 3),
            "distance_km": round(chosen["dist_km"], 3),
            "notes": f"assigned by heuristic (cost={chosen['cost']:.2f})"
        }

        plan[gid][day].append(entry)

        # update state
        st["used_person_hours"] += chosen["person_hours"]
        st["last_lat"] = job.get("lat")
        st["last_lon"] = job.get("lon")
        st["last_end_time"] = round(start_time + chosen["elapsed_h"], 3)
        st["entries"].append(entry)

        # update group's history workload (simple add)
        group_map[gid]["history_workload"] = group_map[gid].get("history_workload", 0.0) + chosen["person_hours"]

    # final packaging: convert plan to simpler serializable structure (already is)
    return {
        "plan": plan,
        "unassigned": unassigned,
        "group_state": group_state
    }

# Quick test helper (not executed on import)
if __name__ == "__main__":
    # small smoke test
    jobs = [
        {"id":"job-001","lat":35.747,"lon":51.412,"priority":1,"estimated_person_hours":3.5,"constraints":["finish_by_monday"]},
        {"id":"job-002","lat":35.76,"lon":51.42,"priority":2,"estimated_person_hours":2.0,"requires":"crane"}
    ]
    groups = [
        {"id":"crew-A","label":"جرثقیل","members_count":3,"daily_capacity_hours":24,"skills":["crane"],"base_lat":35.747,"base_lon":51.412,"history_workload":5.0},
        {"id":"crew-B","label":"تعمیرات","members_count":2,"daily_capacity_hours":16,"skills":[],"base_lat":35.74,"base_lon":51.4,"history_workload":2.0}
    ]
    res = plan_week(jobs, groups)
    import json
    print(json.dumps(res, indent=2, ensure_ascii=False))