---
layout: persian
classes: wide rtl-layout
dir: rtl
title: "رسم شماتیک مدار"
permalink: /teaching/circuiteffort/Circuit_Schematic_Drawing_Project/
author-profile: true

---


# رسم شماتیک مدار 

<div style="display: flex; justify-content: right; gap: 10px;">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/MyPhoto.jpg" alt="IPS1" style="width: 20%; height: 20%; object-fit:cover; ">
</div>

<div class="caption" style="text-align: right; margin-top: 8px;">
    _figure1:Hossein Jahanbanifar_
</div>



## فهرست مطالب

1-  [اطلاعات نویسنده](#اطلاعات-نویسنده)

2-  [مقدمه ](#مقدمه)

3-  [انواع نرم افزار ها برای رسم شماتیک](#انواع-نرم-افزار-ها-برای-رسم-شماتیک)

4-  [نرم افزار پروتئوس](#نرم-افزار-proteus-design-suite)

5-  [نرم افزار آلتیوم دیزاینر](#نرم-افزار-altium-designer)

6-  [نرم افزار اورکد](#نرم-افزار-orcad-cadence)

7-  [نرم افزار کیکد](#نرم-افزار-kicad)

8-  [نرم افزار فریتزینگ](#نرم-افزار-fritzing)

9-  [شرح محیط طراحی شماتیک](#شرح-محیط-طراحی-شماتیک)

10- [نحوه طراحی شماتیک مدارهای الکتریکی](#نحوه-طراحی-شماتیک-مدارهای-الکتریکی)

11- [نتیجه گیری](#نتیجه-گیری)

12- [منابع](#منابع)


## اطلاعات نویسنده
**نام :**  حسین جهانبانی فر

**وابستگی:**  گروه مهندسی کامپیوتر، دانشگاه فردوسی مشهد

**تماس:**  hosseinjahanbanifar@gmail.com



## مقدمه

در حوزه مهندسی برق و الکترونیک، ترسیم شماتیک مدارها یکی از مراحل بسیار مهم در طراحی و پیاده‌سازی سیستم‌های الکتریکی محسوب می‌شود. شماتیک مدار، نمایش گرافیکی اجزای یک مدار به همراه اتصالات آن‌ها است که با استفاده از نمادهای استاندارد، روابط الکتریکی را به صورت دقیق و قابل فهم بیان می‌کند. این مرحله نه تنها برای مستندسازی پروژه‌های مهندسی ضروری است، بلکه به مهندسان و تکنسین‌ها کمک می‌کند تا پیش از ساخت  اجزای فیزیکی مدار، منطق عملکرد و ایرادات احتمالی را شناسایی کنند.

هدف این پروژه، آشنایی با نرم‌افزارهای استاندارد ترسیم شماتیک (مانند Proteus، Altium Designer، OrCAD و KiCad) و کسب مهارت در استفاده صحیح از ابزارهای آن‌ها برای طراحی مدارهای الکترونیکی است. 

در نهایت در طول پروژه یکی از نرم افزاری های معرفی شده برای رسم را انتخاب کرده و با محیط کاری آن و شیوه رسم اصولی یک مدار الکتریکی آشنا خواهیم شد.

## انواع نرم افزار ها برای رسم شماتیک



در حوزه طراحی مدارهای الکتریکی، انتخاب نرم‌افزار مناسب نقش مهمی در کیفیت و سرعت کار ایفا می‌کند. چهار نرم‌افزار اصلی که در این زمینه بیشترین استفاده را دارند، شامل Proteus Design Suite، Altium Designer، OrCAD (Cadence) و KiCad هستند.

در ادامه، این نرم‌افزارها براساس شاخص‌هایی همچون کاربرپسندی محیط نرم‌افزار، قدرت و دقت کتابخانه قطعات، توانایی شبیه‌سازی مدار، قابلیت طراحی PCB، و دسترس‌پذیری مورد بررسی قرار می‌گیرند.


### نرم افزار Proteus Design Suite

پروتئوس (Proteus Design Suite) محصول شرکت Labcenter Electronics است که نخستین نسخهٔ آن در دههٔ ۱۹۹۰ عرضه شد. این نرم‌افزار ترکیبی از طراحی شماتیک، شبیه‌سازی مدار و طراحی PCB را در محیطی یکپارچه ارائه می‌دهد. محیط کاربری آن گرافیکی و نسبتاً کاربرپسند است؛ منوها و پنل‌ها به گونه‌ای چیده شده‌اند که دسترسی سریع به ابزارها را فراهم می کنند. کتابخانه قطعات آن بسیار گسترده و دقیق است و شامل مدل‌های شبیه‌سازی برای میکروکنترلرها و آی‌سی‌های مختلف می‌شود. قدرت شبیه‌سازی پروتئوس در اجرای کدهای واقعی میکروکنترلرها بر روی مدار و مشاهدهٔ رفتار فیزیکی-منطقی بسیار مورد توجه واقع شده. طراحی PCB نیز با ابزارهای داخلی و معیارهای صنعتی انجام می‌شود. این نرم‌افزار تجاری است و نسخه کامل آن نیاز به لایسنس دارد، ولی نسخه آزمایشی محدود آن نیز موجود است.

### نرم افزار Altium Designer
التیوم دیزاینر محصول شرکت Altium Limited است که نخستین بار به‌عنوان Protel در دههٔ ۱۹۸۰ عرضه شد و بعدها نام آن تغییر یافت. این نرم‌افزار یکی از پیشرفته‌ترین ابزارهای موجود برای طراحی شماتیک و PCB است که به‌طور ویژه در صنایع هوافضا، مخابرات و تجهیزات پیشرفته استفاده می‌شود. محیط کاربری آن  کاربرپسند با رابط گرافیکی مدرن و قابلیت شخصی‌سازی است. کتابخانه‌ها دقیق، کامل و شامل مدل‌های سه‌بعدی هستند. شبیه‌سازی مدار به صورت داخلی و همچنین اتصال به ابزارهای خارجی قابل انجام است. قابلیت طراحی PCB با پشتیبانی ، لایه‌های متعدد و مدل‌سازی سه‌بعدی در آن بسیار پیشرفته است. نرم‌افزار تجاری با مجوز سالیانه عرضه می‌شود


### نرم افزار OrCAD (Cadence)
اورکد (OrCAD) محصول شرکت Cadence Design Systems است که از دههٔ ۱۹۸۰ توسعه می‌یابد و برای طراحی شماتیک، شبیه‌سازی و PCB در سطح حرفه‌ای کاربرد دارد. محیط کاربری آن بسیار قدرتمند ولی بیشتر مناسب کاربران حرفه‌ای و تیم‌های مهندسی است، بنابراین نسبت به نرم‌افزارهای آموزشی پیچیده‌تر به نظر می‌رسد. کتابخانه‌ها دقیق و گسترده‌اند و استانداردهای پیشرفتهٔ صنعتی را پوشش می‌دهند. شبیه‌سازی مدارها با دقت بالا و امکانات تحلیل سیگنال و رفتار گذرا انجام می‌شود. طراحی PCB در آن مطابق نیازهای صنعتی و چندلایه قابل انجام است. نرم‌افزار تجاری بوده و نیاز به خرید مجوز دارد.

### نرم افزار KiCad
کی‌کد (KiCad) نرم‌افزار متن‌باز و رایگان است که از سال ۱۹۹۲ توسعه یافته و اکنون تحت مدیریت تیم بین‌المللی و حمایت CERN عرضه می‌شود. حوزهٔ اصلی استفادهٔ آن طراحی شماتیک و PCB برای پروژه‌های متن‌باز، دانشگاهی و تجاری است. محیط کاربری آن با وجود رایگان بودن، مدرن و کاربرپسند است و پنل‌های طراحی، کتابخانه قطعات و نمایش سه‌بعدی برد را به‌طور یکپارچه ارائه می‌دهد. کتابخانه‌ها دقیق و قابل توسعه هستند و کاربران می‌توانند آن‌ها را شخصی‌سازی یا کتابخانه‌های خارجی اضافه کنند. شبیه‌سازی مدار به‌طور کامل داخلی نیست، ولی امکان اتصال به ابزارهای شبیه‌ساز خارجی مثل SPICE وجود دارد. ابزار طراحی PCB کاملاً حرفه‌ای با پشتیبانی از لایه‌های متعدد و استانداردهای صنعتی ارائه شده است.

### نرم افزار Fritzing

فرتیزینگ یک نرم‌افزار رایگان و متن‌باز است که از سال ۲۰۰۹ برای آموزش و طراحی نمونه‌های اولیه عرضه شده است. تمرکز آن بر نمایش شماتیک، بردبرد و PCB در قالب گرافیکی ساده است. محیط کاربری آن کاملاً کاربرپسند و مناسب مبتدیان است؛ ابزارها و کتابخانه‌ها ساده ولی دقیق برای قطعات رایج هستند. شبیه‌سازی واقعی ندارد و بیشتر نمایش مدار و طرح‌برد است. طراحی PCB قابل انجام است ولی برای کاربردهای صنعتی محدودیت دارد

در ادامه نحوه نصب ، فعال سازی و کار با نرم افزار پروتئوس به عنوان یکی از محبوب ترین ابزار های رسم شماتیک مدار را یاد خواهیم گرفت


## نصب و راه اندازی پروتئوس

این نرم افزار هر چند متن باز نیست و مقداری محدودیت دارد ولی بدلیل محبوبیت آن در بین نرم افزارهای طراحی و رسم شماتیک تصمیم گرفتیم که آموزش کار با این نرم افزار را ارائه دهیم.
می توانید از خود سایت مرجع نرم افزار و از این [لینک](https://www.labcenter.com/downloads/) اقدام کنید

روش دیگر و ساده تر برای دانلود نسخه pro نرم افزار ، مراجعه به سایت geeksforgeeks می باشد که لینک دانلود این پروتئوس رو در اختیار کاربران قرار داده است که از این [لینک](https://www.geeksforgeeks.org/installation-guide/how-to-download-and-install-proteus-software-on-windows/) قابل دسترسی است.
و در این پروژه قصد داریم روش نصب و راه اندازی این نرم افزار محبوب را از این سایت به شما آموزش دهیم.

بعد از اینکه به سایت مراجعه کردید بر روی گزینه دانلود که در صفحه قرار داده شده کلیک کنید
منتظر بمانید که پوشه حاوی نرم افزار بطور کامل دانلود شود. 


<div style="display: flex; justify-content: center; gap: 10px; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus-Download-1.jpg" alt="IPS1" style="width: 100%; height: 50%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top:8px; margin-bottom:15px ">
    _figure 2: Download Proteus_
</div>


بعد از اینکه فایل زیپ نرم افزار دانلود شد، ان را در مسیر دلخواه خودمان در سیستم از حالت فشرده خارج می کنیم.


 
<div style="display: flex; justify-content: center; gap: 10px; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus-Extract-2.jpg" alt="IPS1" style="width: 100%; height: 650px; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure3:Extrant Proteus_
</div>


طبق تصویر زیر وارد پوشه میشویم و با کلیک بر روی فایل .exe نرم افزار اقدام به نصب آن میکنیم


<div style="display: flex; justify-content: center; gap: 10px; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus-Extract-3.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure4 : Extract proteus2_
</div>

<div style="display: flex; justify-content: center; gap: 10px; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus4.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 5 : Install Proteus_
</div>


مراحل نصب رو طبق راهنما جلو رفته و در آخر صبر میکنیم که فرایند نصب در مسیر مورد نظر کامل شود. به دلیل سهولت این مرحله از بعضی قسمت های آن عبور میکنیم. این قسمت ابهام و پیچیدگی خاصی ندارد.

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus-8.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 6 : Install Protues 2_
</div>


در نهایت با تکمیل فرایند نصب در مسیر مورد نظر ، روی دکمه Finish کلیک کرده. پروتئوس در سیستم ما نصب شد و حالا میتوانیم وارد آن شویم و از آن استفاده کنیم



<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Proteus9.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 7 : Install Protues 3_
</div>




<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/UUProteus-10.jpg" alt="IPS1" style="width: 100%; height: 450px; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px ">
    _figure 8: Install Protues 4_
</div>


با ورود به نرم افزار تصویر زیر را میبینیم که ابتدا ورود به محیط نرم افزار است.

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/ProtesComplted.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 9 : End of Installaion
</div>.


مثلا از نوار بالا می توانیم بخش های مربوط به ایجاد فایل ، ادیت ، نما، ابزارها، دیزاین، گراف ، کتابخانه قطعات،و ... را مشاهده کرد. برای ساختن پروژه کافی است که مانند زیر روی بخش New Project کلیک کنیم.


<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-15_22-35-39.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 10 : Start Project_
</div>

پنجره New Project Wizard باز می شود. همان طور که مشاهده می شود باید اسمی روی پروژه خود و مسیری در سیستم برای ذخیره آن قرار دهیم

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-15_22-36-29.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 11 : New Project_
</div>

در پنجره باز شده زیر ، یک قالب برای شروع پروژه شماتیک خود انتخاب میکنیم. مثلا طبق موارد نمایش داده شده می توانیم، نوع قالب بندی صفحه رو بصورت افقی یا Landscape قرار دهیم. بصورت عمودی یا portrait قرار دهیم. یا در آخر یک قالب آماده با تنظیمات نمونه سیستم بسازیم. حالت Sample Design. پروژه را با حالت پیش فرض سیستم یعنی default جلو می بریم.

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-15_22-53-41 (2).jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 12 : Select Template_
</div>

در پنجره بعدی از ما خواسته می شود که برای طراحی چاپی با همان PCB بردی را از میان موارد لیست شده   انتخاب کنیم. ولی چون در این پروژه هدف ما یادگیری طراحی شماتیک است با حالت Don't create PCB layout ادامه می دهیم



<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_07-46-34.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 13 : Select Template for PCB_
</div>


در مرحله آخر از ما خواسته می شود که مشخص کنیم که  پروژه ما شامل کد برنامه نویسی (Firmware) و یا نمودار منطقی برای میکروکنتلر ها (Flowchart) باشد یا خیر. با حالت پیش فرض یعنی No firmware Project ادامه میدهیم.

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_07-46-28.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 14 : Firmware Selection_
</div>

حالا پروژه ما ساخته شده. دقت شود که در این پروژه فقط میخواهیم که حالت شماتیک مدار را بررسی کنیم نه PCB . 

<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_07-46-22.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 15 : Start Project_
</div>


## شرح محیط طراحی شماتیک

در بخش Schematic Capture پروتئوس، محیطی وجود داره که میتوانیم مدار را بصورت شماتیک رسم کنیم. حالا میخواهیم بیشتر با این قسمت آشنا شویم.


نوار بالای این صفحه شامل دکمه ها و آیکون های اصلی است. کاربرد این بخش عبارت است از 
ایجاد، باز و ذخیره کردن پروژه ها(New , Open , Save ) - ابزار های بزرگ نمایی و جابجایی دید در مدار (Zoom In , Zoom Out) ابزارهای اضافه کردن سیم ، لیبل ، منبع تغذیه - گزینه های Simulation برای توقف یا اجرای مدار


<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_07-46-18.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 16 : Main ToolBar_
</div>


بخش دوم نوار ابزار سمت چپ است که که شامل ابزارهای کاربردی طراحی است
قسمت های مهم آن شامل Selection Tool برای انتخاب قطعات. Component Mode برای انتخاب قطعات از کتابخانه text lable mode   برای نوشتن توضیحات کنار قطعات ، Terminals mode برای تعیین ورودی ، خروجی ، زمین  و دیگر ابزار های که بسته به اهداف پیاده سازی ما ممکن است مورد استفاده قرار گیرند.


<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_09-59-19.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 17 : Devices Panel 1_
</div>

بخش سوم پنجره دستگاه هاست که وقتی روی P(pick devices) کلیک میکنیم پنجره ای برای ما باز میشود که اسم قطعات، مدل و مشخصات ان ها نمایش داده شده است. این قسمت همان جعبه قطعات است که می توان از داخل ان انواع ترانزیستور ها، مقاومت ها، دیود ها و ... را انتخاب نمود. با کلیک روی Library و زدن روی گزینه pick devices هم میتوان به این قسمت دسترسی پیدا کرد. برای انتخاب قطعه مورد نظر فقط کافی است نام قطعه را در نواری که در تصویر مشخص شده وارد کرده و جستجو کنیم.
گاهی ممکن است که قطعه ای در دسترس نباشد. مثل بعضی سنسور ها یا Arduino . تحت این شرایط می شود که کتابخانه های مربوطه را دانلود کرد و در مسیر نصب نرم افزار کپی کرده. پروتئوس رو بسته و مجدد پروژه را راه اندازی کرده تا کتابخانه قطعه مورد نظر را شناسایی کند. و یا اینکه از قسمت نوار بالا، بخش library روی گزینه import path کلیک کرده و فایل دانلودی مربوط به قطعه مثل Arduino را اضافه می کنیم. 




و دو بخش آخر محیط شماتیک Schematic sheet و Status Bar هستن. در بخش اول که به شکل صفحه ای مشبک است، طراحی مدار صورت میگیرد. یعنی قطعات بعد از اینکه انتخاب می شوند در این محیط قرار گرفته و ارتباطات میان انها توسط سیم بهم برقرار می شود. و در آخر، بخش پایین که می توان در آن مختصات مکان نما که با x و y معلوم شده است را مشاهده کرد.و سمت چپ نام شیت فعلی و پیام های هشدار و خطا هنگام طراحی یا شبیه سازی مدار ، دکمه های شروع و توقف شبیه سازی قابل مشاهده می باشد.


<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_09-59-167.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 18 : Devices Panel2_
</div>


<div style="display: flex; justify-content: center; gap: 10px;margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/photo_2025-10-16_15-47-01.jpg" alt="IPS1" style="width: 100%; height: 70%; border-radius:5px; object-fit:cover; ">
</div>

<div class="caption" style="text-align: center; margin-top: 8px; margin-bottom:15px">
    _figure 19 : Shematic Area_
</div>


در فاز بعدی پروژه به طراحی چند مدار الکتریکی ساده می پردازیم و در حین طراحی به معرفی بعضی اصول و استاندارد های طراحی اشاره خواهیم کرد.

## نحوه طراحی شماتیک مدارهای الکتریکی 

 قصد داریم مداری ساده با مقاومت ، ال ای دی ، منبع تغذیه، دیود در محیط پروتئوس بسازیم. طبق روش های گفته شده ابتدا پروژه ای جدید می سازیم. سپس از جعبه قطعات(pick tools)نام لاتین هر کدام از ابزار ها را در نوار جستجو تایپ میکنیم. برای مقاومت res برای دیود diode برای منبع تغذیه battery برای ال ای دی LED . سپس روی ok کلیک کرده تا ابزار ها همانند تصویر زیر در پنجره ابزار ها قرار گیرند.
در طول پروژه سعی می شود نکات و اصول مورد نیازی که لازم است هنگام طراحی رعایت شود را ذکر کنیم

<div style="display: flex; justify-content: center; align-items:center;margin-top:40px ">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 132413.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 20: Select Tools_
</div>

سپس هر کدام رو انتخاب کرده و روی صفحه قرار میدهیم. مانند یک drag کردن ساده.

<div style="display: flex; justify-content: center; align-items:center; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 135503.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 21: Drag Tools To Area_
</div>

هنوز مدار کامل نشده. کافی است که المان ها را با سیم بهم متصل کنیم. هر المانی دو سر مثبت  و منفی دارد. باید توجه کرد که سر مثبت المان ها به سر مثبت باتری و سر منفی انها با سیم به سر منفی منبع تغذیه متصل شود. روی یک سر المان کلیک کرده تا شکل سیم ظاهر شود . سپس با حفظ قطبیت به هم متصل می کنیم. 
دقت شود که سیم ها فقط در جهت افقی یا عمودی امتداد می یابند نه مورب.

<div style="display: flex; justify-content: center; align-items:center; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 142831.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 22: Drawing Curcuit_
</div>

ممکن است که مدار را که متصل کردیم، ال ای دی روشن نشود. این چند حالت میتواند داشته باشد.

1- جهت دیود مخالف جریان عبوری باشد

2- مقدار مقاومت به قدری زیاد است که مانع از عبور جریان میشود

3- ال ای دی برای روشن شدن به مقدار ولتاژی بیشتر از ولتاژ باتری نیاز دارد

 کام به گام بررسی میکنیم . ابتدا دو بار روی ال ای دی راست کلیک کرده تا مشخصات آن رو ببینیم.

 <div style="display: flex; justify-content: center; align-items:center; margin-top:40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 144903.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 23: Drawing Curcuit 2_
</div>

با توجه به شکل متوجه می شویم که این ال ای دی برای روشن شدن به حداقل ولتاژ 2.2 ولت احتیاج دارد. پس باید از جعبه قطعات باتری ای با ولتاژ بالاتر انتخاب کنیم. دقت شود که وقتی مدار در حالت فعال قرار دارد نمی توان هیچ کدام از اجزای مدار را تغییر داد. بلکه باید روی گزینه  stop که با نماد مربع درنوار status قرار گرفته کلیک کرده سپس اقدام به برداشتن یا جایگزین کردن المان های مدار کرد. 

البته میتوان برای شناسایی ارور های هنگام طراحی به پیام ها درنوار پایین مراجعه کرد

 <div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 143104.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 24: Handling Errors_
</div>

برای حذف المان ها کافی است روی ان ها راست کلیک کرده و روی گزینه delete در پنجره ای که باز می شود کلیک کنیم. می بینیم که المان به همراه سیم های متصل به آن به سادگی حذف خواهند شد.


 <div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 153006.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 25: Deleting Elements_
</div>

از قسمت جعبع قطعات یک مقاومت 1 کیلو اهمی و یک منبع تغذیه 9 ولتی انتخاب می کنیم و مانند شکل زیر دوباره مدار رو می بندیم.

 <div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 155410.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 26: Replace Elements In Curcuit_
</div>


حالا روی دکمه run the simulation در نوار پایین کلیک میکنیم. مشاهده میکنیم که LED روشن می شود.


 <div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 155430.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 27:  Turning On The LED_
</div>

حالا اگر جهت دیود در مدار را برعکس کنیم یعنی سیم ها رو به دیگر قطب های آن متصل کنیم. اگر روی دکمه اجرا کلیک کنیم، می بینیم که ال ای دی روشن نمی شود.

 <div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 161004.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 28:  Unable To Turning On The LED_
</div>

 از همین قسمت متوجه می شویم که دیود ها یک سو کننده های جریان هستند یعنی جریان در مدار را تنها از یک سو عبور می دهند.
 
 گاهی ممکن است در طراحی اشتباهاتی رخ دهد. از قبیل اتصال یک سیم اشتباه به ترمینال یک از المان های مدار. در این شرایط کافی است با نگهداری هم زمان کلید های Ctrl  و  z تغییرات رو به حالت (های) قبل بازگردانیم.


اگر دقت کنیم می بینم که این المان ها دو پرچسب(lable) دارند. بالایی Part Id نام دارد که برای مقاومت با R  و برای دیود با  D مشخص میشوند. هر چند طبق تصویر زیر می توانیم این مقادیر پیش فرض را به دلخواه خودمان تغییر دهیم.
برای تغییر مقدار هر پرچسب کافی است روی آن کلیک کنیم



<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 161935.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 29:  Element's Lables_
</div>


بر چسب پایینی مربوط به مقدار است که با part value  مشخص می شود. نکته حائز اهمیت در این بخش این است که میتوان این مقادیر را تغییر داد. مثلا طبق تصویر زیر به جای مقاومت 1 کیلو اهمی ما مقدار 0.25 کیلو اهم را وارد کردیم.


حالا اگر دوباره مدار رو راه اندازی کنیم، می بینیم که مقدار روشنایی LED نسبت به حالت قبلی بیشتر شد!

<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 162052.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 30:  Element's Lables 2_
</div>

در مرحله اخر روی گزینه save project از نوار بالا کلیک کرده تا پروژه ذخیره شود. چون گاهی ممکن است مدار ترسیم ان ساده نبوده و نیازمند دقت و وقت بیشتر است . لذا بهتر است پروژه را در مسیری که از قبل تعیین کردیم، ذخیره کنیم.

<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Screenshot 2025-10-17 165029.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 31:  save project_
</div>


حال میخواهیم مدار دیگری را با همین روش های اموخته شده رسم کنیم که کمی پیچیده تر از این مدار الکتریکی ساده است.

میخواهیم با بستن یک مدار یک سون سگمنت را روشن کنیم
در ابتدا یک پروژه در مسیر دلخواه خود می سازیم. وسایل مورد نیاز ما: یک سون سگمنت آند مشترک، 7 عدد مقاومت به ازای 7 LED سون سگمنت، یک دیکودر یا IC آند مشترک که در ایجا 7447  است. یک باتری و ۴ سوویچ برای تولید اعداد باینری بین 0 تا 9



<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 32:  Seven Segment_
</div>


حالا که ابزار های لازم را در اختیار داریم، کافی است که اتصالات لازم را برقرار کنیم. ابتدا یک سر هر سوویچ را به قطب منفی باتری (می توانیم از سر یک سوویچ به قطب منفی وصل کنیم و سه تای دیگر را به همین سیم وصل شده به قطب منفی متصل کنیم ) وصل می کنیم . مشابه این کار را با سر دیگر سوویچ ها ولی این بار به قطب مثبت باتری وصل میکنیم (انگار یک سر سوویچ ها را به GND و سر دیگر ان ها را به Vcc وصل کرده ایم.)


<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture2.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 33:  Seven Segment 1_
</div>

در قدم بعدی باید 3 ورودی کنترلی سون سگمنت را ( LT , RBI , BI) به ولتاژ مثبت باتری وصل کنیم.


<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture4.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 34:  Seven Segment 2_
</div>


حال در گام بعدی 7 خروجی دیکودر را به ترتیب به ورودی های a تا  g سون سگمنت متصل می کنیم. در گام یعد پایه مشترک سون سگمنت را به Vcc وصل می کنیم
<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture5.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 35:  Seven Segment 3_
</div>


حالا که مدار کامل شد کافی است که با سوویچ ها ورودی بدهیم. می خواهیم عدد 1 را روی سون سگمنت نشان دهیم.به ترتیب زیر اقدام می کنیم:

SW 1 --> Vcc

SW 2 --> GND

SW 3 --> GND

SW 4 --> GND


<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture6.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 36:  Seven Segment 4_
</div>

حالا سوویچ ها رو به ترتیب زیر وصل می کنیم:

SW 1 = GND

SW 2 = GND

SW 3 = Vcc

SW 4 = GND


<div style="display: flex; justify-content: center; align-items:center; margin-top: 40px">
    <img src="./assets/circuiteffort/Circuit_Schematic_Drawing_Project/Capture7.png" style="height:70%; width: 100%;">
</div>
<div class="caption" style="text-align:center; margin-top:10px; margin-bottom:15px">
    _figure 37:  Seven Segment 5_
</div>


## نتیجه گیری

در این پروژه انواع ابزار های رایج رسم شماتیک مدار را نظیر پروتئوس ، کیکد، اورکد و آلتیوم را از نظیر کاربری محیط نرم افزار ، کتابخانه قطعات ، امکان طراحی PCB و .. بررسی کنیم. در بخش دوم پروژه یاد گرفتیم که چگونه پروتئوس را نصب و راه اندازی کنیم . با محیط کار آن آشنا شدیم ، اینکه چگونه از چعبه قطعات ، ابزاری را انتخاب یا در صورت نبود آن ، کتابخانه اش را به پروتئوس اضافه کنیم و در فاز آخر پروژه با ترسیم دو مدار الکتریکی سعی شد که بعضی از نکات مهم و اصولی در مورد طراحی را بیاموزیم.


## منابع 

<div style="direction: rtl; text-align: right;">
  <a href="https://www.labcenter.com" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://www.labcenter.com
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://fritzing.org/learning/" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://fritzing.org/learning/
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://www.altium.com/documentation" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://www.altium.com/documentation
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/orcad.html" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/orcad.html
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://docs.kicad.org/" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://docs.kicad.org
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://theengineeringmindset.com/the-basics-of-diodes-explained/" 
     style="text-decoration:none; color:green; font-weight:bold;" 
     target="_blank">
     https://theengineeringmindset.com/the-basics-of-diodes-explained
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://www.electronics-tutorials.ws/blog/7-segment-display-tutorial.html" 
    style="text-decoration:none; color:green; font-weight:bold;" 
    target="_blank">
    https://www.electronics-tutorials.ws/blog/7-segment-display-tutorial.html
  </a>
</div>

<div style="direction: rtl; text-align: right;">
  <a href="https://www.geeksforgeeks.org/installation-guide/how-to-download-and-install-proteus-software-on-windows/" 
    style="text-decoration:none; color:green; font-weight:bold;" 
    target="_blank">
   https://www.geeksforgeeks.org/installation-guide/how-to-download-and-install-proteus-software-on-windows/
  </a>
</div>
