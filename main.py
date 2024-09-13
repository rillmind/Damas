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
        self.jogador_atual = 'X'

    def criar_tabuleiro(self):
        tabuleiro = [[' ' for _ in range(8)] for _ in range(8)]
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'X'
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'O'
        return tabuleiro

    def mostrar_tabuleiro(self):
        print("  1 2 3 4 5 6 7 8")
        print(" +---------------+")
        for i in range(8):
            print(f"{8 - i}|", end="")
            for j in range(8):
                print(self.tabuleiro[i][j], end=" ")
            print(" ")
        print(" +---------------+")

    def mover_peca(self, linha_inicial, coluna_inicial, linha_final, coluna_final):
        self.tabuleiro[linha_final][coluna_final] = self.tabuleiro[linha_inicial][coluna_inicial]
        self.tabuleiro[linha_inicial][coluna_inicial] = ' '

    def promover_dama(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == 'X' and linha == 0:
            self.tabuleiro[linha][coluna] = 'D'  # 'D' para dama
        elif self.tabuleiro[linha][coluna] == 'O' and linha == 7:
            self.tabuleiro[linha][coluna] = 'D'

    def verificar_movimento(self, linha_inicial, coluna_inicial, linha_final, coluna_final):
        peca = self.tabuleiro[linha_inicial][coluna_inicial]
        if abs(linha_final - linha_inicial) == 1 and abs(coluna_final - coluna_inicial) == 1:
            return self.tabuleiro[linha_final][coluna_final] == ' '  # Movimento simples
        elif abs(linha_final - linha_inicial) == 2 and abs(coluna_final - coluna_inicial) == 2:
            linha_meio = (linha_inicial + linha_final) // 2
            coluna_meio = (coluna_inicial + coluna_final) // 2
            return (self.tabuleiro[linha_final][coluna_final] == ' ' and 
                    self.tabuleiro[linha_meio][coluna_meio] != ' ' and 
                    self.tabuleiro[linha_meio][coluna_meio] != peca)  # Captura

        return False  # Movimento inválido

    def realizar_captura(self, linha_inicial, coluna_inicial, linha_final, coluna_final):
        linha_meio = (linha_inicial + linha_final) // 2
        coluna_meio = (coluna_inicial + coluna_final) // 2
        self.tabuleiro[linha_meio][coluna_meio] = ' '  # Remove a peça capturada

    def checar_vencedor(self):
        x_count = sum(row.count('X') for row in self.tabuleiro) + sum(row.count('D') for row in self.tabuleiro)
        o_count = sum(row.count('O') for row in self.tabuleiro) + sum(row.count('D') for row in self.tabuleiro)

        if x_count == 0:
            return "O venceu!"
        elif o_count == 0:
            return "X venceu!"
        return None

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            print(f"Turno do jogador {self.jogador_atual}")
            jogada = input("Digite a posição da peça (linha coluna) e a posição de destino (linha coluna), ex: 3 4 4 5: ").strip()

            try:
                posicao = list(map(int, jogada.split()))
                if len(posicao) != 4:
                    raise ValueError

                linha_inicial, coluna_inicial, linha_final, coluna_final = posicao
                linha_inicial = 8 - linha_inicial
                coluna_inicial -= 1
                linha_final = 8 - linha_final
                coluna_final -= 1

                if not (0 <= linha_inicial < 8 and 0 <= coluna_inicial < 8 and
                        0 <= linha_final < 8 and 0 <= coluna_final < 8):
                    print("Movimento fora dos limites. Tente novamente.")
                    continue

                if self.verificar_movimento(linha_inicial, coluna_inicial, linha_final, coluna_final):
                    self.mover_peca(linha_inicial, coluna_inicial, linha_final, coluna_final)
                    self.promover_dama(linha_final, coluna_final)

                    if abs(linha_final - linha_inicial) == 2:
                        self.realizar_captura(linha_inicial, coluna_inicial, linha_final, coluna_final)

                    vencedor = self.checar_vencedor()
                    if vencedor:
                        self.mostrar_tabuleiro()
                        print(vencedor)
                        break
                    
                    # Trocar o jogador
                    self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
                else:
                    print("Movimento inválido. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Utilize o formato 'linha coluna linha coluna'.")

if __name__ == "__main__":
    jogo = Damas()
    jogo.jogar()

