# Patimah
# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen perpustakaan berbasis MVC (Model-View-Controller) menggunakan Python, CustomTkinter, dan basis data MySQL.

## Struktur Direktori

Modul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── config/
│   └── database.py
├── controller/
│   ├── anggota_controller.py
│   ├── auth_controller.py
│   └── buku_controller.py
├── models/
│   ├── anggota_model.py
│   ├── buku_model.py
│   └── user_model.py
├── views/
│   ├── anggota_view.py
│   ├── buku_view.py
│   └── login_view.py
├── test/
│   ├── test_auth.py
│   └── test_buku.py
├── main.py
├── requirements.txt
└── README.md

--Panduan Instalasi & Konfigurasi Database

1. Konfigurasi Database MySQL:
a. Buka aplikasi Laragon lalu klik Start All.
b. Buat database baru bernama db_perpustakaan melalui phpMyAdmin / HeidiSQL.
c. Eksekusi tabel users, buku, dan anggota.

2. Setup Proyek:
bash
# Clone repositori:
git clone https://github.com/HQID/modul3.git
cd Modul3_RPL

# Aktifkan Virtual Environment:
.\env\Scripts\activate

# Instal dependensi:
pip install -r requirements.txt

--Cara Menjalankan Aplikasi

1. Jalankan via Script Python:
Bash
python main.py
2. Jalankan via Executable (.exe):
Masuk ke folder dist/ lalu klik dua kali pada Aplikasi Perpustakaan.exe (Pastikan MySQL di Laragon dalam kondisi aktif).