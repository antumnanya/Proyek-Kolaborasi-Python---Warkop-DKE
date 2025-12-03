# Proyek Kolaborasi Python Warkop DKE
**SELAMAT DATANG DI PROYEK KOLABORASI PYTHON WARKOP DKE**

## Anggota Kolaborasi:

**1. Excellentio Potalangi - 250211060003**  ([potalangiexcel-da](https://github.com/potalangiexcel-da))

**2. Kobar Pontolondo - 250211060041**  ([antumnanya](https://github.com/antumnanya))

**3. Gideon Pangemanan - 250211060059**  ([gideonridel](https://github.com/gideonridel))

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

