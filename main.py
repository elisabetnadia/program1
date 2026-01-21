"""
Main file untuk menjalankan Game Dakon
"""

from game import DakonGame

def main():
    print("\n" + "="*60)
    print("   SELAMAT DATANG DI PERMAINAN DAKON (CONGKAK)")
    print("="*60)
    print("\nAturan Dakon:")
    print("1. Setiap pemain punya 7 lubang + 1 gudang")
    print("2. Setiap lubang dimulai dengan 7 biji")
    print("3. Pilih lubang, sebarkan biji searah jarum jam")
    print("4. Jika biji terakhir masuk gudang Anda, dapat giliran lagi")
    print("5. Permainan berakhir saat satu sisi habis")
    print("6. Pemenang yang paling banyak biji di gudang")
    print("\n" + "="*60 + "\n")
    
    # Inisialisasi game
    game = DakonGame()
    
    # Permainan utama
    while True:
        game.display_board()
        
        if game.is_game_over():
            print("\n" + "="*60)
            print("PERMAINAN BERAKHIR!")
            print("="*60)
            
            game.end_game()
            winner, player_score, opponent_score = game.get_winner()
            
            print(f"\nSkor Akhir:")
            print(f"  Anda       : {player_score} biji")
            print(f"  Komputer   : {opponent_score} biji")
            
            if winner == 1:
                print(f"\n🎉 ANDA MENANG! 🎉")
            elif winner == 2:
                print(f"\n😢 KOMPUTER MENANG! 😢")
            else:
                print(f"\n🤝 SERI! 🤝")
            
            print("="*60 + "\n")
            
            play_again = input("Main lagi? (y/n): ").lower()
            if play_again == 'y':
                game = DakonGame()
                continue
            else:
                print("Terima kasih telah bermain Dakon! Sampai jumpa!")
                break
        
        # Giliran pemain
        print("\n🎮 GILIRAN ANDA")
        valid_moves = game.get_valid_moves(1)
        
        if not valid_moves:
            print("Tidak ada lubang yang bisa dipilih. Giliran ke komputer.")
        else:
            print(f"Lubang yang tersedia: {valid_moves}")
            while True:
                try:
                    choice = int(input("Pilih lubang (0-6): "))
                    if choice in valid_moves:
                        extra_turn = game.play_turn(1, choice)
                        if extra_turn:
                            print("✨ Anda dapat giliran tambahan!")
                        break
                    else:
                        print("❌ Pilihan tidak valid!")
                except ValueError:
                    print("❌ Input harus angka 0-6!")
        
        # Cek apakah permainan sudah berakhir
        if game.is_game_over():
            continue
        
        # Giliran komputer
        print("\n🤖 GILIRAN KOMPUTER")
        input("Tekan Enter untuk melanjutkan...")
        
        extra_turn = True
        while extra_turn:
            move = game.get_computer_move()
            valid_moves = game.get_valid_moves(2)
            
            if not valid_moves:
                print("Komputer tidak punya lubang yang bisa dipilih.")
                extra_turn = False
            else:
                extra_turn = game.play_turn(2, move)
                if extra_turn:
                    print("✨ Komputer dapat giliran tambahan!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPermainan dihentikan. Sampai jumpa!")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
