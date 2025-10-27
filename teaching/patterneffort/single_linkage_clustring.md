---
layout: persian
classes: wide rtl-layout
dir: rtl
title: "روش های تجمیعی در یادگیری ماشین"
permalink: /teaching/studenteffort/patterneffort/single_linkage_clustring/
author_profile: true

header:
  overlay_image: "/assets/images/background.jpg"
  overlay_filter: 0.3
  overlay_color: "#5e616c"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
---

# روش‌های تجمعی (Agglomerative Methods) در یادگیری ماشین
---


<p>

<p> نویسنده : عرفان موسوی نژاد</p>
  <a href="mailto:er.mousavinezhad@gmail.com">
er.mousavinezhad@gmail.com  </a>
</p>
<p>
دانشگاه فردوسی مشهد - دانشکده مهندسی - گروه هوش مصنوعی
</p>


## مقدمه
---

پیش از آن‌که وارد الگوریتم‌های تجمعی شویم، لازم است ابتدا مفاهیم پایه‌ای در تکنیک‌های خوشه‌بندی را درک کنیم. بنابراین، ابتدا به مفهوم خوشه‌بندی (Clustering) در یادگیری ماشین می‌پردازیم:

خوشه‌بندی مجموعه‌ای گسترده از روش‌هاست که هدف آن یافتن زیرگروه‌ها یا خوشه‌هایی در داده‌هاست؛ به‌گونه‌ای که اعضای هر خوشه از نظر ویژگی‌ها یا مشخصه‌های درون‌داده‌ای به یکدیگر شبیه باشند، اما با اعضای خوشه‌های دیگر تفاوت داشته باشند.
اصل اساسی در خوشه‌بندی این است که داده‌های موجود درون یک خوشه باید تا حد ممکن بیشترین شباهت را با یکدیگر داشته باشند و در مقابل، داده‌های خارج از آن خوشه باید بیشترین تفاوت را نسبت به اعضای آن داشته باشند.
در علم داده و یادگیری ماشین، خوشه‌بندی به‌صورت کلی به چند دسته‌ی اصلی تقسیم می‌شود که از مهم‌ترین آن‌ها می‌توان به موارد زیر اشاره کرد:


| روش  | ویژگی‌ها |
| ---------------------- | ------------------------------------- |
| **روش افرازی (Partitioning Method)**          | - از میانگین یا میدویید برای نمایش مرکز خوشه استفاده می‌کند.<br>- با تکیه بر فاصله، خوشه‌ها را به‌صورت تکراری بهبود می‌دهد.<br>- خوشه‌هایی مجزا با شکل کروی یا تقریباً کروی پیدا می‌کند.<br>- برای مجموعه‌داده‌های کوچک تا متوسط مناسب است. |
| **روش سلسله‌مراتبی (Hierarchical Method)**     | - با تجزیه و ترکیب، ساختاری درخت‌مانند ایجاد می‌کند.<br>- از فاصله بین نزدیک‌ترین یا دورترین نقاط خوشه‌های مجاور برای بهبود استفاده می‌کند.<br>- خطاهای ایجادشده در مراحل اولیه در مراحل بعدی قابل تصحیح نیستند.                        |
| **روش مبتنی بر چگالی (Density-Based Method)** | - برای شناسایی خوشه‌هایی با شکل‌های دلخواه بسیار مفید است.<br>- می‌تواند نقاط پرت (Outlier) را فیلتر کند.              |

اما برای درک بهتر روش‌های تجمعی (Agglomerative Methods)، ابتدا باید با روش‌های سلسله‌مراتبی (Hierarchical Methods) آشنا شویم.



## روش‌های سلسله‌مراتبی (Hierarchical Methods)
---
در این روش، داده‌ها در قالب یک ساختار درختی (Tree-like Structure) گروه‌بندی می‌شوند. این روش شامل دو الگوریتم اصلی برای خوشه‌بندی است:

1.	خوشه‌بندی تقسیم‌گر (Divisive Clustering):
در این رویکرد، از استراتژی بالا به پایین (Top-Down Strategy) استفاده می‌شود. فرآیند به این صورت است که در ابتدا همه‌ی داده‌ها در یک خوشه‌ی بزرگ قرار دارند، سپس این خوشه به‌صورت بازگشتی به خوشه‌های کوچکتر و کوچکتر تقسیم می‌شود. این فرایند زمانی متوقف می‌شود که:
-	شرط توقف از پیش تعیین‌شده توسط کاربر برآورده شود، یا
-	هر خوشه تنها شامل یک داده (شیء) باشد.


2.	خوشه‌بندی تجمعی (Agglomerative Clustering):
در این رویکرد، از استراتژی پایین به بالا (Bottom-Up Strategy) استفاده می‌شود. فرآیند به این صورت است که در ابتدا هر داده به‌صورت جداگانه یک خوشه‌ی مستقل تشکیل می‌دهد، سپس در هر مرحله دو خوشه‌ی نزدیک‌تر یا مشابه‌تر با هم ادغام می‌شوند تا خوشه‌های بزرگ‌تری به‌وجود آید. این روند تا زمانی ادامه دارد که:
-	شرط توقف تعریف‌شده توسط کاربر برآورده شود، یا
-	همه‌ی خوشه‌ها در نهایت در یک خوشه‌ی واحد ادغام شوند.

یک دندروگرام (Dendrogram) که ساختاری درخت‌مانند دارد، برای نمایش نتایج خوشه‌بندی سلسله‌مراتبی (Hierarchical Clustering) به‌کار می‌رود.
در این ساختار:
-	هر شیء (داده منفرد) با یک گره برگ (Leaf Node) نمایش داده می‌شود.
-	هر خوشه (که از ادغام چند داده یا خوشه کوچکتر تشکیل شده است) با یک گره ریشه (Root Node) نشان داده می‌شود.

به بیان دیگر، دندروگرام به ما نشان می‌دهد که چه نقاطی، در چه مراحلی و با چه میزان شباهتی با یکدیگر ادغام شده‌اند.
در پایین، درخت داده‌های منفرد قرار دارند و با بالا رفتن از درخت، خوشه‌های بزرگ‌تر حاصل از ادغام‌های پی‌در‌پی نمایش داده می‌شوند.
نمایی از یک دندروگرام نمونه در شکل زیر نشان داده شده است:

<img src="/assets/patterneffort/single_linkage_clustring/Dendrogram.png" alt="Single Linkage">



## مبنای ادغام خوشه ها (Linkage Criteria)
---
خوشه‌ها بر اساس فاصله بین آن‌ها ادغام می‌شوند.
برای محاسبهٔ این فاصله بین خوشه‌ها، از روش‌های مختلفی تحت عنوان معیار پیوند (Linkage Criteria) استفاده می‌شود.
این معیار مشخص می‌کند که فاصله بین دو خوشه چگونه و بر اساس چه تابعی از فاصله‌های جفتی بین اعضای آن خوشه‌ها محاسبه گردد.

در ادامه چهار نوع رایج معیار پیوند را می‌بینیم:

| نوع معیار پیوند                            | تعریف فاصله بین دو خوشه                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------- |
| **Single Linkage (پیوند تک‌گانه)**          | فاصله بین دو خوشه برابر است با **کمترین فاصله** بین اعضای دو خوشه.         |
| **Complete Linkage (پیوند کامل)**          | فاصله بین دو خوشه برابر است با **بیشترین فاصله** بین اعضای دو خوشه.        |
| **Average Linkage (پیوند میانگین)**        | فاصله بین دو خوشه برابر است با **میانگین تمام فاصله‌ها** بین اعضای دو خوشه. |
| **Centroid Linkage (پیوند بر مبنای مرکز)** | فاصله بین دو خوشه برابر است با **فاصله بین مراکز هندسی (Centroid)** آن‌ها.  |


به‌طور خلاصه، تفاوت اصلی این معیارها در نحوهٔ محاسبهٔ فاصله بین خوشه‌هاست و همین تفاوت باعث می‌شود که ساختار و شکل نهایی خوشه‌ها در نمودار دندروگرام متفاوت باشد.

در این درس تنها پیوند تک گانه (مجرد) را بصورت کامل تشریح خواهیم کرد.


## خوشه بندی اتصال مجرد (Single-Linkage Clustering)
---
در آمار، خوشه‌بندی اتصال مجرد یکی از چندین روشِ خوشه‌بندی سلسله‌مراتبی است. این روش بر پایه گروه‌بندی خوشه‌ها به شیوه پایین به بالا (خوشه‌بندی تجمعی) استوار است؛ به‌طوری که در هر گام، دو خوشه‌ای با یکدیگر ادغام می‌شوند که دارای نزدیک‌ترین زوج از عناصر باشند، به شرطی که آن دو عنصر هنوز به یک خوشه تعلق نداشته باشند.
این روش تمایل دارد خوشه‌هایی باریک و دراز تولید کند که در آن‌ها عناصر مجاورِ درون یک خوشه، فاصله‌ای اندک دارند، اما عناصر واقع در دو انتهای یک خوشه ممکن است فاصله‌ای بسیار بیشتر از دو عنصر متعلق به خوشه‌های دیگر از یکدیگر داشته باشند. برای برخی از داده ها، این ویژگی می‌تواند به ایجاد مشکلاتی در تعریف کلاس‌هایی که بتوانند داده را به شکلی درست تقسیم بندی کند، بینجامد. با این حال، این روش در اخترشناسی برای تحلیل خوشه‌های کهکشانی - که اغلب ممکن است شامل رشته‌های درازی از ماده باشند - پرطرفدار است. در این حوزه کاربردی، این الگوریتم با نام الگوریتم دوستانِ دوستان (friends-of-friends algorithm) نیز شناخته می‌شود.


## الگوریتم
---
بطور کلی برای دو خوشۀ R و S، الگوریتم اتصال مجرد، کمینه فاصله (Minimum Distance) بین نقاط این دو خوشه را به عنوان معیار فاصله بازمی‌گرداند. این روش به دلیل حساسیت بالایی که به داده‌های پرت (Outliers) دارد، و با اتکا به تعداد بسیار معدودی از نقاط مجاور، می‌تواند خوشه‌ها را به یکدیگر متصل کند. این ویژگی منجر به شکل‌گیری خوشه‌هایی با ساختار طویل و زنجیره‌ای می‌شود.


$$ L(R, S) = min(D(i, j)), i \in R, j \in S $$


D(i, j) همان تابع محاسبه فاصله بین i و j است.

<img src="/assets/patterneffort/single_linkage_clustring/Single-Linkage.jpg" alt="Single Linkage">

## حل یک مسال تئوری
---

در این قسمت قصد داریم تا با حل یک مثال تئوری، موضوع را شفاف تر کنیم:

### 1. جدول داده ها

6 داده با مختصات X و Y را به شکلی که در جدول زیر آمده است در نظر بگیرید:



| Sample | X    | Y    |
| ------ | ---- | ---- |
| P1     | 0.40 | 0.53 |
| P2     | 0.22 | 0.38 |
| P3     | 0.35 | 0.32 |
| P4     | 0.26 | 0.19 |
| P5     | 0.08 | 0.41 |
| P6     | 0.45 | 0.30 |




### 2. فرمول ها

برای محاسبه و خوشه بندی به روش single-linkage clustering، نیاز به فرمول های زیر خواهیم داشت:

- **فاصله اقلیدسی بین 2 نقطه**

<div  dir="ltr" align='justify'>

$$d( (x_1,y_1), (x_2,y_2)) = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$$

</div>

- **فاصله اتصال یگانه بین خوشه A و B** (نزدیکترین همسایه)

<div  dir="ltr" align='justify'>

$$D_{\text{single}}(A,B) = \min_{a\in A,\, b\in B} d(a,b)$$

</div>

حال با داشتن داده ها و فرمول های بالا، نیاز است تا ماتریس فاصله را بسازیم.

### 3. ماتریس فواصل (اقلیدس)


|           | P1     | P2     | P3     | P4     | P5     | P6     |
| --------- | ------ | ------ | ------ | ------ | ------ | ------ |
| <b>P1</b> | 0.0000 | 0.2193 | 0.2304 | 0.4031 | 0.3240 | 0.2357 |
| <b>P2</b> | 0.2193 | 0.0000 | 0.1414 | 0.1949 | 0.1442 | 0.2500 |
| <b>P3</b> | 0.2304 | 0.1414 | 0.0000 | 0.1323 | 0.2713 | 0.1000 |
| <b>P4</b> | 0.4031 | 0.1949 | 0.1323 | 0.0000 | 0.2608 | 0.2500 |
| <b>P5</b> | 0.3240 | 0.1442 | 0.2713 | 0.2608 | 0.0000 | 0.3781 |
| <b>P6</b> | 0.2357 | 0.2500 | 0.1000 | 0.2500 | 0.3781 | 0.0000 |


### 4. مراحل ادغام (Single-Link)


| Step | Left cluster | Right cluster | Single-link distance | New cluster size |
| ---- | ------------ | ------------- | -------------------: | ---------------: |
| 1    | P3           | P6            |               0.1000 |                2 |
| 2    | P2           | P5            |               0.1442 |                2 |
| 3    | P3,P6        | P4            |               0.1323 |                3 |
| 4    | P2,P5        | P1            |               0.2193 |                3 |
| 5    | P2,P5,P1     | P3,P6,P4      |               0.2500 |                6 |


توضیح مختصر برای هر ستون:

- Left cluster / Right cluster: برچسب خوشه‌هایی که در آن مرحله با هم ادغام شده‌اند.

- Single-link distance: کوچک‌ترین فاصلهٔ بین هر جفت نقطه‌ای که در دو خوشه قرار دارند (فاصله‌ای که تعیین‌کنندهٔ ادغام است).

- New cluster size: تعداد عضوهای خوشهٔ جدید پس از ادغام.

محاسبات کامل و مرحله به مرحله را میتوانید در این <a href="https://www.geeksforgeeks.org/machine-learning/agglomerative-methods-in-machine-learning/">لینک</a> مشاهده کنید.

### 5. رسم دندروگرام
در نهایت و پس از اعمال single-linkage clustering، به دندروگرام زیر خواهیم رسید:

<img src="/assets/patterneffort/single_linkage_clustring/dendo1.jpg" alt="Single Linkage">


## پیاده سازی به زبان پایتون
---

حال میخواهیم مثال بالا را با استفاده از پایتون پیاده سازی کرده و بصری سازی را انجام دهیم. برای اینکار، ابتدا لازم است کتابحانه های مورد نیاز را به برنامه اضافه و داده ها را مشخص کنیم:




```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist

# داده‌ها
labels = ["P1","P2","P3","P4","P5","P6"]
coords = np.array([
    [0.40, 0.53],
    [0.22, 0.38],
    [0.35, 0.32],
    [0.26, 0.19],
    [0.08, 0.41],
    [0.45, 0.30],
])

# نمایش داده‌ها
df = pd.DataFrame(coords, columns=["X","Y"], index=labels)
df
```


حال محاسبات فاصله اقلیدسی را به شکل زیر انجام میدهیم:




```python
n = len(coords)
D = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        D[i, j] = np.linalg.norm(coords[i] - coords[j])

dist_df = pd.DataFrame(D, index=labels, columns=labels)
dist_df.round(4)

```

در نهایت برای پیاده سازی الگوریتم single-linkage از کتابخانه `scipy`، از دستور زیر استفاده میکنیم:


```python
# الگوریتم single-linkage با scipy
Z = linkage(pdist(coords, 'euclidean'), method='single')

# نمایش ماتریس linkage
linkage_df = pd.DataFrame(Z, columns=["Cluster 1", "Cluster 2", "Distance", "Cluster Size"])
linkage_df.round(4)

```


در نهایت برای رسم دندروگرام، خواهیم داشت:


```python
plt.figure(figsize=(8, 5), dpi=120)
dendrogram(Z, labels=labels, color_threshold=0.25)
plt.title("Single-Link Dendrogram (Euclidean Distance)", fontsize=12)
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
```


<!-- <details>
<summary>توجه</summary> -->
**توجه**

اگر مایل هستید که تصویر دندروگرام خود را با کیفیت بالا ذخیره کنید، میتوانید از قطعه کد زیر استفاده کنید:


```python
plt.figure(figsize=(8, 5), dpi=300)
dendrogram(Z, labels=labels, color_threshold=0.25)
plt.title("Single-Link Dendrogram (Euclidean Distance)", fontsize=12)
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.tight_layout()

plt.savefig("single_link_dendrogram.png", dpi=300)
plt.close()

print("✅ دندروگرام با موفقیت در فایل 'single_link_dendrogram.png' ذخیره شد.")
```

<!-- </details> -->



## تولید چرخ از اول!
---
اگر شما هم جزو کسانی هستند که دوست دارن چرخ را از ابتدا و به دست خودشان تولید کنند، کد زیر پیاده سازی روش single-linkage clustring هست که دید بسیار خوبی به شما خواهد داد و به راحتی میتوان پارامتر های آن را جایگزین و تمامی تغییرات را بررسی کرد. قطعا برای انجام محاسبات دم دستی و سریع، استفاده از کتابخانه scipy بسیار راحت تر و سریعتر خواهد بود، اما اگر قصد تغییرات و یا اضافه کردن مواردی به این الگوریتم باشید، نیاز است که خودتان دست بکار شده و تمامی مراحل را از ابتدا با ایده های خودتان پیاده سازی کنید. شاید به مدل های متفاوتی بتوان این الگوریتم را پیاده سازی و مصورسازی کرد که در زیر، به آوردن یک نمونه از آن اکتفا میکنیم:


```python
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

class SingleLinkageClustering:
    def __init__(self):
        self.labels_ = None
        self.distances_ = None
        
    def fit(self, X, n_clusters=2):
        """
        Single Linkage Clustering
        
        Parameters:
        X : array-like, shape (n_samples, n_features)
            Input data
        n_clusters : int, default=2
            Number of clusters to form
        """
        n_samples = X.shape[0]
        
        # محاسبه ماتریس فاصله
        self.distances_ = squareform(pdist(X))
        
        # مقداردهی اولیه: هر نقطه یک خوشه است
        clusters = [[i] for i in range(n_samples)]
        
        # الگوریتم سلسله مراتبی
        while len(clusters) > n_clusters:
            # پیدا کردن نزدیک‌ترین دو خوشه
            min_distance = float('inf')
            merge_i, merge_j = -1, -1
            
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    # محاسبه فاصله single linkage (حداقل فاصله بین نقاط دو خوشه)
                    distance = self._single_linkage_distance(clusters[i], clusters[j])
                    if distance < min_distance:
                        min_distance = distance
                        merge_i, merge_j = i, j
            
            # ادغام دو خوشه
            clusters[merge_i].extend(clusters[merge_j])
            clusters.pop(merge_j)
        
        # ایجاد برچسب‌های خوشه
        self.labels_ = np.zeros(n_samples, dtype=int)
        for cluster_idx, cluster in enumerate(clusters):
            for point_idx in cluster:
                self.labels_[point_idx] = cluster_idx
                
        return self
    
    def _single_linkage_distance(self, cluster1, cluster2):
        """محاسبه فاصله single linkage بین دو خوشه"""
        min_distance = float('inf')
        for i in cluster1:
            for j in cluster2:
                distance = self.distances_[i, j]
                if distance < min_distance:
                    min_distance = distance
        return min_distance

# مثال استفاده
if __name__ == "__main__":
    # تولید داده‌های نمونه
    np.random.seed(42)
    
    # سه خوشه مجزا
    cluster1 = np.random.normal(2, 0.5, (10, 2))
    cluster2 = np.random.normal(8, 0.5, (10, 2))
    cluster3 = np.random.normal(5, 0.5, (10, 2))
    
    X = np.vstack([cluster1, cluster2, cluster3])
    
    # اجرای الگوریتم
    slc = SingleLinkageClustering()
    slc.fit(X, n_clusters=3)
    
    # نمایش نتایج
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c='blue', alpha=0.7)
    plt.title('Orginal Data')
    
    plt.subplot(1, 2, 2)
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for i in range(3):
        cluster_points = X[slc.labels_ == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                   c=colors[i], label=f'Cluster {i+1}', alpha=0.7)
    plt.title('Single Linkage Clustering')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
```


در انتها، نمونه تصویری از خروجی کد بالا آورده شده است.

<img src="/assets/patterneffort/single_linkage_clustring/implementation.png" alt="Single Linkage">



### منابع
---


1. <a href="https://www.geeksforgeeks.org/machine-learning/agglomerative-methods-in-machine-learning/" target ="_blank">https://www.geeksforgeeks.org/machine-learning/agglomerative-methods-in-machine-learning/</a>
2. <a href="https://www.geeksforgeeks.org/machine-learning/ml-types-of-linkages-in-clustering/" target ="_blank">https://www.geeksforgeeks.org/machine-learning/ml-types-of-linkages-in-clustering/</a>
3. <a href="https://en.wikipedia.org/wiki/Single-linkage_clustering" target ="_blank">https://en.wikipedia.org/wiki/Single-linkage_clustering</a>
4. <a href="https://harikabonthu96.medium.com/single-link-clustering-clearly-explained-90dff58db5cb" target ="_blank">https://harikabonthu96.medium.com/single-link-clustering-clearly-explained-90dff58db5cb</a>
