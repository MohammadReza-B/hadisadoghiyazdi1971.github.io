---
layout: persian  # یا single با کلاس rtl-layout
classes: wide rtl-layout
dir: rtl
title: "سیستم تعمیر-آگاه"
permalink: /presentation/MaintenanceAware/
author_profile: true
sidebar:
  nav: "presentaton"
header:
  overlay_image: "/assets/images/background.jpg"
  overlay_filter: 0.3
  overlay_color: "#5e616c"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
---
 
## تعمیر آگاه چیست

با افزایش روزافزون پیچیدگی و مقیاس شبکه‌های برق مدرن، تأمین انرژی الکتریکی قابل اعتماد و پایدار به یکی از چالش‌های اصلی صنعت برق تبدیل شده است. در این میان، سیستم‌های توزیع به عنوان حلقه واسط بین تولید و مصرف، نقشی حیاتی ایفا می‌کنند و قابلیت اطمینان آن‌ها مستقیماً به کیفیت و به‌موقع بودن فعالیت‌های نگهداری و تعمیرات وابسته است. به این منظور نیاز به **سیستم های تعمیر آگاه** است.

این سیستم دایما خودش را پایش می کند و با ابزار مختلف از وضعیت خود با خبر می شود سپس توسط ابزار هوشمند برای دوقلوی دیجیتالی که از خود بوجود اورده به آگاهی دادن برای تعمیرات پیش بینانه اقدام می کند. 

<a href="https://www.aurecongroup.com/projects/national-grid-uk" style="text-decoration:none; color:green;" target="_blank"><strong>پلتفرم یکپارچه نگهداری و تعمیرات پیش‌بینانه (Predictive Maintenance)</strong></a>   برای دارایی‌های شبکه توزیع برق با استفاده از هوش مصنوعی، اینترنت اشیاء (IoT) و فناوری دوقلوی دیجیتال (Digital Twin) این پروژه یک گام فراتر از نگهداری و تعمیرات سنتی است. به جای تعمیرات بر اساس یک برنامه زمانی ثابت (مثلاً هر ۶ ماه یکبار)، این سیستم بر اساس وضعیت واقعی و لحظه‌ای تجهیزات، زمان و نوع نیاز به تعمیر را پیش‌بینی می‌کند. این 
<a href="https://www.aurecongroup.com/-/media/files/downloads-library/thought-leadership/aurecon-our-digital-futures-your-digital-decisions-report.pdf" style="text-decoration:none; color:green;" target="_blank"><strong>گزارش</strong></a>   را هم ببینید. 

چنانچه دوقلوی دیجیتالی برای منظور تعمیر و نگه داری مشابه دوقلوی  دیجیتال شبکه برق ایران داشته باشیم طبعا پیش بینی و حتی مکانیز "چی می شد اگر" نیز مقدور می شد. 

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/Presentationimages/DT/whatif_Tehran_mashhad.jpg" alt="RAG1" style="width: 80%; height: 80%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
دوقلوی دیجیتال شبکه برق ملی ایران</div>


## اجزای اصلی پروژه پیش بینانه:

### لایه جمع‌آوری داده (Data Layer - IoT):
**سنسورهای هوشمند:** نصب سنسورهای اینترنت اشیاء (IoT) بر روی دارایی‌های حیاتی شبکه توزیع مانند ترانسفورماتورها، کلیدهای قدرت، فیدرها و پایه‌ها. این سنسورها داده‌هایی مانند دما، رطوبت، ارتعاشات، جریان بار و گازهای محلول در روغن ترانس (DGA) را به صورت لحظه‌ای ارسال می‌کنند.
پهپادها و ربات‌ها: استفاده از پهپادهای مجهز به دوربین‌های با وضوح بالا، حرارتی (Thermal) و LiDAR برای بازرسی منظم و خودکار خطوط، شناسایی خوردگی، شکستگی عایق‌ها و رشد بیش از حد گیاهان در نزدیکی خطوط (Vegetation Management).
**داده‌های هواشناسی:** یکپارچه‌سازی داده‌های پیش‌بینی آب و هوا (طوفان، رعد و برق، یخبندان) برای ارزیابی ریسک‌های احتمالی.
### لایه پردازش و مدل‌سازی (Processing & Modeling Layer - Digital Twin):
**ایجاد دوقلوی دیجیتال**: ساخت یک نسخه مجازی و پویا از کل شبکه توزیع (یا بخشی از آن). این مدل دیجیتال، تمام داده‌های دریافتی از سنسورها و پهپادها را در خود منعکس می‌کند. برای توضیح بیشتر این متن را مطالعه کنید 

<a href="https://hadisadoghiyazdi1971.github.io/presentation/HumanDT/" style="text-decoration:none; color:red;" target="_blank"><strong>کلیک کنید</strong></a>

**شبیه‌سازی**: با استفاده از این دوقلوی دیجیتال، مدیران شبکه می‌توان سناریوهای مختلف را شبیه‌سازی کنند. برای مثال: "اگر یک طوفان شدید در منطقه X رخ دهد، کدام بخش از شبکه آسیب‌پذیرترین خواهد بود؟" یا "اثر خروج یک ترانسفورماتور مشخص بر شبکه چیست؟".
### لایه تحلیل و هوش مصنوعی (AI & Analytics Layer):
**الگوریتم‌های یادگیری ماشین (Machine Learning)**: این مغز متفکر سیستم است. الگوریتم‌های هوش مصنوعی، داده‌های تاریخی و لحظه‌ای را تحلیل می‌کنند تا الگوهای نامعقول و نشانه‌های اولیه خرابی را شناسایی کنند.
**پیش‌بینی خرابی:** سیستم می‌تواند با دقت بالایی پیش‌بینی کند که کدام ترانسفورماتور در ۳ ماه آینده دچار نقص فنی خواهد شد یا کدام بخش از عایق‌ها در حال تخریب هستند. این پیش‌بینی‌ها با اولویت‌بندی (مثلاً از بحرانی تا کم‌اهمیت) به تیم نگهداری اعلام می‌شود.
## لایه اجرا و مدیریت (Execution & Management Layer):
**ایجاد خودکار دستور کار (Work Order)**: سیستم به صورت خودکار یک دستور کار دقیق برای تیم تعمیرات صادر می‌کند. این دستور کار شامل مشخصات دقیق مشکل، مکان دارایی روی نقشه، و تاریخ پیشنهادی برای تعمیر است.
**بهینه‌سازی مسیر**: سیستم با توجه به موقعیت تیم‌های تعمیراتی و ترافیک، بهینه‌ترین مسیر برای رسیدن به محل را پیشنهاد می‌دهد.
راهنمایی تعمیرات با واقعیت افزوده (AR): تکنسین‌های تعمیرات می‌توانند با استفاده از عینک‌های هوشمند یا تبلت، اطلاعات دیجیتال (مانند دیاگرام‌ها، دستورالعمل‌ها و داده‌های سنسور) را روی دنیای واقعی و روی خود تجهیزات مشاهده کنند.

## مثال‌های واقعی و پروژه‌های در دست اجرا در دنیا:
این مفهوم دیگر یک ایده تئوریک نیست و شرکت‌های برق بزرگ در سراسر جهان در حال پیاده‌سازی آن هستند:

<a href="https://www.nationalgrid.com/electricity-transmission/national-grid-play-key-role-new-drone-infrastructure-inspection-policy" style="text-decoration:none; color:green;" target="_blank"><strong>شرکت National Grid (بریتانیا و آمریکا):
 </strong></a>

روش کار برای بازرسی خطوط برق، بهره‌گیری از فناوری پهپادهای مجهز به دوربین‌های با وضوح بالا است که قابلیت پرواز «فراتر از خط دید» را دارند. این رویکرد نوین، که با مشارکت شرکت‌هایی مانند National Grid و همکاری مراجع قانونی مانند سازمان هوانوردی بریتانیا توسعه یافته، امکان بازرسی ایمن، سریع و دقیق دکل‌ها و خطوط انتقال نیرو را از راه دور و حتی از یک اتاق کنترل مرکزی فراهم می‌کند. این روش نه تنها هزینه‌ها و زمان عملیات را کاهش می‌دهد، بلکه با حذف نیاز به صعود فیزیکی کارکنان به دکل‌ها برای بازدید بصری، سطح ایمنی نیروی متخصص را به طور چشمگیری افزایش می‌دهد و آن‌ها را برای تمرکز بر وظایف تخصصی‌تر و تعمیرات آماده می‌سازد.

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/Presentationimages/PowerSectorRepairingOptimize/powerLineSurveillance.jpg" alt="RAG1" style="width: 80%; height: 80%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
پایش خطوط با پهپاد</div>


این شرکت به طور گسترده از پهپادها و تحلیل داده‌های مبتنی بر هوش مصنوعی برای مدیریت پوشش گیاهی (Vegetation Management) استفاده می‌کند. پهپادها با اسکن LiDAR، نقشه سه‌بعدی دقیقی از خطوط و درختان اطراف ایجاد می‌کنند و هوش مصنوعی خطر برخورد درختان با خطوط را در آینده نزدیک پیش‌بینی می‌کند. این کار از قطعی‌های ناشی از این علت که یکی از دلایل اصلی خاموشی‌هاست، جلوگیری می‌کند.

### نمونه کار آزمایشگاه الگو دانشگاه فردوسی مشهد

پایش بر اساس تصاویر ماهواره 


<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/Presentationimages/PowerSectorRepairingOptimize/photo_2025-12-14_12-36-22.jpg" alt="powerline1" style="width: 80%; height: 80%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
پایش خطوط با تصاویر ماهواره</div>

مسیرهای تصاویر اخذ شده در شکل زیر آمده است 

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
    <img src="/assets/Presentationimages/PowerSectorRepairingOptimize/photo_2025-12-14_12-35-52.jpg" alt="powerline1" style="width: 80%; height: 80%; object-fit: contain;">
</div>
<div class="caption" style="text-align: center; margin-top: 8px;">
 دکلهای فشار قوی  اخذ شده </div>

