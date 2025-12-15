# backend/app.py
from flask import Flask, render_template, request, jsonify
from scheduler import plan_week
from models import db, Job, Group  # اضافه کردن import مدل‌ها
import os
import json
import urllib.request
import urllib.parse

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    
    # پیکربندی دیتابیس
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///power.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize db با app
    db.init_app(app)
    
    with app.app_context():
        # ایجاد جداول اگر وجود نداشته باشند
        db.create_all()
        
    # در حافظه نگه می‌داریم (برای تست سریع)
    app.config['DATASET'] = {
        "jobs": [],
        "groups": []
    }
    # simple in-memory cache for OSRM results: key => {segments: [...], total: float}
    app.config['OSRM_CACHE'] = {}

    # helper to compute OSRM distances (shared)
    def compute_osrm_route_distances(base_lat, base_lon, jobs_list):
        # build list of coords as lon,lat pairs
        coords = []
        coords.append((base_lon, base_lat))
        for j in jobs_list:
            coords.append((j['lon'], j['lat']))

        # Build coordinate string for OSRM: lon,lat;lon,lat;...
        coord_str = ';'.join([f"{c[0]},{c[1]}" for c in coords])
        qs = urllib.parse.urlencode({'overview': 'false', 'geometries': 'geojson'})
        osrm_url = f"https://router.project-osrm.org/route/v1/driving/{coord_str}?{qs}"
        cache_key = f"osrm:{coord_str}"
        if cache_key in app.config['OSRM_CACHE']:
            cached = app.config['OSRM_CACHE'][cache_key]
            return cached.get('segments'), cached.get('total')
        try:
            with urllib.request.urlopen(osrm_url, timeout=10) as resp:
                raw = resp.read()
                js = json.loads(raw.decode('utf-8'))
                if 'routes' in js and len(js['routes']) > 0:
                    route = js['routes'][0]
                    legs = route.get('legs')
                    if legs:
                        segment_dists = [leg.get('distance', 0.0)/1000.0 for leg in legs]
                        total = sum(segment_dists)
                        app.config['OSRM_CACHE'][cache_key] = {'segments': segment_dists, 'total': total}
                        return segment_dists, total
                    else:
                        total = route.get('distance', 0.0)/1000.0
                        app.config['OSRM_CACHE'][cache_key] = {'segments': [], 'total': total}
                        return [], total
        except Exception:
            return None, None

    @app.route("/")
    def home():
        return render_template("index.html")

    # این تابع برای خواندن کارها از دیتابیس
    @app.route("/api/jobs", methods=["GET"])
    def get_jobs():
        jobs = Job.query.all()
        out = []
        for j in jobs:
            out.append({
                'id': j.id,
                'address': j.address,
                'lat': j.lat,
                'lon': j.lon,
                'priority': j.priority,
                'estimated_person_hours': j.estimated_person_hours,
                'constraints': j.constraints.split(',') if j.constraints else [],
                'requires': j.requires.split(',') if j.requires else []
            })
        return jsonify({'jobs': out})

    # این تابع برای خواندن گروه‌ها از دیتابیس
    @app.route("/api/groups", methods=["GET"])
    def get_groups():
        groups = Group.query.all()
        out = []
        for g in groups:
            out.append({
                'id': g.id,
                'label': g.label,
                'members_count': g.members_count,
                'daily_capacity_hours': g.daily_capacity_hours,
                'skills': g.skills.split(',') if g.skills else [],
                'base_lat': g.base_lat,
                'base_lon': g.base_lon,
                'history_workload': g.history_workload
            })
        return jsonify({'groups': out})

    # این تابع برای ذخیره کارها در دیتابیس
    @app.route("/api/jobs", methods=["POST"])
    def add_jobs():
        payload = request.get_json() or {}
        incoming_jobs = payload.get("jobs", [])
        
        added_count = 0
        updated_count = 0
        
        for job_data in incoming_jobs:
            # بررسی وجود job
            existing_job = Job.query.get(job_data['id'])
            
            if existing_job:
                # به‌روزرسانی job موجود
                existing_job.address = job_data.get('address', existing_job.address)
                existing_job.lat = job_data.get('lat', existing_job.lat)
                existing_job.lon = job_data.get('lon', existing_job.lon)
                existing_job.priority = job_data.get('priority', existing_job.priority)
                existing_job.estimated_person_hours = job_data.get('estimated_person_hours', existing_job.estimated_person_hours)
                existing_job.constraints = ','.join(job_data.get('constraints', []))
                existing_job.requires = ','.join(job_data.get('requires', [])) if job_data.get('requires') else None
                updated_count += 1
            else:
                # ایجاد job جدید
                new_job = Job(
                    id=job_data['id'],
                    address=job_data.get('address'),
                    lat=job_data.get('lat'),
                    lon=job_data.get('lon'),
                    priority=job_data.get('priority', 3),
                    estimated_person_hours=job_data.get('estimated_person_hours', 3.0),
                    constraints=','.join(job_data.get('constraints', [])),
                    requires=','.join(job_data.get('requires', [])) if job_data.get('requires') else None
                )
                db.session.add(new_job)
                added_count += 1
        
        try:
            db.session.commit()
            # به‌روزرسانی حافظه موقت
            ds = app.config['DATASET']
            ds['jobs'].extend(incoming_jobs)
            
            return jsonify({
                "added": added_count,
                "updated": updated_count,
                "total": len(incoming_jobs),
                "message": f"✅ {added_count} کار جدید اضافه شد، {updated_count} کار به‌روزرسانی شد"
            }), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # این تابع برای ذخیره گروه‌ها در دیتابیس
    @app.route("/api/groups", methods=["POST"])
    def add_groups():
        payload = request.get_json() or {}
        incoming_groups = payload.get("groups", [])
        
        added_count = 0
        updated_count = 0
        
        for group_data in incoming_groups:
            # بررسی وجود group
            existing_group = Group.query.get(group_data['id'])
            
            if existing_group:
                # به‌روزرسانی group موجود
                existing_group.label = group_data.get('label', existing_group.label)
                existing_group.members_count = group_data.get('members_count', existing_group.members_count)
                existing_group.daily_capacity_hours = group_data.get('daily_capacity_hours', existing_group.daily_capacity_hours)
                existing_group.skills = ','.join(group_data.get('skills', []))
                existing_group.base_lat = group_data.get('base_lat', existing_group.base_lat)
                existing_group.base_lon = group_data.get('base_lon', existing_group.base_lon)
                existing_group.history_workload = group_data.get('history_workload', existing_group.history_workload)
                updated_count += 1
            else:
                # ایجاد group جدید
                new_group = Group(
                    id=group_data['id'],
                    label=group_data.get('label'),
                    members_count=group_data.get('members_count', 3),
                    daily_capacity_hours=group_data.get('daily_capacity_hours', 18),
                    skills=','.join(group_data.get('skills', [])),
                    base_lat=group_data.get('base_lat'),
                    base_lon=group_data.get('base_lon'),
                    history_workload=group_data.get('history_workload', 0.0)
                )
                db.session.add(new_group)
                added_count += 1
        
        try:
            db.session.commit()
            # به‌روزرسانی حافظه موقت
            ds = app.config['DATASET']
            ds['groups'].extend(incoming_groups)
            
            return jsonify({
                "added": added_count,
                "updated": updated_count,
                "total": len(incoming_groups),
                "message": f"✅ {added_count} گروه جدید اضافه شد، {updated_count} گروه به‌روزرسانی شد"
            }), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # حذف گروه‌ها از دیتابیس
    @app.route("/api/groups/<group_id>", methods=["DELETE"])
    def delete_group(group_id):
        group = Group.query.get(group_id)
        if not group:
            return jsonify({"error": "گروه یافت نشد"}), 404
        
        try:
            db.session.delete(group)
            db.session.commit()
            return jsonify({"message": f"گروه {group_id} حذف شد"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # حذف کارها از دیتابیس
    @app.route("/api/jobs/<job_id>", methods=["DELETE"])
    def delete_job(job_id):
        job = Job.query.get(job_id)
        if not job:
            return jsonify({"error": "کار یافت نشد"}), 404
        
        try:
            db.session.delete(job)
            db.session.commit()
            return jsonify({"message": f"کار {job_id} حذف شد"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @app.route("/api/dataset", methods=["GET"])
    def get_dataset():
        return jsonify(app.config['DATASET'])

    @app.route("/api/plan", methods=["POST"])
    def create_plan():
        payload = request.get_json() or {}
        jobs = payload.get("jobs", []) or []
        groups = payload.get("groups", []) or []
        if not isinstance(jobs, list) or not isinstance(groups, list):
            return "Invalid payload", 400
        try:
            # پارامترهای کاری را از payload بگیر (در صورت وجود)
            working_params = payload.get('working_params', {})
            # تبدیل کلیدها به float در صورت نیاز
            params = {}
            for k, v in working_params.items():
                try:
                    params[k] = float(v)
                except Exception:
                    params[k] = v
            result = plan_week(jobs, groups, params=params)
            # ذخیره برنامه در حافظه برنامه
            app.config['CURRENT_PLAN'] = result
            app.config['DATASET']['jobs'] = jobs
            app.config['DATASET']['groups'] = groups
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # این route ها را به داخل تابع create_app() منتقل کنید:
    @app.route('/map-view')
    def map_view():
        """صفحه نمایش نقشه جداگانه"""
        return render_template('map-view.html')

    @app.route('/api/map-data')
    def get_map_data():
        """داده‌های نقشه برای صفحه جداگانه"""
        try:
            group_id = request.args.get('group')
            day = request.args.get('day')
            lat = request.args.get('lat')
            lon = request.args.get('lon')
            job_id = request.args.get('job')

            # group/day view
            if group_id and day:
                groups_data = app.config['DATASET'].get('groups', [])
                group = next((g for g in groups_data if g.get('id') == group_id), None)
                if not group:
                    return jsonify({"error": "گروه یافت نشد"}), 404

                current_plan = app.config.get('CURRENT_PLAN', {}).get('plan', {})
                if not (group_id in current_plan and day in current_plan[group_id]):
                    return jsonify({'error': 'no assignments for this group/day'}), 404

                assignments = current_plan[group_id][day]
                jobs_data = []
                jobs_dict = {j['id']: j for j in app.config['DATASET'].get('jobs', [])}
                for assignment in assignments:
                    job = jobs_dict.get(assignment['job_id'])
                    if job and job.get('lat') is not None and job.get('lon') is not None:
                        try:
                            jobs_data.append({
                                'id': job['id'],
                                'lat': float(job['lat']),
                                'lon': float(job['lon']),
                                'address': job.get('address', ''),
                                'start_time': float(assignment.get('start', 0)),
                                'distance_km': float(assignment.get('distance_km')) if assignment.get('distance_km') is not None else None
                            })
                        except Exception:
                            continue

                base_lat = float(group.get('base_lat') or group.get('baseLat') or 36.317054)
                base_lon = float(group.get('base_lon') or group.get('baseLon') or 59.473879)
                segs, total_route_km = compute_osrm_route_distances(base_lat, base_lon, jobs_data) if jobs_data else (None, None)
                if segs is not None:
                    for idx, job in enumerate(jobs_data):
                        try:
                            job['route_distance_km'] = segs[idx]
                        except Exception:
                            job['route_distance_km'] = None
                resp = {'type': 'group_day', 'group': group, 'jobs': jobs_data, 'day': day}
                if total_route_km is not None:
                    resp['route_total_km'] = total_route_km
                return jsonify(resp)

            # single job or coordinates
            if job_id or (lat and lon):
                if job_id:
                    jobs_data = app.config['DATASET'].get('jobs', [])
                    job = next((j for j in jobs_data if j['id'] == job_id), None)
                    if not job:
                        return jsonify({'error': 'کار مورد نظر یافت نشد'}), 404
                    try:
                        job_data = {
                            'id': job['id'],
                            'address': job.get('address', ''),
                            'lat': float(job['lat']) if job.get('lat') else None,
                            'lon': float(job['lon']) if job.get('lon') else None
                        }
                    except (ValueError, TypeError):
                        return jsonify({'error': 'مختصات جغرافیایی نامعتبر'}), 400
                else:
                    try:
                        job_data = {'id': 'موقعیت انتخاب شده', 'address': '', 'lat': float(lat), 'lon': float(lon)}
                    except (ValueError, TypeError):
                        return jsonify({'error': 'مختصات جغرافیایی نامعتبر'}), 400

                return jsonify({'type': 'single_location', 'job': job_data})

            return jsonify({'error': 'داده‌ی یافت نشد'}), 404
        except Exception as e:
            return jsonify({'error': f'خطای سرور: {str(e)}'}), 500

    @app.route('/api/map-data/batch', methods=['POST'])
    def get_map_data_batch():
        """Accepts JSON {items: [{group: id, day: day}, ...]} and returns per-item route data to reduce repeated calls."""
        try:
            payload = request.get_json() or {}
            items = payload.get('items', [])
            if not isinstance(items, list):
                return jsonify({'error': 'invalid payload'}), 400

            results = []
            groups_data = app.config['DATASET'].get('groups', [])
            jobs_dict = {j['id']: j for j in app.config['DATASET'].get('jobs', [])}


            for it in items:
                gid = it.get('group')
                day = it.get('day')
                group = next((g for g in groups_data if g['id'] == gid), None)
                if not group:
                    results.append({'group': gid, 'day': day, 'error': 'group not found'})
                    continue

                current_plan = app.config.get('CURRENT_PLAN', {}).get('plan', {})
                if not (gid in current_plan and day in current_plan[gid]):
                    results.append({'group': gid, 'day': day, 'error': 'no assignments'})
                    continue

                assignments = current_plan[gid][day]
                jobs_data = []
                for assignment in assignments:
                    job = jobs_dict.get(assignment['job_id'])
                    if job and 'lat' in job and 'lon' in job:
                        try:
                            jobs_data.append({
                                'id': job['id'],
                                'lat': float(job['lat']),
                                'lon': float(job['lon']),
                                'address': job.get('address', ''),
                                'start_time': float(assignment.get('start', 0))
                            })
                        except Exception:
                            continue

                base_lat = float(group.get('base_lat') or group.get('baseLat') or 36.317054)
                base_lon = float(group.get('base_lon') or group.get('baseLon') or 59.473879)
                segs, total = compute_osrm_route_distances(base_lat, base_lon, jobs_data) if jobs_data else (None, None)
                # DEBUG: log the first leg and job order
                import sys
                print(f"[OSRM-BATCH-DEBUG] group={gid} day={day} base=({base_lat},{base_lon}) jobs={[j['id'] for j in jobs_data]}", file=sys.stderr)
                if segs is not None and len(segs) > 0:
                    print(f"[OSRM-BATCH-DEBUG] first_leg_km={segs[0]}", file=sys.stderr)
                if segs is not None:
                    for idx, job in enumerate(jobs_data):
                        try:
                            job['route_distance_km'] = segs[idx]
                        except Exception:
                            job['route_distance_km'] = None
                    results.append({'group': gid, 'day': day, 'jobs': jobs_data, 'route_total_km': total})
                else:
                    results.append({'group': gid, 'day': day, 'jobs': jobs_data, 'route_total_km': None})

            return jsonify({'items': results})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app

app = create_app()

if __name__ == "__main__":
    print("Server running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)