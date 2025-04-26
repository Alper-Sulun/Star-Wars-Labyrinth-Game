# 🌌 Star Wars Temalı Labirent Oyunu

## 📚 Proje Hakkında
Bu proje, **nesne yönelimli programlama (OOP)** ve **veri yapıları** konseptlerini uygulamak amacıyla geliştirilmiştir.  
Oyuncu, sabit bir harita üzerinde seçtiği karakterle düşmanlardan kaçarak kupaya ulaşmaya çalışır.  
Bu süreçte kullanıcı arayüzü, karakter etkileşimleri ve algoritmik yol bulma mekanizmaları kullanılmıştır.

---

## 🎯 Projenin Amacı
- OOP prensiplerini uygulamak
- Veri yapıları ve algoritmalarla çalışmak
- Yol bulma algoritmaları (BFS, vs.) ile düşman hareketleri oluşturmak
- Basit bir masaüstü oyun deneyimi sunmak

---

## 📋 Gereksinim Analizi

### 🎨 Arayüz Gereksinimleri
- Masaüstü uygulama olarak tasarlandı.
- Grafiksel harita gösterimi (Pygame kullanılarak).
- Oyuncunun başlangıç noktası: **Sarı kutu**
- Düşman girişleri: **Mavi oklar**
- Karakter konumu ve can bilgisi kullanıcıya her zaman gösterilir.
- Yön tuşları ile iyi karakter hareket ettirilir.

### ⚙️ Fonksiyonel Gereksinimler
- Oyuncu, **Luke Skywalker** veya **Master Yoda** karakterlerinden birini seçebilir.
- Düşman karakterler (`Darth Vader`, `Kylo Ren`, `Stormtrooper`) dinamik olarak `harita.txt` dosyasından yüklenir.
- Düşmanlar, her hamlede en kısa yolu bularak oyuncuya yaklaşır.
- Kupaya ulaşan oyuncu oyunu kazanır, canlar biterse **Game Over** ekranı gösterilir.
- Düşman karakterlerin kendilerine özgü özel yetenekleri bulunur.

---

## 🛠️ Kullanılan Teknolojiler
- **Programlama Dili**: Python 🐍
- **Grafik**: Pygame 🎮

---

## 🏗️ Mimari Tasarım
- **Model-View-Controller (MVC)** yapısı önerildi.
- Karakterler sınıflar şeklinde modellendi.
- Harita ve karakter verileri harici dosyalardan (`map.txt`, görseller, ses dosyaları) okunur.

---

## 🎮 Kullanıcı Arayüzü
- Oyun başladığında grafiksel bir harita açılır.
- İyi karakter (Luke veya Yoda) sarı kutuda başlar.
- Düşman giriş kapıları harflerle gösterilir.
- Can azaldıkça kalp görselleri ile görsel bildirim yapılır.
- "Kazandın" ve "Kaybettin" ekranları için özel müzikler oynatılır.
- Özel efektler (duvar yıkma, can azalma) için ses efektleri mevcuttur.

---

## 🧩 Kodlanan Bileşenler

- **Lokasyon Sınıfı**: Karakterlerin konumlarını yönetir.
- **Karakter Sınıfı**: Ortak karakter özelliklerini barındırır.
- **LukeSkywalker / MasterYoda**: Farklı can sistemleri vardır.
- **DarthVader / KyloRen / Stormtrooper**: Özel hareket kuralları ve yol bulma algoritmaları içerir.

---

## 🧠 Karşılaşılan Zorluklar ve Çözüm Yöntemleri
- **Can Azaltma Gösterimi**: Haritaya yeni bir sütun eklenerek kalp görselleriyle can durumu görsel olarak yönetildi.
- **Darth Vader'ın Duvar Yıkması**: BFS algoritması özelleştirildi ve Darth Vader'ın hareket ederken duvarları kırıp geçmesi sağlandı.

---

## 🚨 Eksik Yönler
- Düşman karakterlerin `EnKısaYol()` metodları sadece path (yol) oluşturmak için kullanıldı. Hareket işlemleri ana dosyada yönetildi.
- Darth Vader'ın EnKısaYol() metodu, duvar yıkma özelliği nedeniyle özel olarak değiştirildi.

---


## 🌟 Özet
Bu projede nesne yönelimli programlama teknikleri, veri yapıları, yol bulma algoritmaları ve grafik arayüz geliştirme konularında uygulamalı deneyim kazandırılması hedeflenmiştir.

---

> 🎵 *"May the Force be with you!"* 🌟

