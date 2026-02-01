# Desktop Widget (Linux / Ubuntu)

Android widget benzeri, Ubuntu masaüstünde çalışan hafif bir **Python + PyQt** uygulaması.

## 🎯 Amaç
- Web üzerinden veri çekmek
- Masaüstünde **widget hissi veren** bir arayüzde göstermek
- Always-on-top olmayan
- Taskbar / Alt-Tab’da görünmeyen
- Kullanıcı oturum açınca otomatik başlayan bir yapı kurmak

## 🧠 Özellikler (Planlanan)
- PyQt tabanlı masaüstü widget
- Modüler mimari (UI / veri / config ayrımı)
- Periyodik veri güncelleme
- Şeffaf ve çerçevesiz tasarım
- Autostart desteği (Ubuntu)

## 🛠️ Teknolojiler
- Python 3.12+
- PyQt5
- requests
- Ubuntu (GNOME)

## 📁 Proje Yapısı
```text
desktop-widget/
├── main.py
├── widget/
│   ├── ui.py
│   ├── fetcher.py
│   └── config.py
├── requirements.txt
├── .gitignore
└── README.md
