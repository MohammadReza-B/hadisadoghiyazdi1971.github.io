
# طراحی و پیاده‌سازی سیستم تصمیم‌ساز خودکار برنامه‌ریزی و زمان‌بندی گروه‌های تعمیراتی


**{کد پروژه : 436/1404 -صدوقی -فرقانی}**



## پیش‌نیازها

- Python 3.12 

## نصب و راه‌اندازی

### 1. دریافت پروژه


### 2. ایجاد محیط مجازی (توصیه می‌شود)


python -m venv powerscheduling

فعال کردن آن
powerscheduling\Scripts\activate


### 3. نصب dependencies
فایل requirements.txt موجود است

```bash
# آپدیت pip
python -m pip install --upgrade pip

# نصب requirements
pip install -r requirements.txt
```

### 4. راه‌اندازی پایگاه داده

```bash
python db_init.py
```

### 5. اجرای برنامه

```bash
python app.py
```

### 6. دسترسی به برنامه

مرورگر را باز کنید و به آدرس زیر بروید:
```
http://localhost:5000
```

## ساختار پروژه

```
project/
│
├── app.py              # فایل اصلی اجرای برنامه
├── db_init.py          # راه‌اندازی اولیه پایگاه داده
├── models.py           # مدل‌های پایگاه داده
├── scheduler.py        # مدیریت زمان‌بندی کارها
├── fix_coordinates_geocoding2.py  # ابزار اصلاح مختصات
├── requirements.txt    # لیست پکیج‌های مورد نیاز
│
├── static/             # فایل‌های استاتیک
│   ├── styles.css      # استایل‌های CSS
│   └── script.js       # اسکریپت‌های JavaScript
│
├── templates/          # قالب‌های HTML
│   ├── index.html      # صفحه اصلی
│   └── map-view.html   # نمایش نقشه
│
├── tools/              # ابزارهای کمکی
│   ├── check_import_app.py
│   ├── export_test.py
│   ├── generate_excel_from_plan.py
│   └── inspect_excel.py
│
└── __pycache__/        # فایل‌های کامپایل شده پایتون
```

## امکانات اصلی

- دریافت درخواست و ثبت در دیتابیس 
- زمانبندی و بهینه سازی
- نمایش نقشه و موقعیت‌های جغرافیایی
- مدیریت و ذخیره‌سازی مختصات
- ابزارهای اصلاح و بهبود داده‌های مکانی
- خروجی اکسل از داده‌ها
- زمان‌بندی کارهای خودکار
- امکان تولید اکسل 

## ابزارهای کمکی

### بررسی داده‌ها
```bash
python tools/inspect_excel.py
```

### تولید اکسل
```bash
python tools/generate_excel_from_plan.py
```

### تست خروجی
```bash
python tools/export_test.py
```

### اصلاح مختصات
```bash
python fix_coordinates_geocoding2.py
```

## مدیریت برنامه

### راه‌اندازی زمان‌بند
```bash
python scheduler.py
```

### راه‌اندازی مجدد پایگاه داده
```bash
python db_init.py
```

