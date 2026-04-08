# 🚀 Colab Drive Downloader (Aria2 Edition)

Script sederhana, super cepat, dan anti-putus untuk mendownload file berukuran raksasa (bergiga-giga) langsung ke Google Drive menggunakan Google Colab.

Pernah ngalamin download file 4 GB ke Google Drive tapi mentok dan suksesnya cuma 400 MB doang? Script ini adalah solusinya! Kita menggunakan **Aria2** yang memecah file jadi banyak jalur dan punya fitur auto-resume.

## ✨ Fitur Unggulan
* ⚡ **Super Ngebut:** Menggunakan 16 jalur koneksi secara bersamaan (menembus limitasi server).
* 🛡️ **Auto-Resume (Anti-Gagal):** Kalau proses terputus di tengah jalan, tinggal jalankan ulang kodenya, dan download akan dilanjutkan dari titik terakhir (tidak mengulang dari 0%).
* 💾 **Direct to Drive:** File langsung masuk ke Google Drive tanpa numpang di penyimpanan internal HP atau Laptop kamu.
* 👶 **Ramah Pemula:** Sangat mudah digunakan, cukup _copy-paste_ dan jalankan.

---

## 🛠️ Persiapan Awal
1. Pastikan kamu punya akun Google dan sisa kapasitas Google Drive yang cukup untuk menampung file yang mau didownload.
2. Buka [Google Colab](https://colab.research.google.com/) dan buat **Notebook Baru** (*New Notebook*).

---

## 📖 Cara Penggunaan (Tutorial Lengkap)

Ikuti langkah-langkah di bawah ini secara berurutan. Taruh masing-masing kode di **Sel (Cell) Kode** yang berbeda di Google Colab.

### Langkah 1: Sambungkan Google Drive
Pertama, kita harus memberi akses Google Colab ke Google Drive kamu. Jalankan kode ini:

```python
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```
*(Nanti akan muncul pop-up dari Google, klik **"Allow" / "Izinkan"**)*.

### Langkah 2: Install Mesin Download (Aria2)
Karena kita mau pakai download manager kelas berat, kita perlu install Aria2 di sistem Colab. Jalankan kode ini:

```python
!apt-get install aria2 -y
```

### Langkah 3: Eksekusi Download
Ini adalah langkah terakhir. Masukkan link download dan tentukan nama filenya di sini.

```python
# 1. Masuk ke folder utama Google Drive
%cd /content/drive/MyDrive/

# 2. GANTI BAGIAN INI DENGAN LINK DAN NAMA FILE KAMU
LINK = "PASTE_LINK_DOWNLOAD_DI_SINI"
NAMA_FILE = "nama_file_kamu.iso" 

# 3. Mulai download ngebut dengan Aria2 (16 koneksi + Auto Resume)
!aria2c -x 16 -s 16 -c "$LINK" -o "$NAMA_FILE"
```
*(Jangan lupa pertahankan tanda kutip `"` pada bagian link dan nama file ya!)*

---

## 💡 Troubleshooting & FAQ (Tanya Jawab)

**Q: Kok prosesnya tiba-tiba berhenti atau koneksinya putus?**
A: Tenang, itu biasa terjadi kalau filenya sangat besar dan server sumber membatasi waktu. Cukup jalankan ulang kode di **Langkah 3**. Aria2 akan membaca file yang setengah jadi dan melanjutkannya secara otomatis berkat fitur `-c` (continue).

**Q: Saya mau simpan di dalam folder khusus di Drive, bukan di halaman depan. Caranya?**
A: Ganti kode baris pertama di **Langkah 3** menjadi `%cd /content/drive/MyDrive/NamaFolderKamu`. Pastikan foldernya sudah kamu buat dulu di Google Drive ya.

**Q: Muncul error "No such file or directory"?**
A: Biasanya karena Google Drive kamu belum tersambung dengan benar. Coba klik menu **Runtime** > **Restart session** di bagian atas Colab, lalu jalankan lagi mulai dari Langkah 1.

---

## 🤝 Kontribusi
Punya ide untuk bikin script ini lebih canggih? Silakan *fork* repository ini dan buat *Pull Request*. Semua kontribusi sangat dihargai!
