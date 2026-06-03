# 📊 Akıllı Lojistik Depolarında Karar Destek Sistemi ve Kesikli Olay Simülasyonu

Bu proje, modern lojistik merkezlerinde sipariş akış hızı, otonom yönlendirmeli araç (AGV) kapasite planlaması ve operasyonel darboğazların analizi için geliştirilmiş **Kesikli Olay Simülasyonu (DES)** tabanlı bir **Karar Destek Sistemi** dashboard uygulamasıdır.

## 🏛️ Kurumsal Bilgiler
* **Üniversite:** T.C. Mersin Üniversitesi
* **Geliştirici:** Mahmut Ercan (Öğrenci No: 22430070018)
* **Proje Türü:** Karar Destek Sistemi ve Simülasyon Uygulaması

---

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



 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Projeyi Klonlayın:**
```bash
git clone [https://github.com/kullaniciadi/akilli-depo-simulasyonu.git](https://github.com/kullaniciadi/akilli-depo-simulasyonu.git)
cd akilli-depo-simulasyonu