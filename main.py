class Damas:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.jogador_atual = 'X'

    def criar_tabuleiro(self):
        tabuleiro = [[' ' for _ in range(8)] for _ in range(8)]
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'O'
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 != 0:
                    tabuleiro[i][j] = 'X'
        return tabuleiro

    def mostrar_tabuleiro(self):
        print("  1 2 3 4 5 6 7 8")
        print(" +---------------+")
        for i in range(8):
            print(f"{8 - i} ", end="")
            for j in range(8):
                print(self.tabuleiro[i][j], end=" ")
            print(" ")
        print(" +---------------+")

    def mover_peca(self, linha_inicial, coluna_inicial, linha_final, coluna_final):
        self.tabuleiro[linha_final][coluna_final] = self.tabuleiro[linha_inicial][coluna_inicial]
        self.tabuleiro[linha_inicial][coluna_inicial] = ' '

    def promover_dama(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == 'O' and linha == 7:  # X atinge a última linha do oponente
            self.tabuleiro[linha][coluna] = 'Q'  # Dama de X
        elif self.tabuleiro[linha][coluna] == 'X' and linha == 0:  # O atinge a última linha do oponente
            self.tabuleiro[linha][coluna] = 'K'  # Dama de O

    def verificar_movimento(self, linha_inicial, coluna_inicial, linha_final, coluna_final):
        peca = self.tabuleiro[linha_inicial][coluna_inicial]

        if peca == 'K' or peca == 'Q':
            # Movimento diagonal para a dama
            if abs(linha_final - linha_inicial) == abs(coluna_final - coluna_inicial):
                i, j = linha_inicial, coluna_inicial
                direcao_linha = 1 if linha_final > linha_inicial else -1
                direcao_coluna = 1 if coluna_final > coluna_inicial else -1
                i += direcao_linha
                j += direcao_coluna

                # Verificando se há peças a serem capturadas
                while i != linha_final and j != coluna_final:
                    if self.tabuleiro[i][j] != ' ':
                        # Se houver peça inimiga no caminho
                        if self.tabuleiro[i][j] != peca:  # Verifique se não é a mesma peça
                            # Verifique se a casa final está vazia para capturar
                            if self.tabuleiro[linha_final][coluna_final] == ' ':
                                return True  # Movimento de captura
                        return False  # Se houver uma peça própria ou uma peça inimiga no caminho
                    i += direcao_linha
                    j += direcao_coluna

                # A dama pode se mover livremente para uma casa vazia
                return self.tabuleiro[linha_final][coluna_final] == ' '

        else:
            # Movimentos normais
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
        peca = self.tabuleiro[linha_inicial][coluna_inicial]
        direcao_linha = 1 if linha_final > linha_inicial else -1
        direcao_coluna = 1 if coluna_final > coluna_inicial else -1

        # Captura múltipla para dama
        i, j = linha_inicial + direcao_linha, coluna_inicial + direcao_coluna
        while i != linha_final and j != coluna_final:
            if self.tabuleiro[i][j] != ' ' and self.tabuleiro[i][j] != peca:
                self.tabuleiro[i][j] = ' '  # Captura a peça
            i += direcao_linha
            j += direcao_coluna

    def checar_vencedor(self):
        x_count = sum(row.count('X') for row in self.tabuleiro) + sum(row.count('K') for row in self.tabuleiro)
        o_count = sum(row.count('O') for row in self.tabuleiro) + sum(row.count('Q') for row in self.tabuleiro)

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

                    # Realizar captura
                    if abs(linha_final - linha_inicial) > 1:  # Captura
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

jogo = Damas()
jogo.jogar()

