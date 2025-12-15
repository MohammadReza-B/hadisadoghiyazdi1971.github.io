# tools/export_test.py
"""Create app in-process, populate DATASET and CURRENT_PLAN for the user's example,
call /api/map-data/batch via test_client and emulate exportToExcel summation logic.
"""
import os
import sys
import json

# make sure repo root is on sys.path so `import app` works when running from tools/
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app

app = create_app()

with app.app_context():
    # prepare jobs and groups matching user's data
    jobs = [
        {'id': 'job-017', 'address': 'مشهد، بلوار هاشمیه، پلاک ۱۲۳ - شماره 17', 'lat': 36.319542, 'lon': 59.605757},
        {'id': 'job-019', 'address': 'مشهد، بلوار سجاد، مجتمع تجاری - شماره 19', 'lat': 36.326162, 'lon': 59.60086},
        {'id': 'job-014', 'address': 'مشهد، قاسم آباد، خیابان شهیدان - شماره 14', 'lat': 36.303664, 'lon': 59.608943},
        {'id': 'job-018', 'address': 'مشهد، کوهسنگی، خیابان بهشت - شماره 18', 'lat': 36.339166, 'lon': 59.60396}
    ]
    groups = [
        {'id': 'teamA', 'label': 'تیم الف', 'members_count': 3, 'daily_capacity_hours': 18, 'skills': [], 'base_lat': 36.317054, 'base_lon': 59.605757}
    ]

    app.config['DATASET']['jobs'] = jobs
    app.config['DATASET']['groups'] = groups

    # current_plan as in the user's example (order-preserving)
    current_plan = {
        'plan': {
            'teamA': {
                'Saturday': [
                    {'job_id': 'job-017', 'start': 8.05, 'duration': 1.1},
                    {'job_id': 'job-019', 'start': 9.1667, 'duration': 2},
                    {'job_id': 'job-014', 'start': 11.2333, 'duration': 2.1}
                ],
                'Sunday': [
                    {'job_id': 'job-018', 'start': 8.0, 'duration': 2.7}
                ]
            }
        }
    }
    app.config['CURRENT_PLAN'] = current_plan

    items = [{'group': 'teamA', 'day': 'Saturday'}, {'group': 'teamA', 'day': 'Sunday'}]
    # use test_request_context + full_dispatch_request to avoid test_client werkzeug compatibility issues
    import json as _json
    payload = _json.dumps({'items': items})
    headers = {'Content-Type': 'application/json'}
    with app.test_request_context('/api/map-data/batch', method='POST', data=payload, headers=headers):
        # call the Flask full dispatch to run the endpoint
        resp = app.full_dispatch_request()
        status = resp.status_code
        raw = resp.get_data(as_text=True)
        print('status_code:', status)
        try:
            data = _json.loads(raw)
        except Exception:
            print('failed to parse response as json:', raw)
            data = {}
    print(json.dumps(data, ensure_ascii=False, indent=2))

    # emulate exportToExcel summation logic for each returned item
    for it in data.get('items', []):
        gid = it.get('group')
        day = it.get('day')
        print('\n---', gid, day)
        route_jobs = it.get('jobs', [])
        route_total = it.get('route_total_km')
        # build ordered assignments
        assignments = current_plan['plan'][gid][day]
        orderedJobIds = [a['job_id'] for a in assignments]
        sumRoute = 0.0
        # virtual row: base -> first
        if route_jobs and len(route_jobs) > 0 and route_jobs[0].get('route_distance_km') is not None:
            first = route_jobs[0]
            print('virtual base->first leg km =', first.get('route_distance_km'))
            sumRoute += float(first.get('route_distance_km'))
        # job rows: apply same rules as JS
        for idx, aid in enumerate(orderedJobIds):
            # find job in route_jobs
            rj = next((r for r in route_jobs if r['id'] == aid), None)
            distanceKm = None
            if route_jobs:
                if len(route_jobs) == 1:
                    # single-job day -> job row should be empty
                    distanceKm = None
                else:
                    # multiple-job day: only idx>0 job rows have leg
                    if idx > 0 and rj and rj.get('route_distance_km') is not None:
                        distanceKm = rj.get('route_distance_km')
            # fallback
            if distanceKm is None and rj and 'distance_km' in rj:
                distanceKm = rj['distance_km']
            if isinstance(distanceKm, (int, float)):
                sumRoute += float(distanceKm)
                print(f'job {aid} leg km =', distanceKm)
            else:
                print(f'job {aid} leg km = (none)')
        print('sumRoute =', sumRoute, 'route_total =', route_total, 'diff =', None if route_total is None else sumRoute - float(route_total))

print('\nDone test')
