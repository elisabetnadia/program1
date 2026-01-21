"""
Game Dakon (Congkak) - Traditional Indonesian Board Game
Permainan ini adalah versi text-based dari permainan Dakon tradisional
"""

class DakonGame:
    def __init__(self):
        # Inisialisasi board dengan 7 lubang per sisi + 1 gudang per sisi
        # Masing-masing lubang dimulai dengan 7 biji
        self.board_player = [7] * 7 + [0]  # Index 7 adalah gudang pemain
        self.board_opponent = [7] * 7 + [0]  # Index 7 adalah gudang lawan
        self.current_player = 1  # 1 untuk pemain, 2 untuk komputer
        self.move_history = []
        
    def display_board(self):
        """Menampilkan papan permainan"""
        print("\n" + "="*60)
        print("                    PERMAINAN DAKON")
        print("="*60)
        
        # Tampilkan sisi lawan (terbalik)
        print("\n          LAWAN (Komputer)")
        print("    ", end="")
        for i in range(6, -1, -1):
            print(f"[{i}]:{self.board_opponent[i]:2d}  ", end="")
        print()
        
        # Tampilkan gudang
        print(f"  Gudang Lawan: [{self.board_opponent[7]:2d}]", end="")
        print(" " * 28, end="")
        print(f"Gudang Anda: [{self.board_player[7]:2d}]")
        
        # Tampilkan sisi pemain
        print("\n          ANDA (Pemain)")
        print("    ", end="")
        for i in range(7):
            print(f"[{i}]:{self.board_player[i]:2d}  ", end="")
        print("\n")
        print("="*60 + "\n")
        
    def get_valid_moves(self, player):
        """Dapatkan daftar gerakan yang valid"""
        board = self.board_player if player == 1 else self.board_opponent
        valid_moves = []
        
        for i in range(7):  # Hanya lubang 0-6, bukan gudang
            if board[i] > 0:
                valid_moves.append(i)
        
        return valid_moves
    
    def make_move(self, hole, player):
        """Melakukan gerakan pemain"""
        if player == 1:
            board = self.board_player
            opponent_board = self.board_opponent
            is_player_board = True
        else:
            board = self.board_opponent
            opponent_board = self.board_player
            is_player_board = False
        
        # Validasi gerakan
        if hole < 0 or hole >= 7 or board[hole] == 0:
            return False, "Lubang tidak valid atau kosong!"
        
        # Ambil biji dari lubang
        seeds = board[hole]
        board[hole] = 0
        current_hole = hole
        
        # Sebarkan biji
        extra_turn = False
        current_side = "player" if is_player_board else "opponent"
        
        while seeds > 0:
            current_hole += 1
            
            # Jika mencapai gudang
            if current_hole == 8:
                if current_side == "player":
                    board[7] += 1
                    seeds -= 1
                    if seeds == 0:
                        extra_turn = True
                    current_hole = 0
                    current_side = "opponent"
                else:
                    current_hole = 0
                    current_side = "player"
            else:
                if current_side == "player":
                    board[current_hole] += 1
                    seeds -= 1
                else:
                    opponent_board[current_hole] += 1
                    seeds -= 1
        
        self.move_history.append((player, hole))
        return True, extra_turn
    
    def is_game_over(self):
        

        player_empty = all(count == 0 for count in self.board_player[:7])
        opponent_empty = all(count == 0 for count in self.board_opponent[:7])
        return player_empty or opponent_empty
    
    def end_game(self):
        """Akhiri permainan dan kumpulkan sisa biji"""
        # Kumpulkan sisa biji
        for i in range(7):
            self.board_player[7] += self.board_player[i]
            self.board_player[i] = 0
            self.board_opponent[7] += self.board_opponent[i]
            self.board_opponent[i] = 0
    
    def get_winner(self):
        """Tentukan pemenang"""
        player_score = self.board_player[7]
        opponent_score = self.board_opponent[7]
        
        if player_score > opponent_score:
            return 1, player_score, opponent_score
        elif opponent_score > player_score:
            return 2, player_score, opponent_score
        else:
            return 0, player_score, opponent_score
    
    def get_computer_move(self):
        """AI komputer memilih gerakan terbaik (simple strategy)"""
        valid_moves = self.get_valid_moves(2)
        
        if not valid_moves:
            return None
        
        # Strategi sederhana: pilih lubang dengan biji terbanyak
        best_move = max(valid_moves, key=lambda x: self.board_opponent[x])
        return best_move
    
    def play_turn(self, player, move=None):
        """Jalankan satu giliran"""
        if move is None:
            move = self.get_computer_move()
        
        success, extra_turn = self.make_move(move, player)
        
        if success:
            player_name = "Anda" if player == 1 else "Komputer"
            print(f"{player_name} memilih lubang [{move}]")
            return extra_turn
        else:
            print(f"Gerakan tidak valid! {extra_turn}")
            return False
