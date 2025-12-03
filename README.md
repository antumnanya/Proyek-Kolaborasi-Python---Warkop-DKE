# Proyek Kolaborasi Python Warkop DKE
**SELAMAT DATANG DI PROYEK KOLABORASI PYTHON WARKOP DKE**

# Anggota Kolaborasi:

**1. Excellentio Potalangi - 250211060003**  ([potalangiexcel-da](https://github.com/potalangiexcel-da))

**2. Kobar Pontolondo - 250211060041**  ([antumnanya](https://github.com/antumnanya))

**3. Gideon Pangemanan - 250211060059**  ([gideonridel](https://github.com/gideonridel))

# Pembuatan Aplikasi Minesweeper
## Deskripsi Proyek
Program yang kami buat merupakan replika dari permainan komputer ***minesweeper*** yang populer di tahun 1990-2000an. Program ini merupakan bentuk kolaborasi 
tim dalam pemrograman game python. Setiap anggota turut mengambil bagian dalam penulisan kode program.

***Minesweeper*** merupakan game logika yang berpadu dengan ketelitian. Di dalam game ini, pemain harus menebak posisi bom yang diletakkan secara
acak dan memilih kotak atau *tile* yang tidak berisi bom. Permainan berakhir apabila pemain bisa memilih semua *tile* kosong (**Menang**), atau ketika 
pemain memilih *tile* yang berisi bom (**Kalah**). Skor pemain dinilai dari seberapa cepat permainan dimenangkan dan disimpan dalam *leaderboard*.

Selain untuk bersenang-senang, game ini juga bisa melatih kecekatan dan ketepatan kemampuan otak dalam mengolah data riil. Ini tentu saja berguna untuk membentuk
kemampuan berpikir kritis yang sangat diperlukan di era digital, terutama di bidang informatika. Untuk itu kelompok kami memilih game ***minesweeper***
sebagai proyek kolaborasi kali ini karena selain menyenangkan, proyek kami bisa membantu untuk melatih kemampuan siswa informatika untuk berpikir kritis.

## Fitur-fitur
 |             Kategori            |           Fitur            | Detail kode | 
|-----------------|-------|-------------|
| Papan & Logika Inti  | Model papan disederhanakan (self.adj)                 | Menggunakan matriks 2D (self.mined dan self.adj) untuk melacak ranjau (-1) dan hitungan ranjau di sekitar (0-8). Logika penempatan ranjau (plant_mines) memastikan klik pertama aman.             
|              | Status permainan: revealed, flagged, questioned, running              | Diimplementasikan melalui matriks Boolean: self.hidden, self.flagged, self.questioned. Status utama dikontrol oleh self.game_over dan self.paused.             
|          | Pengungkapan Sel (Flood Fill)                  | Fungsi reveal(r, c) menangani logika rekursif untuk mengungkapkan sel kosong (nilai 0) dan semua tetangganya secara otomatis hingga batas sel bernomor.                
|           | Penampilan Angka Berwarna                  | Menggunakan dictionary COLOR_MAP untuk memberikan warna khusus (biru, hijau, merah, dll.) pada tombol yang menampilkan angka ranjau di sekitarnya.   
|    Kontrol & UI       |  Menu Tingkat Kesulitan                 | Menggunakan tk.Radiobutton untuk Easy, Medium, Hard (DEFAULTS) dan fungsi show_new_game_dialog menggunakan simpledialog untuk input kustom (R,C,M).
|           | Fungsi Pause/Resume                 | Menggunakan self.toggle_pause() untuk menghentikan/melanjutkan timer dan interaksi game.
|           | Replay                 | Tombol Replay memanggil self.new_game() untuk memulai ulang permainan dengan pengaturan kesulitan yang sama. 
|           | Timer                 | Fungsi update_timer() menggunakan time.time() dan self.master.after() untuk melacak waktu bermain dalam detik. 
| Persistensi Data  | Pencatatan Highscore                | Fungsi save_highscore(t) menyimpan waktu terbaik ke dalam mines_highscores.json dan memuatnya kembali melalui load_highscores(). Hanya 5 skor terbaik per kesulitan yang disimpan.

## Panduan Instalasi
Sebelum menjalankan program ini, pastikan sudah menginstall beberapa program berikut:
  | **Requirements** | **Fungsi** | **Link Download** |
|-------------------|------------------|-----------------|
| Python | Untuk menjalankan file python dan memuat *library* yang digunakan digunakan dalam program | https://www.python.org/ftp/python/pymanager/python-manager-25.0.msix |
| Git | Untuk *cloning repository* dan menjalankan program lewat terminal/*bash* | https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe |

### *Cloning repository*
1. Salin link repositori proyek ini: https://github.com/antumnanya/Proyek-Kolaborasi-Python---Warkop-DKE.git
2. Buka terminal dan pilih folder yang akan dijadikan tempat kloning repositori
```bash
  cd "[direktori folder yang ingin digunakan]"
```
  > contoh direktori folder: cd "D:/Pengenalan Pemrograman/Repository Github
3. Salin repositori program ke dalam folder menggunakan fungsi '**git clone**'
```bash
  git clone https://github.com/antumnanya/Proyek-Kolaborasi-Python---Warkop-DKE.git
```

## Menjalankan file program
1. Buka terminal dan pilih direktori folder yang berisi repositori
```bash
  cd "[direktori folder sebelumnya]
```
2. Pilih folder dengan nama yang sama dengan repositori
```bash
  cd Proyek-Kolaborasi-Python---Warkop-DKE
```
3. Jalankan program utama menggunakan fungsi '**python [nama file].py**'
```bash
  python main.py
```
> 'main.py' merupakan file utama untuk menjalankan program kami
4. Selamat Bermain!

## Dokumentasi Teknis(Flowchart)
![photo_2025-12-03_11-40-01](https://github.com/user-attachments/assets/c9238502-7c11-4ba5-92a8-099829f91256)
![2](https://github.com/user-attachments/assets/375dd8db-e022-4a72-a718-349d1ca883df)

### PENJELASAN FLOWCHART
Diagram ini menggambarkan alur kerja program mulai dari inisialisasi game, interaksi pemain (klik), hingga penentuan menang atau kalah.
Berikut adalah penjelasan langkah demi langkah dari alur tersebut:

### 1. Inisialisasi (Bagian Awal)
* **Start & Inisialisasi**: Program dimulai (**Start**), kemudian melakukan **Inisialisasi UI** (menyiapkan antarmuka) dan **Inisialisasi Game** (memuat konfigurasi, skor tertinggi, dll).
* **New Game**: Permainan baru dimulai.

### 2. Loop Utama & Input Pengguna
Disini program menunggu aksi dari pemain (**User Input**). Ada tiga cabang aksi yang bisa dilakukan pemain:
* **Klik Kanan (Toggle Flag)**: Pemain menandai kotak yang dicurigai berisi bom dengan bendera. Setelah itu, alur kembali menunggu input user.
* **Tombol Pause**: Pemain menjeda permainan. Setelah selesai, alur kembali menunggu input user.
* **Klik Kiri (Reveal)**: Pemain membuka kotak. Ini adalah aksi utama yang memicu logika permainan selanjutnya.

### 3. Logika "Klik Pertama" (First Click)
Setelah pemain melakukan Klik Kiri, ada pengecekan penting:
* **Klik Pertama?**: Sistem mengecek apakah ini adalah klik pertama dalam sesi permainan tersebut.
    * **YA**: Jika ya, program akan **Plant Mines & Start Timer** (Menanam bom secara acak dan menyalakan waktu). *Catatan: Ini dilakukan setelah klik pertama agar pemain tidak langsung kalah pada klik pertama (fitur keselamatan umum di Minesweeper).*
    * **TIDAK**: Jika bukan klik pertama, langsung lanjut ke proses membuka sel.

### 4. Logika Membuka Sel (Reveal Cell)
Masuk ke gambar kedua, setelah sel dibuka (**Reveal Cell**):
* **Adalah Bom?**: Sistem mengecek apakah kotak yang dibuka berisi bom.
    * **YA (Kalah)**: Jika bom, maka **Game Over** (tampilkan semua bom), lalu masuk ke menu Replay.
    * **TIDAK**: Jika bukan bom, lanjut ke penghitungan angka.

### 5. Logika Angka & Area Kosong (Flood Fill)
* **Hitung Angka**: Sistem menghitung berapa jumlah bom yang ada di 8 kotak sekeliling sel tersebut.
* **Angka 0?**:
    * **YA (Kosong)**: Jika tidak ada bom di sekitar (angka 0), program menjalankan **Flood Fill Rekursif**. Artinya, program akan otomatis membuka semua kotak tetangga yang juga kosong secara berantai. Ini adalah fitur yang membuat area besar terbuka sekaligus.
    * **TIDAK**: Jika ada angka (misal 1, 2, 3), maka hanya kotak itu yang terbuka.

### 6. Cek Kemenangan
Setelah proses membuka kotak selesai (baik satu kotak atau banyak kotak karena flood fill):
* **Cek Menang?**: Sistem mengecek apakah semua kotak non-bom sudah terbuka?
    * **YA (Menang)**: Pemain mendapatkan status **You Win!** dan lanjut ke menu Replay.
    * **TIDAK (Belum)**: Permainan belum selesai. Alur kembali (looping) ke atas, menunggu **User Input** selanjutnya.

### 7. Selesai atau Main Lagi (Replay)
Baik setelah Menang atau Game Over, pemain diberi pilihan:
* **Replay?**:
    * **YA**: Kembali ke blok **New Game**.
    * **TIDAK**: Menuju ke **End** (Keluar dari permainan).

**Ringkasan Singkat:**
Flowchart ini memastikan permainan berjalan adil (tidak kalah di klik pertama), efisien (otomatis membuka area kosong/nol), dan terus berulang (looping) sampai pemain menang atau terkena bom.
