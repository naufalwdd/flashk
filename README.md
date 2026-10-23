# Flashk

Starter aplikasi Flask modular. App tidak membuat tabel atau akun otomatis. Siapkan schema dengan Flask-Migrate, seed akun, lalu jalankan server.

## Setup project

Jalankan perintah dari folder project. Pilih perintah sesuai terminal.

### Windows — PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
```

### Windows — Command Prompt (CMD)

```bat
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
if not exist .env copy .env.example .env
```

### macOS — Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
```

## Siapkan database dan jalankan

Dengan virtual environment aktif, jalankan dari folder project. `db init` hanya dilakukan sekali untuk membuat folder `migrations/`; jika project sudah memiliki `migrations/env.py`, lewati langkah tersebut.

```console
flask db init
flask db migrate -m "initial schema"
flask db upgrade
python seed_super.py
flask run
```

Buka [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login). Login awal mengikuti `SEED_ADMIN_USERNAME` dan `SEED_ADMIN_PASSWORD` di `.env.example`, yaitu **admin** / **admin**. Ganti password tersebut sebelum memakai akun di lingkungan bersama.

`seed_super.py` mengisi akun admin, empat user contoh, dan empat role contoh. Seeder tidak membuat tabel; jalankan `db upgrade` lebih dulu. Aman dijalankan ulang dan melewati username/role yang sudah ada.

## Halaman dan API contoh

- `/app` — dashboard
- `/app/users` — daftar user dari database
- `/app/roles` — daftar role dan permission dari database
- `/app/reports` — laporan
- `/app/settings` — pengaturan workspace

Data diambil dari backend melalui `GET /api/dashboard/overview`, `GET /api/users`, `GET /api/roles`, `GET /api/demo/reports`, dan `GET /api/demo/settings`. Semua endpoint data memakai decorator `@protected`.

Login tersedia di `POST /api/auth/login`; logout tersedia di `POST /api/auth/logout`. Tombol **Keluar** di sidebar memanggil endpoint logout, menghapus token browser, lalu kembali ke halaman login. Token Bearer yang logout dicatat sebagai revoked di tabel `revoked_tokens`, jadi jalankan migration upgrade setelah perubahan model auth.

## Perubahan model dan migration

Setelah menambah atau mengubah model, pastikan model diimpor oleh app factory supaya Flask-Migrate menemukannya. Buat revision lalu terapkan ke database:

```console
flask --app main db migrate -m "describe schema change"
flask --app main db upgrade
```

Periksa file baru di `migrations/versions/` sebelum menjalankan upgrade. Jangan jalankan `db init` lagi setelah folder migration sudah diinisialisasi.

### Contoh membuat model

1. Buat package dan file model, misalnya `modules/task/task_model.py`:

   ```python
   from core.extensions import db


   class Task(db.Model):
       __tablename__ = "tasks"

       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(150), nullable=False)
       is_done = db.Column(db.Boolean, nullable=False, default=False)
   ```

2. Ekspor model dari `modules/task/__init__.py`, mengikuti pola `modules/user/__init__.py` yang mengekspor `User` dan `Role`:

   ```python
   from modules.task.task_model import Task

   __all__ = ["Task"]
   ```

   Untuk beberapa model, impor semuanya dan cantumkan di `__all__`:

   ```python
   from modules.task.task_model import Task
   from modules.task.task_label_model import TaskLabel

   __all__ = ["Task", "TaskLabel"]
   ```

3. Import model dari package di `core/__init__.py` agar masuk ke metadata SQLAlchemy:

   ```python
   from modules.task import Task  # noqa: F401
   ```

Lalu jalankan `flask --app main db migrate -m "add tasks"` dan `flask --app main db upgrade`.

### Database yang sudah dibuat sebelumnya

Jika database masih berisi tabel dari versi auto-bootstrap lama, jalankan `migrate` terhadap database tersebut lalu periksa revision yang dihasilkan sebelum `upgrade`. Revision seharusnya hanya menambahkan schema yang belum ada, misalnya tabel `revoked_tokens` untuk logout. Jangan jalankan revision yang mencoba membuat ulang tabel yang sudah ada. Untuk database lama yang tidak memiliki tabel `revoked_tokens`, jalankan `upgrade` agar tabel itu dibuat dan logout Bearer token dapat bekerja.

## Database selain SQLite

Buat database server terlebih dahulu, pasang driver Python yang sesuai, lalu atur `DATABASE_URL` di `.env`. Contoh PostgreSQL dengan Psycopg 3:

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE_NAME
```

Jalankan migration `upgrade` sebelum `python seed_super.py`. Seeder memasukkan data ke tabel yang sudah ada dan tidak membuat database server maupun tabel.

## Struktur singkat

- `core/` — app factory, konfigurasi, extension, registrasi blueprint
- `common/` — helper bersama, termasuk `@protected`
- `modules/auth/`, `modules/user/`, `modules/dashboard/` — API dan logika fitur
- `modules/web/templates/` — halaman dan komponen reusable Jinja
- `modules/web/static/` — Tailwind dan CSS
