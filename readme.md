# Asesmen Software Engineer - Aplikasi Otentikasi (Django)

Ini adalah proyek aplikasi web mandiri yang dibangun menggunakan framework Django. Proyek ini dibuat sebagai bagian dari proses asesmen untuk posisi **Software Engineer** di **PT Informatika Media Pratama**.

Tujuan utama proyek ini adalah untuk mendemonstrasikan implementasi sistem otentikasi pengguna dan operasi CRUD dasar pada data pengguna.

## Fitur Utama

-   **Otentikasi Pengguna**:
    -   Registrasi Pengguna Baru (Sign Up).
    -   Login Pengguna (Sign In).
    -   Logout Pengguna (Sign Out).
-   **Manajemen Pengguna (CRUD User)**[cite: 18]:
    -   **Create**: Pengguna dapat dibuat melalui halaman Sign Up.
    -   **Read**: Pengguna yang sudah login dapat melihat detailnya (contoh: di halaman profil). Admin dapat melihat semua pengguna di panel admin.
    -   **Update**: Fungsionalitas untuk memperbarui data pengguna (contoh: halaman edit profil).
    -   **Delete**: Fungsionalitas untuk menghapus akun pengguna.

## Teknologi yang Digunakan

-   Python
-   Django
-   Pip & Virtualenv

## Panduan Instalasi dan Setup

Berikut adalah langkah-langkah untuk menjalankan proyek ini di lingkungan lokal.

1.  **Clone Repositori**
    ```bash
    git clone Assesment-Django-IMP
    cd Assesment-Django-IMP
    ```

2.  **Buat dan Aktifkan Virtual Environment**
    Sangat direkomendasikan untuk menggunakan virtual environment untuk mengisolasi dependencies.
    ```bash
    # Membuat virtual environment
    python -m venv venv

    # Mengaktifkan di Windows
    .\venv\Scripts\activate

    # Mengaktifkan di macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Pastikan Anda berada di direktori utama proyek (di mana file `requirements.txt` berada), lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Migrasi Database**
    Perintah ini akan membuat database SQLite dan semua tabel yang dibutuhkan (termasuk tabel user, grup, dll).
    ```bash
    python manage.py migrate
    ```

5.  **Buat Superuser (Opsional)**
    Dengan membuat superuser, Anda bisa masuk ke panel admin Django untuk melihat semua data pengguna yang terdaftar.
    ```bash
    python manage.py createsuperuser
    ```
    Ikuti instruksi untuk membuat username dan password.

6.  **Jalankan Server**
    ```bash
    python manage.py runserver
    ```
    Secara default, aplikasi akan berjalan di `http://127.0.0.1:8000`.

## Cara Menggunakan Aplikasi

1.  Buka browser dan kunjungi `http://127.0.0.1:8000/`.
2.  Klik **Sign Up** untuk membuat akun baru.
3.  Setelah berhasil, Anda akan diarahkan ke halaman **Login**. Masuk menggunakan akun yang baru saja dibuat.
4.  Setelah berhasil login, Anda akan diarahkan ke halaman utama.
