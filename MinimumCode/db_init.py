# backend/db_init.py
from app import create_app
from models import db, Job, Group
import json
import os

def init_db():
    # ایجاد app
    app = create_app()

    # اطمینان از وجود دایرکتوری برای دیتابیس
    db_dir = os.path.dirname(os.path.abspath('power.db'))
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    with app.app_context():
        # ایجاد جداول
        db.create_all()

        # خواندن داده‌های نمونه از فایل
        try:
            with open('sample_data.json', 'r', encoding='utf-8') as f:
                sample_data = json.load(f)
        except FileNotFoundError:
            sample_data = {
                "jobs": [
                    {
                        "id": "job-001",
                        "address": "مشهد، خیابان امام رضا",
                        "lat": 36.2972,
                        "lon": 59.6067,
                        "priority": 1,
                        "estimated_person_hours": 3.5,
                        "constraints": ["finish_by_monday"]
                    }
                ],
                "groups": [
                    {
                        "id": "crew-A",
                        "label": "گروه تعمیرات",
                        "members_count": 3,
                        "daily_capacity_hours": 24,
                        "skills": "repair",
                        "base_lat": 36.2972,
                        "base_lon": 59.6067
                    }
                ]
            }

        # افزودن کارها به دیتابیس
        for job_data in sample_data.get('jobs', []):
            existing_job = Job.query.get(job_data['id'])
            if not existing_job:
                job = Job(
                    id=job_data['id'],
                    address=job_data.get('address'),
                    lat=job_data.get('lat'),
                    lon=job_data.get('lon'),
                    priority=job_data.get('priority', 1),
                    estimated_person_hours=job_data.get('estimated_person_hours', 2.0),
                    constraints=','.join(job_data.get('constraints', [])),
                    requires=','.join(job_data.get('requires', []))
                )
                db.session.add(job)

        # افزودن گروه‌ها به دیتابیس
        for group_data in sample_data.get('groups', []):
            existing_group = Group.query.get(group_data['id'])
            if not existing_group:
                group = Group(
                    id=group_data['id'],
                    label=group_data.get('label'),
                    members_count=group_data.get('members_count', 2),
                    daily_capacity_hours=group_data.get('daily_capacity_hours', 16),
                    skills=','.join(group_data.get('skills', [])) if isinstance(group_data.get('skills'), list) else group_data.get('skills', ''),
                    base_lat=group_data.get('base_lat'),
                    base_lon=group_data.get('base_lon')
                )
                db.session.add(group)

        # ذخیره تغییرات
        db.session.commit()
        print("دیتابیس با موفقیت مقداردهی اولیه شد.")

if __name__ == "__main__":
    init_db()