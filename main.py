# t0 = [".", ".", ".", ".", ".", ".", ".", "."]
# t1 = t0[:]
# t2 = t0[:]
# t3 = t0[:]
# t4 = t0[:]
# t5 = t0[:]
# t6 = t0[:]
# t7 = t0[:]
# t8 = [t0, t1, t2, t3, t4, t5, t6, t7]

#     print(' ')
#     for c2 in c:
# for c in t8:
#         print(c2, end=' ')

# print()

tabuleiroj = [["." for _ in range(8)] for _ in range(8)]

def mostrar_tabuleiro():
    print("  A B C D E F G H")
    number = 1
    for linha in tabuleiroj:
        print(number, end=" ")
        print(" ".join(linha))
        number += 1

class Damas:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.current_player = 'X'  # 'X' para Jogador 1 e 'O' para Jogador 2

    def criar_tabuleiro(self):
        # Cria um tabuleiro 8x8 com peças iniciais
        tabuleiro = [[' ' if (i + j) % 2 == 0 else '.' for j in range(8)] for i in range(8)]
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'X'  # Jogador 1
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'O'  # Jogador 2
        return tabuleiro

    def display_board(self):
        print("  A B C D E F G H")
        print(" +----------------+")
        for i in range(8):
            print(f"{1 + i}  ", end="")  # Exibe a numeração ao lado
            for j in range(8):
                print(self.tabuleiro[i][j], end=" ")
            print(" ")
        print(" +----------------+")

    def is_valid_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.tabuleiro[start_row][start_col]

        if self.tabuleiro[end_row][end_col] != ' ':
            return False  # Casa de destino não está vazia

        # Movimento simples
        if piece == 'X':
            if end_row == start_row - 1 and abs(end_col - start_col) == 1:
                return True  # Movimento simples para frente
        elif piece == 'O':
            if end_row == start_row + 1 and abs(end_col - start_col) == 1:
                return True  # Movimento simples para frente

        # Captura
        if piece == 'X' and start_row > 1:
            if (end_row == start_row - 2 and abs(end_col - start_col) == 2 and
                self.tabuleiro[start_row - 1][(start_col + end_col) // 2] == 'O'):
                return True  # Captura para cima
        elif piece == 'O' and start_row < 6:
            if (end_row == start_row + 2 and abs(end_col - start_col) == 2 and
                self.tabuleiro[start_row + 1][(start_col + end_col) // 2] == 'X'):
                return True  # Captura para baixo

        return False

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.tabuleiro[start_row][start_col]

        self.tabuleiro[end_row][end_col] = piece
        self.tabuleiro[start_row][start_col] = ' '

        # Verificar captura
        if abs(end_row - start_row) == 2:
            middle_row = (start_row + end_row) // 2
            middle_col = (start_col + end_col) // 2
            self.tabuleiro[middle_row][middle_col] = ' '  # Remove a peça capturada

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        x_count = sum(row.count('X') for row in self.tabuleiro)
        o_count = sum(row.count('O') for row in self.tabuleiro)

        if x_count == 0:
            return "O venceu!"
        elif o_count == 0:
            return "X venceu!"
        return None

    def play(self):
        while True:
            self.display_board()
            print(f"Turno do jogador {self.current_player}")
            move = input("Digite o movimento (ex: A3 B4): ").strip()
            try:
                start_pos, end_pos = move.split()
                start_row = 8 - int(start_pos[1])  # Ajuste para a numeração
                start_col = ord(start_pos[0].upper()) - ord('A')
                end_row = 8 - int(end_pos[1])  # Ajuste para a numeração
                end_col = ord(end_pos[0].upper()) - ord('A')

                if self.is_valid_move((start_row, start_col), (end_row, end_col)):
                    self.move_piece((start_row, start_col), (end_row, end_col))
                    winner = self.check_winner()
                    if winner:
                        self.display_board()
                        print(winner)
                        break
                    self.switch_player()
                else:
                    print("Movimento inválido. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Utilize o formato A1 B2.")

if __name__ == "__main__":
    game = Damas()
    game.play()
