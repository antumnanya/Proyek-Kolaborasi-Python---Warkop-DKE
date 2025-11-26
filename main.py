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

import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time
import json
import os
import threading

# ---------------- Config ----------------
HIGHSCORE_FILE = 'mines_highscores.json'
DEFAULTS = {
    'Easy': (9, 9, 10),
    'Medium': (16, 16, 40),
    'Hard': (16, 30, 99)
}

ICONS = {
    'bomb': '💣',
    'flag': '🚩',
    'hidden': '■',
    'question': '?'
}

COLOR_MAP = {
    1: "#0000FF",   # biru
    2: "#008000",   # hijau
    3: "#FF0000",   # merah
    4: "#000080",   # biru navy
    5: "#800000",   # maroon
    6: "#008080",   # teal
    7: "#000000",   # hitam
    8: "#808080",   # abu
}
