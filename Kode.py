# 1. Masuk ke folder Google Drive kamu
%cd /content/drive/MyDrive/

# 2. Setup link dan nama file
LINK = "PASTE_LINK_DOWNLOAD_DISINI"
NAMA_FILE = "file_baru_gua.iso"

# 3. Eksekusi download dengan Aria2 (16 koneksi + Auto-Resume)
!aria2c -x 16 -s 16 -c "$LINK" -o "$NAMA_FILE"
