"""
Game Minesweeper 

Fitur:
- Model papan disederhanakan menggunakan `self.board` 
  (nilai -1 untuk ranjau, dan angka ≥ 0 untuk jumlah ranjau di sekitar).
- Variabel status permainan: `self.revealed`, `self.flagged`, 
  `self.questioned`, dan `self.running`.
- Penampilan angka berwarna menggunakan `COLOR_MAP`.
- Fitur jumpscare dengan peluang acak yang dapat dikonfigurasi.
- Menu tingkat kesulitan (Easy, Medium, Hard) serta opsi kustom 
  melalui dialog input.
- Fungsi Pause/Resume, Replay, dan pencatatan Highscore 
  (disimpan dalam berkas JSON lokal).

"""
