# Reservasi Tiket

Aplikasi web ini adalah sistem manajemen reservasi tiket sederhana yang dibangun dengan Flask, HTML, dan CSS. Sistem ini mencakup fitur untuk mendaftarkan pengguna, login/logout, membuat reservasi baru, memperbarui data reservasi, dan menghapus reservasi.

## Fitur
1. **Registrasi Pengguna**: Pengguna baru dapat mendaftar dengan username dan password.
2. **Login dan Logout**: Sistem autentikasi untuk mengamankan halaman dashboard.
3. **Dashboard**: Menampilkan daftar reservasi yang sudah dibuat.
4. **CRUD Reservasi**:
   - Membuat reservasi baru.
   - Memperbarui informasi reservasi.
   - Menghapus reservasi.

## Teknologi yang Digunakan
- **Backend**: Flask (Python)
- **Database**: MySQL dengan library `pymysql`
- **Frontend**: HTML, CSS, dan Bootstrap untuk tampilan antarmuka.

## Instalasi

### Prasyarat
1. Python 3.x
2. MySQL Server
3. Virtualenv (opsional, untuk lingkungan terisolasi)

### Langkah Instalasi
1. Clone repositori ini:
   ```bash
   git clone <repository-url>
   cd reservasi-tiket
   ```

2. Buat virtual environment (opsional namun disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate   # Untuk Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Buat database MySQL:
   ```sql
   CREATE DATABASE reservasi_tiket;
   USE reservasi_tiket;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       password_hash VARCHAR(255) NOT NULL
   );

   CREATE TABLE reservations (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nama VARCHAR(100) NOT NULL,
       kategori_destinasi VARCHAR(50) NOT NULL,
       kota_destinasi VARCHAR(100) NOT NULL,
       jumlah_orang INT NOT NULL,
       tanggal DATE NOT NULL
   );
   ```

5. Jalankan aplikasi:
   ```bash
   python app.py
   ```

6. Buka browser dan akses aplikasi di:
   ```
   http://127.0.0.1:5000
   ```

## Struktur Proyek
```
reservasi-tiket/
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── create.html
│   ├── update.html
│   ├── login.html
│   └── register.html
├── static/
│   └── (optional CSS/JS files)
├── app.py
├── requirements.txt
└── README.md
```

## Dependencies
Semua dependencies tercantum dalam file `requirements.txt`. Berikut adalah beberapa library utama yang digunakan:
- Flask
- PyMySQL
- Werkzeug

## Kontribusi
Kontribusi sangat diterima. Silakan buat pull request atau ajukan issue jika Anda menemukan bug atau memiliki ide untuk fitur baru.

## Lisensi
Proyek ini menggunakan lisensi [MIT](LICENSE).

## Anggota Kelompok
1. Viona Leny Anjani
2. Shanny Novalina Turnip
3. Ulfah Nur Uzlifah 
