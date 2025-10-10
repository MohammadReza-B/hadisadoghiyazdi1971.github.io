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
 
<a href="https://fa.wikipedia.org/wiki/%D9%BE%D8%A7%DB%8C%DA%AF%D8%A7%D9%87_%D8%AF%D8%A7%D8%AF%D9%87_%D8%A8%D8%B1%D8%AF%D8%A7%D8%B1%DB%8C#:~:text=FAISS%3A%20%DA%A9%D8%AA%D8%A7%D8%A8%D8%AE%D8%A7%D9%86%D9%87%E2%80%8C%D8%A7%DB%8C%20%D9%85%D9%86%D8%A8%D8%B9%E2%80%8C%D8%A8%D8%A7%D8%B2%20%DA%A9%D9%87%20%D8%AA%D9%88%D8%B3%D8%B7,%D8%AD%D8%AC%D9%85%20%D8%A8%D8%A7%D9%84%D8%A7%20%D8%B7%D8%B1%D8%A7%D8%AD%DB%8C%20%D8%B4%D8%AF%D9%87%20%D8%A7%D8%B3%D8%AA." style="text-decoration:none; color:green;" target="_blank">
      <strong>FAISS</strong>
    </a> (مخفف Facebook AI Similarity Search) یک کتابخانه اوپن‌سورس است که توسط تیم AI Research فیسبوک (متا) توسعه داده شده است. این کتابخانه برای **جستجوی شباهت بردارها** (Vector Similarity Search) بهینه‌سازی شده است.

ابتدا پایگاه داده برداری بحث می کنیم 


پایگاه‌های داده برداری، نسل جدیدی از سیستم‌های ذخیره‌سازی هستند که نه تنها داده‌ها را نگهداری می‌کنند، بلکه **معنا و رابطه** بین آن‌ها را نیز درک می‌کنند. این فناوری در قلب تحولات هوش مصنوعی، به‌ویژه در کار با مدل‌های زبانی بزرگ (LLM) و داده‌های بدون ساختار (مانند متن، تصویر و صدا) قرار دارد. برخلاف پایگاه‌های داده سنتی (SQL) که بر تطابق دقیق در داده‌های ساختاریافته تکیه دارند، پایگاه‌های داده برداری امکان جستجو بر اساس **شباهت معنایی** را فراهم می‌کنند.

**چرا پایگاه داده برداری؟ مشکل چیست؟**
در یک پایگاه داده سنتی، اگر داده‌ها به صورت بردار (تعبیه یا Embedding) ذخیره شوند، انجام یک جستجوی ساده (مثلاً یافتن مشابه‌ترین آیتم) به دلیل دو چالش اصلی بسیار ناکارآمد خواهد بود:
1.  **ابعاد بالا:** بردارها اغلب صدها یا هزاران بعد دارند و مقایسه آن‌ها پرهزینه است.
2.  **مقیاس‌پذیری:** محاسبه شباهت بین یک بردار پرس‌وجو و میلیون‌ها بردار ذخیره‌شده، از توان پایگاه‌های سنتی خارج است و پاسخ‌دهی بلادرنگ را غیرممکن می‌سازد.

**راه‌حل: پایگاه داده‌های برداری**
این پایگاه‌ها با استفاده از نمایه‌های (Indexes) ویژه و الگوریتم‌های **جستجوی تقریبی نزدیک‌ترین همسایه (ANN)**، فضای جستجو را بهینه کرده و امکان یافتن نزدیک‌ترین نتایج را در کسری از ثانیه و در میان میلیاردها داده فراهم می‌کنند. در این سیستم‌ها، بین سرعت و دقت یک **مبادله (Trade-off)** وجود دارد.

**مبانی فنی: بردارها، تعبیه و جستجوی معنایی**
*   **بردار (Vector):** نمایش عددی داده (یک کلمه، تصویر یا سند) به صورت یک لیست از اعداد. کامپیوترها از این طریق می‌توانند داده‌ها را درک و مقایسه کنند.
*   **تعبیه (Embedding):** فرآیند تبدیل داده به بردار. این بردارها به گونه‌ای ایجاد می‌شوند که داده‌های مشابه از نظر معنایی (مانند "پادشاه" و "ملکه") در فضای برداری به یکدیگر نزدیک باشند.
*   **جستجوی معنایی:** به جای تطابق کلمه کلیدی، به دنبال درک **منظور و مفهوم** پرس‌وجو است (مثلاً تشخیص اینکه "پایتون" در یک متن برنامه‌نویسی به مار اشاره ندارد).

**معیارهای سنجش شباهت**
برای مقایسه بردارها از معیارهای ریاضی مختلفی استفاده می‌شود، از جمله:
*   **شباهت کسینوسی:** زاویه بین دو بردار را اندازه می‌گیرد (مقدار ۱ به معنای شباهت کامل).
*   **فاصله اقلیدسی:** فاصله مستقیم بین دو نقطه را اندازه می‌گیرد (مقدار ۰ به معنای شباهت کامل).

**پایگاه‌های داده برداری محبوب**
برخی از گزینه‌های شناخته‌شده عبارتند از:
*   **Pinecone:** یک سرویس کاملاً مدیریت‌شده و کاربرپسند.
*   **Milvus:** یک پایگاه داده منبع‌باز و بسیار مقیاس‌پذیر.
*   **Weaviate:** پایگاه داده منبع‌باز با قابلیت جستجوی ترکیبی (برداری و کلمه‌کلیدی).
*   **Chroma:** ساده و بهینه‌شده برای برنامه‌های مبتنی بر مدل‌های زبانی بزرگ (LLM).
*   **FAISS:** یک کتابخانه بهینه‌شده توسط متا برای جستجوی شباهت.

**موارد استفاده کلیدی**
*   **عوامل مکالمه‌ای (Chatbots):** ذخیره‌سازی و بازیابی حافظه بلندمدت مکالمات برای پاسخ‌دهی متنی.
*   **سیستم‌های توصیه‌گر:** پیشنهاد محصولات، فیلم‌ها یا موسیقی مشابه بر اساس علایق کاربر.
*   **جستجوی معنایی:** یافتن اسناد و محتوای مرتبط بر اساس مفهوم، نه کلمه کلیدی.
*   **جستجوی تصویر و ویدیو:** یافتن محتوای بصری مشابه.

**چالش‌ها**
*   **تعادل سرعت و دقت:** الگوریتم‌های تقریبی ممکن است همیشه دقیق‌ترین نتیجه را برنگردانند.
*   **هزینه و منابع:** پردازش بردارهای با ابعاد بالا به سخت‌افزار قدرتمند نیاز دارد.
*   **ادغام با سیستم‌های سنتی:** یکپارچه‌سازی با پایگاه‌های داده رابطه‌ای موجود می‌تواند پیچیده باشد.

**جمع‌بندی نهایی**
پایگاه‌های داده برداری با امکان **ذخیره‌سازی و جستجوی هوشمند** بر اساس معنا و شباهت، زیرساخت ضروری برای نسل جدید برنامه‌های هوش مصنوعی هستند. آن‌ها با حل مشکل کار با داده‌های حجیم و بدون ساختار، دنیای تعامل با ماشین را متحول کرده‌اند.


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


## آزمایش
**برای انجام این آزمایش ابتدا باید پایتون گونه 3.12 داشته باشید با بالاتر از آن دچار بحران! می شوید**

### محیط جدید
python -m venv "torch_env_fixed"

### فعال کردن
torch_env_fixed\Scripts\activate

### نصب ها 

If you’re on CPU:

pip install faiss-cpu

If you have a CUDA GPU:

pip install faiss-gpu

pip install sentence_transformers

حالا اولین تبدیل متن به بردار

```python
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

docs = [
    "The capital of France is Paris.",
    "Machine learning is a subset of AI.",
    "The Mona Lisa is in the Louvre."
]

# Encode documents into vectors
embeddings = model.encode(docs, convert_to_numpy=True)
```

output:
[[ 0.10325696  0.03042014  0.02909579 ...  0.05853157  0.08585992
  -0.0056698 ]
 [-0.03637548 -0.02661065  0.06555219 ...  0.05287919  0.06833272
  -0.06037488]
 [ 0.00113731 -0.04676315  0.00223458 ...  0.01240106  0.0471148
  -0.06059993]]

```python
import faiss
import numpy as np

# Create a FAISS index
dim = embeddings.shape[1]  # vector dimension
index = faiss.IndexFlatL2(dim)  # L2 distance
index.add(embeddings)  # add vectors to the index

print("Number of vectors in index:", index.ntotal)
```

output: Number of vectors in index: 3

## جستجوی 2-NN

```python 
query = "Where is the Mona Lisa located?"
query_vec = model.encode([query], convert_to_numpy=True)

# Search top-2 results
k = 2
distances, indices = index.search(query_vec, k)

for i, idx in enumerate(indices[0]):
    print(f"Result {i+1}: {docs[idx]} (distance={distances[0][i]:.4f})")
```

output is:
Result 1: The Mona Lisa is in the Louvre. (distance=0.3544)
Result 2: The capital of France is Paris. (distance=1.5152)

### **مرحله ۵: افزودن بازیاب (Retriever) به معماری RAG**

* FAISS تنها نقش بازیاب را ایفا می‌کند.
* شما آن را به یک مدل مولد (مانند gpt-neo, llama.cpp یا یک فراخوان API به OpenAI/Gemini) متصل می‌کنید تا خط لوله کامل RAG شکل بگیرد:

  ۱. کاربر سوال می‌پرسد.
  ۲. بازیابی اسناد برتر (top-k) با FAISS.
  ۳. الحاق اسناد + سوال → ورودی به مدل زبانی بزرگ (LLM).

### مثال

  ```python 
  retrieved_docs = [docs[idx] for idx in indices[0]]
context = "\n".join(retrieved_docs)

prompt = f"Answer the question using the context:\n\n{context}\n\nQuestion: {query}"
print(prompt)
```

output is:
Answer the question using the context:

The Mona Lisa is in the Louvre.
The capital of France is Paris.

Question: Where is the Mona Lisa located?



## آنچه باید از FAISS و Transformer به زبان ساده بدانیم

**تشبیه ساده**

### Transformer
- **یک مترجم متخصص** که متن را به "زبان ریاضی" ترجمه می‌کند
- **درک معنایی**: متن را به بردارهای عددی تبدیل می‌کند
- **حفظ معنا**: بردارها معنای متن را حفظ می‌کنند
- **تشابه معنایی**: متون مشابه، بردارهای نزدیک دارند
- **درک ظرافت‌های زبانی**

### FAISS  
- **یک کتابدار فوق‌سریع** که می‌داند هر کتاب (بردار) کجای کتابخانه قرار دارد
- **جستجوی سریع**: بردارهای مشابه را سریع پیدا می‌کند
- **بدون درک معنایی**: نمی‌فهمد چه چیزی شبیه چیست!

## ✨ نقش دقیق FAISS

### ۱. پایگاه داده بهینه‌شده برای بردارها
### ۲. مقیاس‌پذیری با داده‌های بزرگ  
### ۳. انواع الگوریتم‌های بهینه‌شده

## ⚡ مقایسه سرعت

### با FAISS:
- برای ۱,۰۰۰,۰۰۰ سند → ~۱۰۰-۱۰۰۰ محاسبه فاصله
- **۱۰۰۰x سریع‌تر!**

## 📊 انواع Index در FAISS

| نوع Index | کاربرد | سرعت | دقت |
|-----------|--------|------|------|
| `IndexFlatL2` | داده‌های کوچک | متوسط | ۱۰۰٪ |
| `IndexIVFFlat` | داده‌های متوسط | سریع | بالا |
| `IndexIVFPQ` | داده‌های بزرگ | بسیار سریع | خوب |
| `IndexHNSW` | داده‌های خیلی بزرگ | فوق‌سریع | عالی |

## 🏗️ معماری RAG کامل

### مرحله ۵: افزودن بازیاب (Retriever) به معماری RAG

- FAISS تنها نقش **بازیاب** را ایفا می‌کند
- آن را به یک مدل مولد متصل می‌کنید تا خط لوله کامل RAG شکل بگیرد

### مراحل کار:

۱. **کاربر سوال می‌پرسد**
۲. **بازیابی اسناد برتر (top-k) با FAISS**  
۳. **الحاق اسناد + سوال → ورودی به مدل زبانی بزرگ (LLM)**

## 🎯 جمع‌بندی نهایی

### FAISS = سیستم بازیابی اطلاعات برای بردارها

- **ورودی**: بردار جستجو
- **خروجی**: نزدیک‌ترین بردارها در پایگاه داده  
- **مزیت**: سرعت و مقیاس‌پذیری
- **جایگاه**: بین ترنسفورمر (درک معنا) و LLM (تولید پاسخ)

### Transformer = فهم معنایی  
### FAISS = جستجوی سریع

**بدون FAISS، RAG برای داده‌های واقعی غیرعملی می‌شود!**

