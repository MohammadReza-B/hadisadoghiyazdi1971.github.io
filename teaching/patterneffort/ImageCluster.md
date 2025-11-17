---
layout: persian  # یا single با کلاس rtl-layout
classes: wide rtl-layout
dir: rtl
title: "خوشه بندی تصاویر"
permalink: /teaching/studenteffort/patterneffort/ImageCluster/
author_profile: true

header:
  overlay_image: "/assets/images/background.jpg"
  overlay_filter: 0.3
  overlay_color: "#5e616c"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
---

# استخراج ویژگی از صوت

<div  dir="rtl">
<p >

<p> نویسنده : پارسا سینی چی</p>
  <a href="mailto:p.sinichi@gmail.com">
p.sinichi@gmail.com  </a>
</p>
<p >

  دانشگاه فردوسی مشهد
  مهندسی کامپیوتر
</p>

</div>

<div dir="rtl">


## فهرست مطالب

<ul>
  <li><a href="#مقدمه">مقدمه</a></li>
  <li><a href="#یادگیری-بدون-نظارت-و-خوشهبندی">یادگیری بدون نظارت و خوشه‌بندی</a></li>
  <li><a href="#اهمیت-استخراج-ویژگی">اهمیت استخراج ویژگی</a></li>
  <li><a href="#شبکه-های-عصبی-cnn-و-مدل-vgg16">شبکه های عصبی CNN و مدل VGG16</a></li>
  <li><a href="#توابع-ضرر">توابع ضرر</a>
    <ul>
      <li><a href="#1-تابع-ضرر-مربعی-square-loss--l2">1. تابع ضرر مربعی Square Loss / L2</a></li>
      <li><a href="#2-تابع-ضرر-مطلق-absolute-loss--l1">2. تابع ضرر مطلق Absolute Loss / L1</a></li>
      <li><a href="#3-تابع-huber-loss">3. تابع Huber Loss</a></li>
      <li><a href="#4-تابع-pseudo-huber-loss">4. تابع Pseudo-Huber Loss</a></li>
      <li><a href="#5-تابع-correntropy-loss">5. تابع Correntropy Loss</a></li>
      <li><a href="#6-تابع-epsilon-insensitive-loss">6. تابع Epsilon-Insensitive Loss</a></li>
    </ul>
  </li>
  <li><a href="#استفاده-از-توابع-ضرر-برای-خوشه-بندی">استفاده از توابع ضرر برای خوشه بندی</a>
    <ul>
      <li><a href="#1-راهحلهای-تحلیلی-analytical-solutions">1. راه‌حل‌های تحلیلی</a></li>
      <li><a href="#2-بهینهسازی-عددی-numerical-optimization">2. بهینه‌سازی عددی</a></li>
    </ul>
  </li>
  <li><a href="#توابع-با-راه-حل-محاسباتی">توابع با راه حل محاسباتی</a>
    <ul>
      <li><a href="#تابع-l2-loss-square-loss--mean">تابع L2 Loss (Square Loss) → Mean</a></li>
    </ul>
  </li>
  <li><a href="#پیاده-سازی-خوشه-بندی-با-استفاده-از-توابع-ضررر-مختلف">پیاده سازی خوشه بندی با استفاده از توابع ضررر مختلف</a>
    <ul>
      <li><a href="#لود-کردن-کتابخانه-های-مورد-استفاده-">لود کردن کتابخانه های مورد استفاده</a></li>
      <li><a href="#لود-کردن-مدل-vgg16-برای-استخراج-ویژگی">لود کردن مدل vgg16 برای استخراج ویژگی</a></li>
      <li><a href="#اسخراج-ویژگی-از-مجموعه-داده">اسخراج ویژگی از مجموعه داده</a></li>
      <li><a href="#تعریف-توابع-ضرر-در-کد">تعریف توابع ضرر در کد</a></li>
    </ul>
  </li>
  <li><a href="#الگوریتم-خوشه-بندی">الگوریتم خوشه بندی</a>
    <ul>
      <li><a href="#پیاده-سازی">پیاده سازی</a></li>
    </ul>
  </li>
  <li><a href="#نتایج-خوشه-بندی">نتایج خوشه بندی</a>
    <ul>
      <li><a href="#تابع-l2">تابع L2</a></li>
      <li><a href="#تابع-l1">تابع L1</a></li>
      <li><a href="#تابع-huber">تابع Huber</a></li>
      <li><a href="#تابع-pseudo-huber">تابع Pseudo-Huber</a></li>
      <li><a href="#تابع-correntropy">تابع Correntropy</a></li>
      <li><a href="#تابع-epsilon-insensitive">تابع Epsilon-Insensitive</a></li>
    </ul>
  </li>
  <li><a href="#منابع">منابع</a></li>
</ul>

---

</div>

## مقدمه

در این پروژه، به بررسی و پیاده‌سازی روش‌های مختلف خوشه‌بندی تصاویر با استفاده از یادگیری عمیق می‌پردازیم. هدف اصلی این است که تصاویر را بر اساس محتوای بصری‌شان به گروه‌های معنادار تقسیم کنیم. برای این منظور، ابتدا از شبکه عصبی پیش‌آموزش‌دیده VGG16 برای استخراج ویژگی‌های تصاویر استفاده می‌کنیم. سپس با بکارگیری توابع ضرر مختلف (از جمله L1، L2، Huber، Correntropy و ...) و تکنیک‌های بهینه‌سازی عددی، خوشه‌بندی را انجام می‌دهیم.

این پروژه نشان می‌دهد که انتخاب تابع ضرر مناسب چگونه می‌تواند بر نتایج خوشه‌بندی تأثیر بگذارد. همچنین تفاوت بین روش‌های تحلیلی و بهینه‌سازی عددی  را برای یافتن مراکز بهینه خوشه‌ها بررسی می‌کنیم.



## یادگیری بدون نظارت و خوشه‌بندی

یادگیری بدون نظارت به تکنیک‌هایی اطلاق می‌شود که بدون نیاز به داده‌های برچسب‌دار، الگوها و گروه‌بندی‌ها را در داده‌ها کشف می‌کنند. خوشه‌بندی یکی از رایج‌ترین روش‌های یادگیری بدون نظارت است که داده‌ها را به گروه‌هایی (خوشه‌ها) تقسیم می‌کند به گونه‌ای که عناصر درون هر خوشه شباهت بیشتری به یکدیگر نسبت به عناصر خوشه‌های دیگر داشته باشند. با اعمال خوشه‌بندی بر روی ویژگی‌های استخراج‌شده از تصاویر، می‌توانیم به طور خودکار تصاویر را بر اساس محتوای بصری‌شان به گروه‌های معناداری سازماندهی کنیم.

این پروژه الگوریتم‌های خوشه‌بندی تعمیم‌یافته را با استفاده از توابع ضرر مختلف پیاده‌سازی می‌کند که امکان گروه‌بندی انعطاف‌پذیر و مقاوم تصاویر را فراهم می‌آورد. نتایج به‌دست‌آمده بینشی درباره ساختار مجموعه داده تصویری ارائه می‌دهد و قدرت ترکیب استخراج ویژگی عمیق با یادگیری بدون نظارت را نشان می‌دهد.

 

## اهمیت استخراج ویژگی

تصاویر به طور کلی داده‌هایی با ابعاد بالا هستند که معمولاً شامل هزاران یا میلیون‌ها پیکسل می‌باشند. استفاده‌ی مستقیم از این مقادیر پیکسل برای وظایف یادگیری ماشین، ناکارآمد و به‌ندرت مؤثر است، زیرا این مقادیر الگوها یا محتوای معنایی زیرین تصویر را به‌خوبی نمایش نمی‌دهند.
استخراج ویژگی، تصاویر خام را به نمایش‌های فشرده و آگاهانه‌ای تبدیل می‌کند که اطلاعات بصری اساسی را خلاصه می‌سازند. این کار باعث می‌شود وظایف بعدی مانند طبقه‌بندی، خوشه‌بندی و بازیابی، مقاوم‌تر و از نظر محاسباتی امکان‌پذیرتر شوند.

## شبکه های عصبی CNN و مدل VGG16

شبکه‌های عصبی کانولوشنی یا به اختصار (CNN) یکی از انواع مدل‌های یادگیری عمیق هستند که به‌طور خاص برای داده‌های تصویری طراحی شده‌اند. این شبکه‌ها از لایه‌های کانولوشنی برای یادگیری خودکار ویژگی‌های سلسله‌مراتبی )بزرگ به کوچک) استفاده می‌کنند. از لبه‌ها و الگوهای ساده گرفته تا اشکال و اجسام پیچیده‌تر. VGG16 یک معماری معروف از نوع CNN است که به دلیل سادگی و کارایی بالا شناخته می‌شود. این مدل از ۱۶ لایه با وزن‌های قابل یادگیری تشکیل شده و از فیلترهای کانولوشنی کوچک (۳×۳) استفاده می‌کند. VGG16 بر روی مجموعه‌داده‌ی بزرگ ImageNet که شامل میلیون ها تصویر روزمره از پیش آموزش داده شده است و به همین دلیل قادر است ویژگی‌های غنی و قابل تعمیم را از تصاویر جدید استخراج کند.

در این پروژه، از VGG16 به‌عنوان استخراج‌کننده‌ی ویژگی‌ها (Feature Extractor) استفاده می‌شود. به‌جای استفاده از مدل برای طبقه‌بندی، خروجی لایه‌های کانولوشنی آن برای به‌دست‌آوردن بردار ویژگی هر تصویر به کار گرفته می‌شود. این بردارها مهم‌ترین ویژگی‌های بصری تصاویر را در بر می‌گیرند و مبنایی برای خوشه‌بندی داده‌ها فراهم می‌کنند.

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/fx-image2.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
استفاده از شبکه عصبی vgg16 برای استخراج ویژگی

</div>

<br>
<br>
برای درک بهتر ویژگی ها میتوان تعداد از ویژگی های استخراج شده از تصاویر را مشاهده کرد

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/org_ant.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
تصویر نمونه مورد استفاده برای استخراج ویژگی
</div>

<br>
<br>
<br>

در تصویر زیر میتوان تعدادی از ویژگی های استخراج شده را مشاهده کرد :

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/layer_1_overview.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
</div>
<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/layer_1_overview.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
نمونه از ویژگی های استخراج شده از شبکه عصبی CNN</div>

<br>

```python
import torch
import torchvision.models as models
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#  Load VGG16
vgg = models.vgg16(weights=models.VGG16_Weights.IMAGENET1K_V1).features.eval()
layers_to_tap = [1,2,3, 8, 15, 22, 29] 
features = {}
def save_activation(name):
    def hook(module, inp, out):
        features[name] = out.detach().cpu()
    return hook
for idx in layers_to_tap:
    vgg[idx].register_forward_hook(save_activation(f"layer_{idx}"))
#  Preprocess
tfms = T.Compose([
    T.Resize(256),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]),
])
img_path = ""  
img = Image.open(img_path).convert("RGB")
plt.imshow(img)
plt.axis(False)
plt.show()
x = tfms(img).unsqueeze(0)
with torch.no_grad():
    vgg(x)
def normalize_channel(arr):
    arr = arr - arr.mean()
    arr = arr / (arr.std() + 1e-5)
    arr = arr * 64 + 128
    return np.clip(arr, 0, 255).astype("uint8")
channels_to_show = 8
for name, fmap in features.items():
    #[1, C, H, W]
    fmap = fmap[0]
    n = min(channels_to_show, fmap.shape[0])
    cols = 4
    rows = int(np.ceil(n / cols))
    plt.figure(figsize=(cols * 4.2, rows * 4.2))
    plt.suptitle(f"{name} — feature maps", y=0.98, fontsize=12)
    for i in range(n):
        ax = plt.subplot(rows, cols, i + 1)
        chan = fmap[i].cpu().numpy()
        norm_img = normalize_channel(chan)
        ax.imshow(norm_img, cmap="viridis")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"ch {i}", fontsize=8)
    plt.tight_layout()
    plt.show()
    plt.close()
```

---

در این پروژه هدف ما اعمال روش های مختلف بهینه سازی و توابع ضرر مختلف برای خوشه بندی تصاویر است

به عنوان نمونه در این مثال ، از تعداد ای تصاویر حیوانات استفاده میکنیم و سعی میکنیم با استفاده از ویژگی های استخراج شده از آن ها ، خوشه بندی را انجام دهیم.

در شکل زیر چند نمونه از تصاویر دیتاست را میتوان مشاهده کرد :

<div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap;">
    <img src="/assets/patterneffort/ImageCluster/data_sample (3).jpg" alt="IPS1" style="width: 24%; height: auto; object-fit: contain;">
    <img src="/assets/patterneffort/ImageCluster/data_sample (1).jpg" alt="IPS1" style="width: 24%; height: auto; object-fit: contain;">
    <img src="/assets/patterneffort/ImageCluster/data_sample (2).jpg" alt="IPS1" style="width: 24%; height: auto; object-fit: contain;">
    <img src="/assets/patterneffort/ImageCluster/data_sample (4).jpg" alt="IPS1" style="width: 24%; height: auto; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
نمونه ای از تصاویر در مجموعه داده ها
</div>

# توابع ضرر

در این قسمت به معرفی توابع ضرری که برای خوشه بندی در این تمرین استفاده میکنیم خواهیم پرداخت :

## 1. تابع ضرر  Square Loss / L2

**نظریه:** ضرر مربعی مجموع مربع فاصله‌ها را کمینه می‌کند. این رایج‌ترین تابع ضرر (در k-means استفاده می‌شود) است اما به دلیل مربع شدن خطاهای بزرگ، به داده‌های پرت بسیار حساس است.

**فرمول:**
<div dir="ltr">


$$L(x, \mu) = \sum (x - \mu)^2$$

</div>

**نمادگذاری:**

- $x$‌: بردار داده (نقطه داده)
- $\mu$: مرکز خوشه (نماینده)
- $(x - \mu)^2$: مربع فاصله اقلیدسی

---

## 2. تابع ضرر  Absolute Loss / L1

**نظریه:** ضرر مطلق مجموع فاصله‌های مطلق را کمینه می‌کند. نسبت به ضرر مربعی به داده‌های پرت مقاوم‌تر است چون خطاها به صورت خطی رشد می‌کنند نه درجه دوم.

**فرمول:**

<div dir="ltr">

$$L(x, \mu) = \sum |x - \mu|$$

</div>

**نمادگذاری:**

- $x$: بردار داده
- $\mu$: مرکز خوشه
- $|x - \mu|$: فاصله منهتن (Manhattan distance)

## 3. تابع Huber Loss

**نظریه:** ضرر هوبر بهترین‌های دو دنیا را ترکیب می‌کند - برای خطاهای کوچک درجه دوم (مثل L2) و برای خطاهای بزرگ خطی (مثل L1) است. این باعث می‌شود در برابر داده‌های پرت مقاوم باشد و در عین حال در نزدیکی مینیمم نرم باشد.

**فرمول:**

<div dir="ltr">

$$
L(x, \mu) = \begin{cases}
\frac{1}{2}(x-\mu)^2 & \text{if } |x-\mu| \leq \delta \\
\delta(|x-\mu| - \frac{\delta}{2}) & \text{otherwise}
\end{cases}
$$
</div>

**نمادگذاری و پارامترها:**

- $x$: بردار داده
- $\mu$: مرکز خوشه
- $\delta$: پارامتر آستانه که نقطه انتقال بین رفتار درجه دوم و خطی را کنترل می‌کند
  - برای $|x-\mu| \leq \delta$: رفتار درجه دوم (مشابه L2)
  - برای $|x-\mu| > \delta$: رفتار خطی (مشابه L1)

---

## 4. تابع Pseudo-Huber Loss

**نظریه:** تقریب نرم ضرر هوبر که در همه جا مشتق‌پذیر است. رفتار مشابه ضرر هوبر دارد اما بدون انتقال ناگهانی.

**فرمول:**



<div dir="ltr">

$$
L(x, \mu) = \sum \delta^2 \left(\sqrt{1 + \left(\frac{x-\mu}{\delta}\right)^2} - 1\right)
$$

</div>


**نمادگذاری و پارامترها:**

- $x$: بردار داده
- $\mu$: مرکز خوشه
- $\delta$: پارامتر نرمی که درجه تقریب را کنترل می‌کند
  - مقادیر کوچک $\delta$: رفتار نزدیک به L1
  - مقادیر بزرگ $\delta$: رفتار نزدیک به L2

---

## 5. تابع (Correntropy Loss)

**نظریه:** بر اساس کرنل گاوسی از نظریه اطلاعات. شباهت را اندازه‌گیری می‌کند نه فاصله و در برابر داده‌های پرت بسیار مقاوم است. نقاط دور از مرکز تقریباً هیچ سهمی در ضرر ندارند.

**فرمول:**
<div dir="ltr">

$$L(x, \mu) = 1 - \exp\left(-\frac{\sum(x-\mu)^2}{2\sigma^2}\right)$$

</div>

**نمادگذاری و پارامترها:**

- $x$: بردار داده
- $\mu$: مرکز خوشه
- $\sigma$: پارامتر عرض کرنل (kernel bandwidth)
  - مقادیر کوچک $\sigma$: حساسیت بیشتر به فاصله‌های کوچک
  - مقادیر بزرگ $\sigma$: تحمل بیشتر نسبت به داده‌های پرت

---

## 6. تابع (Epsilon-Insensitive Loss)

**نظریه:** در ماشین‌های بردار پشتیبان (SVM) استفاده می‌شود. این تابع ضرر خطاهای کوچکتر از اپسیلون را نادیده می‌گیرد و فقط نقاط دور از مرکز را جریمه می‌کند. زمانی خوب است که می‌خواهید تغییرات کوچک را نادیده بگیرید.

**فرمول:**

<div dir="ltr">

$$ L(x, \mu) = \max(0, \|x - \mu\| - \epsilon) $$

</div>

**نمادگذاری و پارامترها:**

- $x$: بردار داده
- $\mu$: مرکز خوشه
- $\|x - \mu\|$: نرم اقلیدسی (فاصله)
- $\epsilon$: پارامتر منطقه بی‌حساس
  - برای $\|x - \mu\| \leq \epsilon$: ضرر صفر است
  - برای $\|x - \mu\| > \epsilon$: ضرر به صورت خطی افزایش می‌یابد

---

# استفاده از توابع ضرر برای خوشه بندی

در مسئله‌ی خوشه‌بندی، باید «مرکز» هر خوشه را بیابیم که مجموع زیان‌ها را کمینه کند. بسته به نوع تابع ضرر این کار می‌تواند به یکی از دو روش زیر انجام شود:

---

#### 1. **راه‌حل‌های تحلیلی (Analytical Solutions)**

برخی تابع‌های ضرر فرمول ریاضی مشخصی برای مرکز بهینه دارند:


<div dir="rtl">
به عنوان مثال تابع ضرر L2 را میتوان مستقیم با میانگین حساب کرد
<br>

  

</div>

$ \mu^* = \frac{1}{n}\sum_{i=1}^n x_i $

 

<div dir="rtl">

<div dir="rtl">
به عنوان مثال تابع ضرر L1 را میتوان مستقیم با میانه حساب کرد
<br>

  

</div>   
</div>

$ \mu^* = \text{median}(x_1, x_2, ..., x_n) $
 
---

#### 2. بهینه‌سازی عددی (Numerical Optimization)

بیشتر تابع‌های زیان دیگر (مثل Huber، Correntropy و ...) فرمول بسته‌ای برای $\mu^*$ ندارند،
بنابراین باید از روش‌های عددی برای یافتن مرکز بهینه استفاده کنیم.

---

**نحوه‌ی کار `scipy.optimize.minimize`:**

```python
result = minimize(objective_function, initial_guess, method='BFGS')
```

<div dir="rtl" style="text-align: right;">
- تابع هدف (Objective Function): تابعی که می‌خواهیم کمینه کنیم (مجموع زیان‌ها)  
- حدس اولیه (Initial Guess): نقطهٔ شروع جست‌وجو (معمولاً از میانگین داده‌ها استفاده می‌شود)  
- method='BFGS': الگوریتم مبتنی بر گرادیان که مراحل زیر را طی می‌کند:

1. از حدس اولیه آغاز می‌کند
2. گرادیان (جهت بیشترین کاهش) را محاسبه می‌کند
3. در آن جهت یک گام برمی‌دارد
4. این فرایند را تا همگرایی به حداقل تکرار می‌کند
</div>

#### مقایسه و موازنه (Trade-offs):

<div dir="rtl" style="text-align: right;">
- تحلیلی: محاسبهٔ سریع و دقیق، بدون خطای تقریبی  
- عددی: کندتر، اما تنها گزینهٔ ممکن زمانی که فرمول بسته وجود ندارد
</div>

به عنوان مثال یک نمونه از کارکرد این روش را برای یک تابع ضرر میتوان مشاهده کرد
در ابتدا از یک نقطه تصادفی شروع کرده و به سمت مخالف گرادیان می رویم (‌گرادیان نزولی)
در واقع نقطه انتخاب شده ، نقطه ای با حداقال فاصله با سایر نقاط است.

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/sgd.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
</div>
---

# توابع با راه حل محاسباتی

## تابع L2 Loss (Square Loss) → Mean

یکی از توابع بسیار پرکاربرد مورد استفاده در الگوریتم های مثل k-means

### گام ۱: مشتق‌گیری نسبت به $\mu^*$

<div dir="ltr">

$
\frac{dL}{d\mu} = \frac{d}{d\mu} \sum_{i=1}^{n} (x_i - \mu)^2
$

</div>



با استفاده از قاعده‌ی زنجیره‌ای:

$
\frac{dL}{d\mu}
= \sum_{i=1}^{n} \frac{d}{d\mu}(x_i - \mu)^2
= \sum_{i=1}^{n} 2(x_i - \mu)(-1)$

$\frac{dL}{d\mu} = -2\sum_{i=1}^{n} (x_i - \mu)$

---

### گام ۲: برابر صفر قرار دادن مشتق (شرط لازم برای کمینه)

$-2\sum_{i=1}^{n} (x_i - \mu) = 0$

$\sum_{i=1}^{n} (x_i - \mu) = 0$

---

### گام ۳: حل برای $\mu^*$

$\sum_{i=1}^{n} x_i - \sum_{i=1}^{n} \mu = 0$

$\sum_{i=1}^{n} x_i - n\mu = 0$

$\mu^* = \frac{1}{n}\sum_{i=1}^{n} x_i$

---

# پیاده سازی خوشه بندی با استفاده از توابع ضررر مختلف

## لود کردن کتابخانه های مورد استفاده :

```python
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tqdm import tqdm
```

## لود کردن مدل vgg16 برای استخراج ویژگی

```python

#pre-trained VGG16 model
vgg16 = models.vgg16(pretrained=True)
model = nn.Sequential(*list(vgg16.features.children()))
model.eval()



image preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

## اسخراج ویژگی از مجموعه داده

در این قسمت از عکس های موجود در دیتاست ، استخراج ویژگی انجام می دهیم.

```python
def extract_features(img_path, model, device='cpu'):
    image = Image.open(img_path).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        features = model(input_tensor)

    # Global average pooling to get a 512-dim vector
    global_pooled = torch.mean(features, dim=(2, 3))
    return global_pooled.squeeze().cpu().numpy()


def extract_features_from_folder(folder_path, model, device):
    """
    Extract features from all images in a folder.

    Args:
        folder_path: Path to folder containing images
        model: Pre-trained VGG16 model
        device: Device to run the model on

    Returns:
        features_dict: Dictionary mapping filenames to feature vectors
        image_files: List of image filenames
    """
    features_dict = {}
    image_files = [f for f in os.listdir(folder_path)
                   if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort()

    print(f"Found {len(image_files)} images in '{folder_path}'")

    for file in image_files:
        img_path = os.path.join(folder_path, file)
        print(f"  Extracting features from: {file}")
        features = extract_features(img_path, model, device)
        features_dict[file] = features

    print("✅ Feature extraction complete!")
    return features_dict, image_files


# Extract features from all images
image_folder = "folder name"
features_dict, image_files = extract_features_from_folder(image_folder, model)

# Convert to numpy array for clustering
features_list = list(features_dict.values())
data = np.stack(features_list)

print(f"\n📊 Data shape: {data.shape}")
print(f"   → {data.shape[0]} images, each with {data.shape[1]} features")
```

## تعریف توابع ضرر در کد

در این قسمت یک تابع کلی تعریف میکنیم که به عنوان ورودی اسم تابع را گرفته و فرمول آن را بر می گردانیم

```python

def get_loss_func(loss_type, params={}):
    """
    Returns a loss function based on the specified type.

    Args:
        loss_type: Name of the loss function
        params: Dictionary of parameters for the loss function

    Returns:
        Loss function that takes (x, mu) and returns a scalar
    """

    if loss_type == 'square':
       
        def loss(x, mu):
            return np.sum((x - mu)**2)
        return loss

    elif loss_type == 'absolute':
     
        def loss(x, mu):
            return np.sum(np.abs(x - mu))
        return loss

    elif loss_type == 'huber':
      
        delta = params.get('delta', 1.0)
        def loss(x, mu):
            res = np.abs(x - mu)
            return np.sum(np.where(res <= delta,
                                   0.5 * res**2,
                                   delta * (res - 0.5 * delta)))
        return loss

    elif loss_type == 'pseudo_huber':
        
        delta = params.get('delta', 1.0)
        def loss(x, mu):
            res = x - mu
            return np.sum(delta**2 * (np.sqrt(1 + (res / delta)**2) - 1))
        return loss

    elif loss_type == 'correntropy':
        
        sigma = params.get('sigma', 1.0)
        def loss(x, mu):
            d2 = np.sum((x - mu)**2)
            return 1 - np.exp(-d2 / (2 * sigma**2))
        return loss

    elif loss_type == 'epsilon_insensitive':
        
        epsilon = params.get('epsilon', 1.0)
        def loss(x, mu):
            d = np.linalg.norm(x - mu)
            return max(0, d - epsilon)
        return loss

```

# الگوریتم خوشه بندی

توضیح کلی راجب خوشه بندی .....

## پیاده سازی

```python

def update_center(points, loss_type, params):
    if len(points) == 0:
        return np.zeros(points.shape[1])
    if loss_type == 'square':
        return np.mean(points, axis=0)
    elif loss_type == 'absolute':
        return np.median(points, axis=0)
    else:
        def objective(mu):
            loss_func = get_loss_func(loss_type, params)
            total_loss = sum(loss_func(x, mu) for x in points)
            return total_loss
        
        initial_guess = np.mean(points, axis=0)
        result = minimize(
            objective,              
            initial_guess,          
            method='BFGS',          
            options={'maxiter': 20} 
        )
        return result.x
```

```python

def generalized_clustering(data, k, loss_type, params={}, max_iter=3, tol=1e-4):
    n, d = data.shape
    centers = data[np.random.choice(n, k, replace=False)]
    prev_shift = np.inf
    for iter in range(max_iter):
        # Assign each point to nearest center
        dists = np.array([[get_loss_func(loss_type, params)(data[i], centers[j])
                          for j in range(k)]
                         for i in range(n)])
        labels = np.argmin(dists, axis=1)

        #  Update centers
        new_centers = np.zeros((k, d))
        for j in tqdm(range(k), desc=f"Updating centers (iter {iter+1})"):
            points_j = data[labels == j]
            if len(points_j) > 0:
                new_centers[j] = update_center(points_j, loss_type, params)
        # Check convergence
        shift = np.sum(np.linalg.norm(new_centers - centers, axis=1))
        centers = new_centers
        if shift < tol or abs(shift - prev_shift) < 1e-6:
            print(f"  Converged after {iter+1} iterations")
            break
        prev_shift = shift
    return centers, labels

```

```python
def find_closest_image(center, points, indices, loss_func):
    min_dist = np.inf
    closest_idx = -1
    for idx, p in zip(indices, points):
        dist = loss_func(p, center)
        if dist < min_dist:
            min_dist = dist
            closest_idx = idx
    return closest_idx


def plot_representatives(loss_type, centers, labels, image_files, folder_path, loss_func):
    fig, axs = plt.subplots(1, len(centers), figsize=(5 * len(centers), 5))
    fig.suptitle(f'Representative Images - {loss_type.upper()} Loss', fontsize=16, fontweight='bold')
    for j, center in enumerate(centers):
        # Find all images in this cluster
        cluster_indices = [i for i in range(len(labels)) if labels[i] == j]
        cluster_points = data[cluster_indices]
        if len(cluster_points) > 0:
            # Find the image closest to the center
            closest_i = find_closest_image(center, cluster_points, cluster_indices, loss_func)
            img_file = image_files[closest_i]
            img_path = os.path.join(folder_path, img_file)
            img = mpimg.imread(img_path)
            if len(centers) == 1:
                axs.imshow(img)
                axs.set_title(f'Representative {j+1}\n{img_file}', fontsize=12)
                axs.axis('off')
            else:
                axs[j].imshow(img)
                axs[j].set_title(f'Representative {j+1}\n{img_file}', fontsize=12)
                axs[j].axis('off')
    plt.tight_layout()
    plt.show()

```

# نتایج خوشه بندی

### تابع L2

```python

loss_type = 'square'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)



loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/SQUARE loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر L2 و نمایش 3 مرکز خوشه برتر
</div>
<!--  -->

### تابع L1

```python

loss_type = 'absolute'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)



loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/ABSOLUTE loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر l1 و نمایش 3 مرکز خوشه برتر
</div>
<!--  -->
<!--  -->

### تابع Huber

```python

loss_type = 'huber'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)



loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/HUBER loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر huber و نمایش 3 مرکز خوشه برتر
</div>

### تابع Pseudo-Huber

```python

loss_type = 'pseudo-huber'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)


loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/PSEUDO_HUBER loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر pseudo-huber و نمایش 3 مرکز خوشه برتر
</div>

### تابع Correntropy

```python

loss_type = 'correntropy'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)



loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/CORRENTROPY loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر Correntropy و نمایش 3 مرکز خوشه برتر
</div>

### تابع Epsilon-Insensitive

```python

loss_type = 'epsilon_insensitive'
params = params_dict[loss_type]

z=(f"🔄 Running clustering with {loss_type.upper()} loss...")
centers, labels = generalized_clustering(data, k, loss_type, params)



loss_func = get_loss_func(loss_type, params)
plot_representatives(loss_type, centers, labels, image_files, image_folder, loss_func,z)

```

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/patterneffort/ImageCluster/EPSILON_INSENSITIVE loss.png" alt="IPS1" style="width: 50%; height: 50%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
حاصل خوشه بندی با تابع ضرر huber و نمایش 3 مرکز خوشه برتر
</div>

# منابع 

- http://cnnlocalization.csail.mit.edu/
- https://docs.pytorch.org/vision/main/models.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
- https://arxiv.org/abs/1409.1556