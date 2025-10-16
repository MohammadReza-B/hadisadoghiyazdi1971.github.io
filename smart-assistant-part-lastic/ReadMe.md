خیلی عالی 👌
اینجا یک فایل کامل و آموزشی به نام `README.md` (یا اگر خواستید دقیقاً طبق خواسته‌تان `ReadMe.rd`) برای پروژه‌ی **Scrapy + ایندکس‌سازی** شما آماده کرده‌ام.
این فایل برای زمانی طراحی شده که مدتی بعد به پروژه برگردید و دقیق یادتان بیاید باید چه کنید و چرا هر مرحله مهم است.

---

## 📘 **فایل: ReadMe.rd**

````markdown
# 🕷️ پروژه خزیدن و ایندکس‌سازی محتوای سایت‌ها با Scrapy و FAISS

این فایل برای مرور کامل مراحل کار طراحی شده تا بعد از گذشت زمان، فراموشی یا سردرگمی پیش نیاید.  
پروژه از دو بخش اصلی تشکیل شده است:

1. **خزیدن (Crawling)** داده‌های وب با `Scrapy`  
2. **ایندکس‌سازی (Indexing)** داده‌ها با اسکریپت `AdvancedFAISSIndexCreator`

---

## 📍 بخش ۱ — اجرای خزنده Scrapy

### 🧩 هدف
جمع‌آوری متن‌های فارسی از سایت‌های دلخواه (مثل `partlasticgroup.com`)  
و ذخیره‌ی آن‌ها در پوشه‌ی `documents/` برای آماده‌سازی ایندکس.

---

### ⚙️ 1. فعال‌سازی محیط مجازی (Virtual Env)
ابتدا محیط پایتون مخصوص پروژه را فعال کنید:

```bash
H:\path\to\rag_env\Scripts\activate
````

اگر هنوز Scrapy نصب نشده:

```bash
pip install scrapy
```

برای اطمینان از نصب صحیح:

```bash
scrapy version
```

---

### 🏗️ 2. ساخت پروژه Scrapy (فقط بار اول)

اگر هنوز پروژه Scrapy ندارید:

```bash
scrapy startproject partlastic_crawler
cd partlastic_crawler
```

پوشه‌ای ساخته می‌شود شامل:

```
partlastic_crawler/
  ├── scrapy.cfg
  └── partlastic_crawler/
      ├── spiders/
      └── settings.py
```

---

### 🕸️ 3. ساخت یا ویرایش فایل خزنده (spider)

در مسیر:

```
partlastic_crawler/spiders/partlastic_spider.py
```

کد زیر را قرار دهید یا ویرایش کنید:

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re, os

class PartlasticSpider(CrawlSpider):
    name = "partlastic"
    allowed_domains = ["partlasticgroup.com"]
    start_urls = [
        "https://partlasticgroup.com/",
        # در صورت نیاز آدرس‌های جدید را در این لیست اضافه کنید
    ]

    rules = (
        Rule(LinkExtractor(allow=()), callback="parse_page", follow=True),
    )

    def clean_text(self, html):
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[\r\n\t]+", " ", text)
        return text.strip()

    def parse_page(self, response):
        text = self.clean_text(response.text)
        if len(text) > 300 and re.search(r"[\u0600-\u06FF]", text):  # فقط صفحات فارسی
            os.makedirs("documents", exist_ok=True)
            filename = re.sub(r"[^a-zA-Z0-9]+", "_", response.url)[:80] + ".txt"
            path = os.path.join("documents", filename)
            if os.path.exists(path):  # از تکرار جلوگیری می‌کند
                self.log(f"⏩ Skipped existing: {path}")
                return
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            self.log(f"✅ Saved clean text: {path}")
```

---

### 🌐 4. اجرای خزنده

از مسیر اصلی پروژه که `scrapy.cfg` در آن است، اجرا کنید:

```bash
scrapy crawl partlastic
```

اگر خطا داد که Scrapy شناخته نشد:

```bash
python -m scrapy crawl partlastic
```

---

### 📁 5. نتایج خزیدن

پس از پایان کار، پوشه‌ای ساخته می‌شود:

```
documents/
   ├── partlasticgroup_com_index.txt
   ├── partlasticgroup_com_about_us.txt
   └── ...
```

هر فایل حاوی متن تمیز و بدون HTML صفحات سایت است.

---

### 💡 نکات مهم برای دفعات بعد:

| موقعیت               | توضیح                                                                   |
| -------------------- | ----------------------------------------------------------------------- |
| افزودن آدرس‌های جدید | کافی است در `start_urls` بنویسید                                        |
| حذف آدرس‌های قدیمی   | آدرس‌های قدیمی را از `start_urls` پاک کنید (اطلاعات قبلی محفوظ می‌ماند) |
| اجرای مجدد خزنده     | فایل‌های جدید به `documents` اضافه می‌شوند                              |
| جلوگیری از بازنویسی  | شرط `if os.path.exists(path)` مانع می‌شود                               |
| شروع از صفر          | پوشه `documents/` را دستی پاک کنید تا دوباره ساخته شود                  |

---

## 📍 بخش ۲ — ایندکس‌سازی با FAISS

بعد از اینکه داده‌ها در پوشه‌ی `documents` آماده شدند، مرحلهٔ دوم آغاز می‌شود.

---

### ⚙️ 1. پیش‌نیازها

در همان محیط مجازی (`rag_env`):

```bash
pip install sentence-transformers faiss-cpu scikit-learn tqdm numpy
```

---

### ⚙️ 2. اجرای ایندکس‌ساز

فایل اصلی ایندکس‌سازی شما:

```
83092fb9-9cb3-4d86-93a7-5d26f33fa1b7.py
```

را در مسیر پروژه اجرا کنید:

```bash
python 83092fb9-9cb3-4d86-93a7-5d26f33fa1b7.py
```

---

### 📦 3. خروجی‌های نهایی

پس از اجرا، در پوشه‌ی `index_v4_upgraded/` فایل‌های زیر ساخته می‌شود:

```
index_v4_upgraded/
  ├── faiss_index_upgraded.index
  ├── enhanced_metadata.json
  └── comprehensive_summary.json
```

این‌ها برای جستجو و پاسخ‌دهی هوشمند (RAG) استفاده می‌شوند.

---

## 🧠 نکات یادآوری نهایی

* **هر بار که سایت جدیدی می‌خزید**، لازم نیست ایندکس‌سازی قبلی را پاک کنید؛ می‌توانید فایل‌های جدید را اضافه کنید و دوباره FAISS را اجرا کنید.
* **اگر خطای "no active project" دیدید**، یعنی در مسیر اشتباهی هستید — باید همان‌جایی باشید که فایل `scrapy.cfg` وجود دارد.
* **اگر Scrapy شناخته نمی‌شود**، با دستور `python -m scrapy crawl partlastic` اجرا کنید.
* **در ویندوز**، از CMD معمولی استفاده کنید نه PowerShell (در برخی نسخه‌ها PATH درست تنظیم نمی‌شود).

---

## 📋 خلاصه مسیر اجرای کلی پروژه

```
(1) فعال‌سازی محیط مجازی
(2) scrapy crawl partlastic   ← برای جمع‌آوری داده‌ها
(3) python advanced_faiss_indexer.py  ← برای ایندکس کردن متن‌ها
(4) استفاده از index در دستیار هوشمند
```

---

✍️ **نکته پایانی:**
برای سایت‌های دیگر نیز می‌توانید یک فایل spider جدید در پوشه‌ی `spiders/` بسازید،
و فقط `allowed_domains` و `start_urls` را تغییر دهید.
به این ترتیب همه‌ی داده‌ها در یک `documents/` جمع می‌شوند و آماده‌ی ایندکس هستند.


می توان چندین ادرس برای بیس و محل جستجو داشت 
start_urls = [
    "https://partlasticgroup.com/",
    "https://another-site.com/",
    "https://example.ir/"
]

allowed_domains = [
    "partlasticgroup.com",
    "another-site.com",
    "example.ir"
]


