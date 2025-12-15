# generate_sample_data.py (بخش‌های تصحیح‌شده)
import json, random
import os
import urllib.request
import urllib.parse
import math
from models import db, Group, Job
from app import create_app

OUT = "sample_data.json"

# مختصات مستطیل مورد نظر
# a=[36.2991, 59.6086] b=[36.513344,59.483414] c=[36.212545,59.601517] d=[36.323268,59.712753]
# محاسبه محدوده مستطیل
min_lat = min(36.2991, 36.513344, 36.212545, 36.323268)
max_lat = max(36.2991, 36.513344, 36.212545, 36.323268)
min_lon = min(59.6086, 59.483414, 59.601517, 59.712753)
max_lon = max(59.6086, 59.483414, 59.601517, 59.712753)

# مرکز جعبه
center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2

# انحراف معیار برای توزیع گوسی (حدود 1/4 عرض جعبه)
lat_std = (max_lat - min_lat) / 10#4
lon_std = (max_lon - min_lon) / 10#4

def reverse_geocode(lat, lon):
    """
    استخراج نام مکان از Nominatim (OpenStreetMap) استفاده کنید
    """
    try:
        params = urllib.parse.urlencode({
            'lat': lat,
            'lon': lon,
            'format': 'json',
            'zoom': 18,
            'addressdetails': 1,
            'language': 'fa'
        })
        url = f"https://nominatim.openstreetmap.org/reverse?{params}"
        
        # User-Agent لازم است برای Nominatim
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'PowerScheduler/1.0 (https://github.com/yourusername)')
        
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if 'address' in data:
                addr = data['address']
                # ترجیح به نام فارسی (address) اگر موجود باشد
                road = addr.get('road', '')
                neighbourhood = addr.get('neighbourhood', '')
                suburb = addr.get('suburb', '')
                city = addr.get('city', '')
                
                # ترکیب بخش‌های معنادار
                parts = []
                if city:
                    parts.append(city)
                if neighbourhood:
                    parts.append(neighbourhood)
                if road:
                    parts.append(road)
                if suburb:
                    parts.append(suburb)
                
                if parts:
                    return ', '.join(parts[:3])  # حداکثر 3 بخش
            
            return data.get('display_name', f'{lat}, {lon}')
    except Exception as e:
        print(f"Geocoding error for ({lat}, {lon}): {e}")
        return f"مشهد - موقعیت {lat:.4f}, {lon:.4f}"

def gaussian_clamped(mu, sigma, min_val, max_val):
    """
    تولید عدد تصادفی با توزیع گوسی که در محدوده [min_val, max_val] باقی بماند
    """
    while True:
        # تولید عدد با توزیع گوسی
        value = random.gauss(mu, sigma)
        # اطمینان از قرارگیری در محدوده
        if min_val <= value <= max_val:
            return value
        # اگر خارج از محدوده بود، دوباره امتحان کن

def rand_coord_gaussian():
    """
    تولید مختصات با توزیع گوسی حول مرکز جعبه
    """
    lat = gaussian_clamped(center_lat, lat_std, min_lat, max_lat)
    lon = gaussian_clamped(center_lon, lon_std, min_lon, max_lon)
    return round(lat, 6), round(lon, 6)

# تولید 5 گروه
groups = []
group_names = ["تیم الف", "تیم ب", "تیم ج", "تیم د", "تیم ه"]
for i in range(1, 6):
    members = random.choice([2, 3])
    lat, lon = rand_coord_gaussian()
    skills_choice = random.choice([["crane"], ["high_voltage"], []])
    
    groups.append({
        "id": f"crew-{i:02d}",
        "label": group_names[i-1],
        "members_count": members,
        "daily_capacity_hours": 6,
        "skills": skills_choice,
        "base_lat": lat,
        "base_lon": lon,
        "history_workload": 0.0
    })

# تولید 35 کار با نام‌های خودکار از OSM
jobs = []
for j in range(1, 36):
    lat, lon = rand_coord_gaussian()
    
    # دریافت نام مکان از Nominatim
    address = reverse_geocode(lat, lon)
    print(f"Job {j}: {address} ({lat}, {lon})")
    
    cons = []
    requires = []
    
    if random.random() < 0.15:
        cons.append("only_saturday")
    if random.random() < 0.25:
        cons.append("finish_by_monday")
    if random.random() < 0.2:
        requires.append("crane")
    
    # اطمینان از فرمت صحیح اعداد (بدون تغییر فرمت)
    estimated_hours = round(random.uniform(1.0, 6.0), 1)
    
    jobs.append({
        "id": f"job-{j:03d}",
        "address": address,
        "lat": lat,
        "lon": lon,
        "priority": random.choice([1, 2, 3]),
        "estimated_person_hours": estimated_hours,
        "constraints": cons,
        "requires": requires
    })

# ذخیره در فایل JSON با فرمت دقیق
data = {
    "groups": groups,
    "jobs": jobs
}

# استفاده از تنظیمات دقیق برای JSON
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ': '))

print(f"✅ Sample data generated and saved to {OUT}")

# ایجاد app و ذخیره در دیتابیس
app = create_app()
with app.app_context():
    db.create_all()
    
    existing_groups = Group.query.count()
    existing_jobs = Job.query.count()
    
    if existing_groups == 0:
        for g in groups:
            group = Group(
                id=g["id"],
                label=g["label"],
                members_count=g["members_count"],
                daily_capacity_hours=g["daily_capacity_hours"],
                skills=",".join(g["skills"]),
                base_lat=g["base_lat"],
                base_lon=g["base_lon"]
            )
            db.session.add(group)
        print(f"✅ {len(groups)} گروه در دیتابیس ذخیره شد")
    else:
        print(f"⚠️  {existing_groups} گروه از قبل در دیتابیس موجود است")
    
    if existing_jobs == 0:
        for j in jobs:
            # مدیریت مقادیر خالی برای requires و constraints
            requires_str = ",".join(j["requires"]) if j["requires"] else None
            constraints_str = ",".join(j["constraints"]) if j["constraints"] else None
            
            job = Job(
                id=j["id"],
                address=j["address"],
                lat=j["lat"],
                lon=j["lon"],
                priority=j["priority"],
                estimated_person_hours=j["estimated_person_hours"],
                constraints=constraints_str,
                requires=requires_str
            )
            db.session.add(job)
        print(f"✅ {len(jobs)} کار در دیتابیس ذخیره شد")
    else:
        print(f"⚠️  {existing_jobs} کار از قبل در دیتابیس موجود است")
    
    db.session.commit()

print("✅ عملیات تکمیل شد")