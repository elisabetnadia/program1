# Game Dakon (Congkak)

Permainan Dakon adalah game papan tradisional yang berasal dari Indonesia dan Malaysia. Game ini juga dikenal dengan nama Congkak atau Congklak.

## 📋 Cara Bermain

### Setup
- Setiap pemain memiliki 7 lubang berukuran kecil dan 1 gudang (lubang besar) di sebelah kanannya
- Setiap lubang kecil dimulai dengan 7 biji
- Gudang dimulai dengan 0 biji

### Aturan Permainan
1. **Pemilihan Lubang**: Pilih salah satu lubang dari 7 lubang Anda (bernomor 0-6)
2. **Penyebaran Biji**: Ambil semua biji dari lubang yang dipilih, kemudian sebarkan satu per satu ke lubang-lubang di sebelahnya searah jarum jam
3. **Gudang**: Jika biji Anda masuk ke gudang Anda sendiri, Anda dapat giliran lagi
4. **Blokade**: Jika biji terakhir masuk ke gudang lawan, giliran beralih ke lawan
5. **Akhir Permainan**: Permainan berakhir ketika salah satu sisi pemain (7 lubang) kosong semua
6. **Pemenang**: Pemain dengan biji terbanyak di gudang adalah pemenang

## 🎮 Cara Menjalankan

### Prasyarat
- Python 3.6 atau lebih tinggi

### Jalankan Game
```bash
python main.py
```

## 📁 Struktur File

- `game.py` - Kelas utama `DakonGame` yang mengimplementasikan logika permainan
- `main.py` - Interface dan loop permainan
- `README.md` - File dokumentasi (file ini)

## 🎯 Fitur Game

✅ Permainan lengkap dengan aturan Dakon yang benar
✅ AI komputer dengan strategi sederhana
✅ Interface text-based yang user-friendly
✅ Sistem scoring otomatis
✅ Kemampuan bermain ulang
✅ Validasi input yang baik

## 🤖 Strategi AI

Komputer menggunakan strategi sederhana:
- Memilih lubang dengan jumlah biji terbanyak
- Strategi ini dapat dikembangkan lebih lanjut untuk AI yang lebih cerdas

## 💡 Pengembangan Lebih Lanjut

Fitur-fitur yang bisa ditambahkan:
- Graphical User Interface (GUI)
- Multiplayer online
- AI dengan minimax algorithm
- Leaderboard dan statistik
- Berbagai level kesulitan

## 📝 Lisensi

Permainan ini dibuat untuk tujuan pembelajaran.

Selamat bermain! 🎉
