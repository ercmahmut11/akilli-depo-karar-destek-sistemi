#  Akıllı Lojistik Depolarında Karar Destek Sistemi ve Kesikli Olay Simülasyonu

Bu proje, modern lojistik merkezlerinde sipariş akış hızı, otonom yönlendirmeli araç (AGV) kapasite planlaması ve operasyonel darboğazların analizi için geliştirilmiş **Kesikli Olay Simülasyonu (DES)** tabanlı bir **Karar Destek Sistemi** dashboard uygulamasıdır.


 Projenin Amacı ve Kapsamı
Akıllı depo süreçlerini dijital ortamda modelleyerek operasyon yöneticilerine stratejik ve veri odaklı karar desteği sağlamak amaçlanmıştır. Sistem:
* Gelen siparişleri **Express (P1)**, **Standart (P2)** ve **İade (P3)** öncelik sınıflarına göre ayırır.
* Dinamik girdi parametrelerine göre **AGV Robot Doluluk Oranlarını** hesaplar.
* Sistem kilitlenmelerini önceden tespit ederek yapay veri odaklı **Tavsiye Modülü** aracılığıyla çözüm önerileri sunar.


 Kullanılan Teknolojiler
Proje tamamen açık kaynaklı mimariler ve popüler veri analitiği kütüphaneleri kullanılarak Python ile geliştirilmiştir:
* **Python** (Simülasyon mantığı ve veri işleme)
* **Streamlit** (Dinamik ve etkileşimli Web UI / Dashboard)
* **Matplotlib** (Performans analiz grafikleri ve pasta/bar dağılımları)
* **Pandas & NumPy** (Sayısal hesaplamalar ve veri manipülasyonu)


 Kurulum ve Çalıştırma Talimatları

Projenin yerel bilgisayarınızda (Localhost) sorunsuz bir şekilde ayağa kaldırılabilmesi için aşağıdaki adımları sırasıyla takip ediniz.

###  Ön Gereksinimler
Sisteminizde **Python 3.8** veya üzeri bir sürümün kurulu olduğundan emin olunuz. Python kurulu değilse [python.org](https://www.python.org/) adresinden indirebilirsiniz.


###  Adım Adım Kurulum

#### 1. Projeyi Bilgisayarınıza İndirin (Klonlayın)
Terminalinizi (Komut İstemi) açın ve projenin indirileceği dizine giderek aşağıdaki komutla repoyu klonlayın:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/akilli-depo-karar-destek-sistemi.git](https://github.com/KULLANICI_ADINIZ/akilli-depo-karar-destek-sistemi.git)
cd akilli-depo-karar-destek-sistemi
