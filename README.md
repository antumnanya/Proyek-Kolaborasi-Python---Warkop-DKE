# Proyek Kolaborasi Python Warkop DKE
**SELAMAT DATANG DI PROYEK KOLABORASI PYTHON WARKOP DKE**

## Anggota Kolaborasi:

**1. Excellentio Potalangi - 250211060003**  ([potalangiexcel-da](https://github.com/potalangiexcel-da))

**2. Kobar Pontolondo - 250211060041**  ([antumnanya](https://github.com/antumnanya))

**3. Gideon Pangemanan - 250211060059**  ([gideonridel](https://github.com/gideonridel))

## Deskripsi PROYEK
Proyek ini adalah kolaborasi dari anggota kelompok yang berupa pembuatan game **minesweeper** dengan menggunakkan pemrogramman python

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
