# backend/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()

class WorkDay(enum.Enum):
    Saturday = "Saturday"
    Sunday = "Sunday"
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.String, primary_key=True)
    address = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    priority = db.Column(db.Integer)
    estimated_person_hours = db.Column(db.Float)
    max_allowable_increase = db.Column(db.Float, default=6.6)
    constraints = db.Column(db.String)  # JSON string or comma-separated
    requires = db.Column(db.String)  # e.g. 'crane'
    arrival_time = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String)

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.String, primary_key=True)
    label = db.Column(db.String)
    members_count = db.Column(db.Integer)
    daily_capacity_hours = db.Column(db.Float)
    skills = db.Column(db.String)  # comma-separated
    base_lat = db.Column(db.Float)
    base_lon = db.Column(db.Float)
    history_workload = db.Column(db.Float, default=0.0)

class PlanEntry(db.Model):
    __tablename__ = 'plan_entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.String)
    group_id = db.Column(db.String)
    day = db.Column(db.String)  # Saturday..Wednesday
    start_time = db.Column(db.Float)  # hour of day (e.g. 7.5 for 07:30)
    duration = db.Column(db.Float)  # person-hours

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.String)
    week_start = db.Column(db.String)
    total_hours = db.Column(db.Float)
