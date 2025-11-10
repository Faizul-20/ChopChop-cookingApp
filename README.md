
# 📁 Panduan Struktur Folder Proyek Flask

Dokumen ini berfungsi sebagai **panduan resmi** bagi developer yang terlibat dalam proyek Flask ini.  
Tujuannya adalah menjaga **konsistensi, keteraturan, dan kemudahan pengelolaan kode** di seluruh tim.

---

## 🏗️ Struktur Folder Standar

```
Cooking_Dash/
│
├── app/
│   ├── __init__.py        # Inisialisasi Flask app dan registrasi blueprint
│   ├── routes.py          # Definisi route / endpoint utama aplikasi
│   ├── models.py          # Definisi model database (SQLAlchemy, dll)
│   ├── forms.py           # Form (WTForms) atau validasi input
│   ├── templates/         # File HTML (Jinja2 templates)
│   └── static/            # Asset statis: CSS, JS, gambar
│
├── venv/                  # Virtual environment (jangan di-commit ke git)
├── config.py              # Konfigurasi aplikasi (development, production, dll)
├── requirements.txt       # Daftar dependensi Python
└── run.py                 # Entry point utama aplikasi
```

---

## ⚙️ Aturan Penempatan File dan Kode

### 1. `app/__init__.py`
- Wajib berisi inisialisasi Flask dan konfigurasi utama.
- Contoh:
  ```python
  from flask import Flask

  def create_app():
      app = Flask(__name__)
      app.config.from_object('config')
      
      from app import routes
      return app
  ```

### 2. `app/routes.py`
- Tempatkan semua **route / endpoint** di sini.
- Gunakan *blueprint* jika aplikasi membesar.
- Contoh:
  ```python
  from flask import render_template
  from app import app

  @app.route('/')
  def home():
      return render_template('index.html')
  ```

### 3. `app/models.py`
- Simpan seluruh **model database** di sini.
- Jika model makin banyak, buat subfolder `models/`.

### 4. `app/forms.py`
- Digunakan untuk validasi input menggunakan WTForms.

### 5. `app/templates/` dan `app/static/`
- `templates/` untuk HTML (Jinja2).
- `static/` untuk CSS, JS, dan gambar.

### 6. `config.py`
- Simpan semua konfigurasi environment di sini.
- Contoh:
  ```python
  class Config:
      DEBUG = True
      SECRET_KEY = 'secret_key_here'
  ```

### 7. `run.py`
- Titik masuk utama aplikasi.
- Contoh:
  ```python
  from app import create_app

  app = create_app()

  if __name__ == '__main__':
      app.run(debug=True)
  ```

---

## 🧹 Aturan Umum

1. **Jangan simpan file Python di luar folder `app/` kecuali `run.py`, `config.py`, dan `requirements.txt`.**
2. **Selalu aktifkan virtual environment (`venv`) sebelum menjalankan proyek.**
3. **Gunakan `requirements.txt` untuk setiap dependensi baru:**  
   ```bash
   pip freeze > requirements.txt
   ```
4. **Gunakan format penulisan PEP8.**
5. **Gunakan blueprint jika fitur baru punya route sendiri.**
6. **Jangan ubah struktur tanpa diskusi dengan lead developer.**

---

<br>
<br>
<br>

# 🚀 Alur Git & Push ke GitHub
---
# 1. Cek branch yang sedang aktif

```bash

git branch
```
- Branch aktif ditandai dengan *.

- Pastikan berada di branch yang tepat sebelum mulai kerja (misal dev atau feature branch).
---
# 2. Buat branch feature baru (dari dev)
```bash
git checkout dev
git pull                # update branch dev terbaru
git checkout -b feature/nama-fitur
```
### Contoh :
```bash
git checkout -b feature/generate-recipe
```
---
# 3. Kerjakan fitur dan commit perubahan

```bash
git add .
git commit -m "Tambah fitur generate resep otomatis"
```
Gunakan pesan commit deskriptif dan jelas.

---
# 4. Push branch ke GitHub
```bash
git push -u origin feature/nama-fitur
```

---
# 5. Merge branch feature ke dev
### Setelah fitur selesai dan diuji:

```bash
git checkout dev
git pull
git merge feature/nama-fitur
git push
```

---
# 6. Merge dev ke main (release)
### Setelah semua fitur di dev siap rilis:
```bash
git checkout main
git pull
git merge dev
git push
```
---
# 7. Hapus branch feature (opsional)
```bash
git branch -d feature/nama-fitur       # hapus lokal
git push origin --delete feature/nama-fitur  # hapus remote
```
## 🧭 Tujuan Akhir

Dengan struktur dan aturan ini, setiap developer dapat:
- Memahami alur proyek tanpa kebingungan.  
- Menambahkan fitur baru tanpa mengacaukan struktur lama.  
- Menjaga konsistensi antar branch dan tim. 

_**Dokumen ini wajib dibaca sebelum memulai kontribusi ke proyek Flask ini.**_
# ChopChop-cookingApp

