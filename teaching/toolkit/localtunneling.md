---
layout: persian
classes: wide rtl-layout
dir: rtl
title: "چگونه تونل بسازیم و سرور با ادرس  ثابت  راه اندازی کنیم"
permalink: /teaching//studenteffort/toolkit/localtunneling/
author_profile: true

header:
  overlay_image: "/assets/images/background.jpg"
  overlay_filter: 0.3
  overlay_color: "#5e616c"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
---

## 📋 فهرست مطالب
- [PM2 چیست؟](#pm2-چیست)
- [توضیحات tunnel.js](#توضیحات-tunneljs)
- [روش اجرا](#روش-اجرا)
- [عیب‌یابی](#عیب‌یابی)
- [FAISS چیست؟ یک راهنمای کامل](#faiss-چیست-یک-راهنمای-کامل)


## PM2 چیست؟

**PM2 (Process Manager 2)** یک مدیریت‌کننده process برای برنامه‌های Node.js است که:

### 🎯 مزایای PM2:
- **ریستارت خودکار** اگر برنامه crash کند
- **مانیتورینگ** وضعیت processes
- **لاگ‌گیری** متمرکز
- **شروع خودکار** پس از ریبوت سیستم
- **مدیریت حافظه** و CPU


### 🔧 دستورات مهم PM2:
```bash
# شروع برنامه
pm2 start tunnel.js --name "tunnel"

# مشاهده وضعیت
pm2 status

# مشاهده لاگ‌ها
pm2 logs tunnel

# توقف برنامه
pm2 stop tunnel

# ریستارت
pm2 restart tunnel

# حذف از لیست
pm2 delete tunnel

# ذخیره configuration
pm2 save
```

### ⚙️ چرا از PM2 استفاده کردیم؟
- وقتی LocalTunnel قطع می‌شود، PM2 به طور خودکار آن را ریستارت می‌کند
- مدیریت بهتر لاگ‌ها و خطاها
- امکان مانیتورینگ از راه دور

## توضیحات tunnel.js

### 📜 کد کامل:
```javascript
// tunnel.js
const { exec } = require('child_process');

console.log('🚀 Starting localtunnel...');

const child = exec('npx localtunnel --port 5000 --subdomain hadisadoghiyazdi');

child.stdout.on('data', (data) => {
  const output = data.toString().trim();
  console.log(`[LT] ${output}`);
  
  if (output.includes('your url is:')) {
    console.log('✅ Tunnel is ready! No password required.');
  }
});

child.stderr.on('data', (data) => {
  console.error(`[LT-ERROR] ${data.toString().trim()}`);
});

child.on('close', (code) => {
  console.log(`❌ Tunnel exited with code ${code}`);
  process.exit(code || 1);
});
```

### 🔍 توضیح خط به خط:

1. **وارد کردن ماژول‌ها**:
   ```javascript
   const { exec } = require('child_process');
   ```
   - برای اجرای دستورات سیستم عامل

2. **اجرای LocalTunnel**:
   ```javascript
   const child = exec('npx localtunnel --port 5000 --subdomain hadisadoghiyazdi');
   ```
   - ایجاد تونل روی پورت 5000
   - استفاده از subdomain ثابت

3. **مدیریت خروجی**:
   ```javascript
   child.stdout.on('data', (data) => {
     console.log(`[LT] ${output}`);
   });
   ```
   - نمایش خروجی استاندارد

4. **مدیریت خطاها**:
   ```javascript
   child.stderr.on('data', (data) => {
     console.error(`[LT-ERROR] ${data.toString().trim()}`);
   });
   ```
   - نمایش خطاهای سیستم

5. **مدیریت بسته شدن**:
   ```javascript
   child.on('close', (code) => {
     console.log(`❌ Tunnel exited with code ${code}`);
     process.exit(code || 1);
   });
   ```
   - وقتی تونل بسته می‌شود، PM2 آن را ریستارت می‌کند

## روش اجرا

### 🚀 راه‌اندازی سریع:
1. **فایل `main.bat` را اجرا کنید**
2. **صبر کنید تا همه سرویس‌ها راه‌اندازی شوند**
3. **پسورد نمایش داده شده را کپی کنید**
4. **به آدرس `https://hadisadoghiyazdi.loca.lt` بروید**
5. **پسورد را وارد کنید**

### 📝 فایل main.bat:
```batch
@echo off
cd /d "H:\HadiSadoghiYazdi\hadisadoghiyazdi1971.github.io\hadisadoghiyazdi1971.github.io\smart-repair-api"
title Smart Repair System

echo ========================================
echo 🚀 Starting System
echo ========================================

echo Step 1: Starting Flask...
start "Flask Server" python app.py
timeout /t 3 >nul

echo Step 2: Stopping old tunnel (if exists)...
call pm2 delete tunnel >nul 2>&1
timeout /t 2 >nul

echo Step 3: Starting new tunnel with pm2...
call pm2 start tunnel.js --name "tunnel" --restart-delay 3000
timeout /t 8 >nul

echo Step 4: Getting password...
powershell -Command "(Invoke-WebRequest -Uri 'https://loca.lt/mytunnelpassword' -UseBasicParsing).Content.Trim()" > password.txt
set /p TUNNEL_PASSWORD=<password.txt

echo.
echo ✅ SYSTEM READY!
echo 📍 Flask: http://localhost:5000
echo 🌐 Tunnel: https://hadisadoghiyazdi.loca.lt
echo 🔑 Password: %TUNNEL_PASSWORD%
echo.
echo To view tunnel logs: pm2 logs tunnel
echo To stop tunnel: pm2 stop tunnel
echo.
pause
```

## عیب‌یابی

### 🔧 مشکلات رایج و راه‌حل‌ها:

1. **تونل قطع می‌شود**:
   - PM2 به طور خودکار ریستارت می‌کند
   - دستی: `pm2 restart tunnel`

2. **پسورد کار نمی‌کند**:
   - جدید بگیرید: `https://loca.lt/mytunnelpassword`
   - در فایل `password.txt` ذخیره می‌شود

3. **PM2 کار نمی‌کند**:
   - از `node tunnel.js` مستقیم استفاده کنید
   - یا از `npx pm2` استفاده کنید

4. **پورت 5000 ت است**:
   - برنامه‌های دیگر را ببندید
   - یا پورت را در `app.py` تغییر دهید

### 📞 دستورات مفید برای دیباگ:
```bash
# بررسی processes
pm2 status

# مشاهده لاگ‌های زنده
pm2 logs tunnel

# بررسی پورت
netstat -ano | findstr :5000

# بررسی سرویس Flask
curl http://localhost:5000/health
```

## 🎯 نکات نهایی

- سیستم با **دیتابیس فایل‌محل** کار می‌کند
- **اتصال اینترنتی** با LocalTunnel برقرار می‌شود
- **مدیریت خطا** با PM2 انجام می‌شود
- **پسورد** هر 7 روز یکبار تغییر می‌کند


## FAISS چیست؟ یک راهنمای کامل

## معرفی کلی
**FAISS** (مخفف Facebook AI Similarity Search) یک کتابخانه اوپن‌سورس است که توسط تیم AI Research فیسبوک (متا) توسعه داده شده است. این کتابخانه برای **جستجوی شباهت بردارها** (Vector Similarity Search) بهینه‌سازی شده است.

## مشکل اصلی که FAISS حل می‌کند
وقتی با داده‌های برداری (Vector Data) کار می‌کنید - مانند:
- امبدینگ‌های متنی
- امبدینگ‌های تصویری
- امبدینگ‌های صوتی

جستجوی مستقیم و مقایسه تمام بردارها با یکدیگر به دلیل **مشکل مقیاس‌پذیری** بسیار کند است. FAISS این مشکل را حل می‌کند.

## چگونه کار می‌کند؟

### الگوریتم‌های اصلی
1. **ایندکس کردن** (Indexing):
   - بردارها را در ساختارهای بهینه‌شده ذخیره می‌کند
   - از تکنیک‌هایی مانند **کوانتیزاسیون** (Quantization) برای فشرده‌سازی استفاده می‌کند

2. **جستجوی سریع**:
   - از الگوریتم‌هایی مانند **IVF** (Inverted File Index)
   - **HNSW** (Hierarchical Navigable Small World)
   - **محاسبه فاصله** (Distance Calculation) بهینه‌شده

## انواع ایندکس در FAISS

### پایه‌ای
- **IndexFlatL2**: جستجوی دقیق با فاصله اقلیدسی
- **IndexFlatIP**: جستجوی دقیق با ضرب داخلی

### بهینه‌شده برای حافظه
- **IndexIVFFlat**: ترکیب جستجوی تقریبی و دقیق
- **IndexPQ**: فشرده‌سازی پیشرفته با Product Quantization

### ترکیبی
- **IndexIVFPQ**: ترکیب IVF و PQ برای کارایی بالاتر

## نصب و راه‌اندازی

```bash
# برای CPU
pip install faiss-cpu

# برای GPU (اگر کارت گرافیک دارید)
pip install faiss-gpu
```

## مثال عملی ساده

```python
import faiss
import numpy as np

# تولید داده‌های نمونه
dimension = 128  # بعد بردارها
num_vectors = 10000

# تولید بردارهای تصادفی
vectors = np.random.random((num_vectors, dimension)).astype('float32')

# ایجاد ایندکس
index = faiss.IndexFlatL2(dimension)

# افزودن بردارها به ایندکس
index.add(vectors)

# جستجوی مشابه‌ترین بردارها
query_vector = np.random.random((1, dimension)).astype('float32')
k = 5  # تعداد نتایج
distances, indices = index.search(query_vector, k)

print("مشابه‌ترین بردارها:", indices)
print("فاصله‌ها:", distances)
```

## کاربردهای اصلی

### 1. سیستم‌های RAG (Retrieval-Augmented Generation)
- بازیابی اسناد مرتبط برای مدل‌های زبانی
- بهبود دقت پاسخ‌های ChatGPT-like

### 2. جستجوی تصویر
- پیدا کردن تصاویر مشابه
- سیستم‌های توصیه‌گر بصری

### 3. جستجوی متنی
- پیدا کردن اسناد مشابه
- تشخیص محتوای تکراری

### 4. سیستم‌های توصیه‌گر
- پیدا کردن آیتم‌های مشابه
- توصیه‌های شخصی‌شده

## مزایای کلیدی

### ✅ **سرعت بسیار بالا**
- بهینه‌شده برای پردازش موازی
- پشتیبانی از GPU برای سرعت بیشتر

### ✅ **مقیاس‌پذیری**
- توانایی مدیریت میلیون‌ها بردار
- استفاده بهینه از حافظه

### ✅ **انعطاف‌پذیری**
- پشتیبانی از انواع الگوریتم‌های جستجو
- قابل تنظیم برای نیازهای مختلف

### ✅ **سادگی استفاده**
- API تمیز و مستندات خوب
- جامعه کاربری فعال

## معایب و محدودیت‌ها

### ❌ **فقط ذخیره‌سازی در حافظه**
- داده‌ها با بسته شدن برنامه از بین می‌روند
- نیاز به مدیریت جداگانه برای ذخیره‌سازی پایدار

### ❌ **عدم پشتیبانی از متادیتا**
- فقط بردارها را ذخیره می‌کند
- برای ذخیره اطلاعات اضافی نیاز به راه‌حل جانبی دارید

### ❌ **مدیریت دستی**
- نیاز به بروزرسانی دستی ایندکس
- عدم وجود قابلیت‌های خودکار

## مقایسه با سایر ابزارها

| ابزار | نوع | بهترین استفاده |
|-------|-----|----------------|
| **FAISS** | کتابخانه | نمونه‌سازی سریع، کاربردهای خاص |
| **Pinecone** | سرویس ابری | تولید، مقیاس بزرگ |
| **Weaviate** | دیتابیس برداری | برنامه‌های کامل با متادیتا |
| **Chroma** | دیتابیس برداری | پروژه‌های ساده تا متوسط |

## جمع‌بندی نهایی

FAISS یک **ابزار تخصصی و فوق‌العاده کارآمد** برای:
- تیم‌های تحقیقاتی
- نمونه‌سازی سریع
- کاربردهای خاص با نیاز به عملکرد بالا

اما برای **برنامه‌های تولیدی در مقیاس بزرگ**، ممکن است نیاز به راه‌حل‌های کامل‌تری مانند دیتابیس‌های برداری تخصصی داشته باشید.

**سخن پایانی:** FAISS مثل یک "موتور جستجوی خالص" برای بردارها است - سریع، قدرتمند، ولی نیاز به ساخت بدنه اطراف آن دارید!