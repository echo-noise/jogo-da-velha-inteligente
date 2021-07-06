class Tabuleiro(object):
    def __init__(self):
        self.casas = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.rodadas = 0
        self.velhas = 0
    
    def reset(self):
        self.casas = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
                     ]
        self.rodadas = 0

    def esta_vazio(self, coordenada, matriz):
        linha = coordenada[0]
        coluna = coordenada[1]
        if matriz[linha][coluna] == 0:
            return True
        return False

    def preencher(self, jogador, linha, coluna):
        if self.casas[linha][coluna] == 0:
            self.casas[linha][coluna] = jogador
            return True
        else:
            return False
    
    def rodar(self):
        self.rodadas += 1

    def checar_velha(self):
        zeros = []

        for linha in self.casas:
            if 0 in linha:
                zeros.append(True)
            else:
                zeros.append(False)

        if True not in zeros:
            print("FIM DE JOGO - DEU VELHA")
            self.velhas += 1
            return True
        else:
            return False

    def checar_linha(self, linha):
        if 0 in linha or not(linha[0] == linha[1] == linha[2]):
            return False
        else:
            return True

    def checar_matriz(self, matriz):
        for linha in matriz:
            if self.checar_linha(linha):
                return True

    # converte as 3 colunas para linhas juntas em uma matriz 3x3 
    def checar_colunas(self):
        lista_aux = [[0,0,0], [0,0,0], [0,0,0]]

        for i in range(0,3):
            for j in range(3):
                lista_aux[j][i] = self.casas[i][j]
        return self.checar_matriz(lista_aux)

    # converte as diagonais em linhas 
    def checar_diagonais(self):
        lista_aux = [0,0,0]
        matriz = []

        for i in range(3):
            lista_aux[i] = self.casas[i][i]

        matriz.append(lista_aux)
        lista_aux = [0, 0, 0]
        j = 0

        for i in range(2, -1, -1):
            lista_aux[j] = self.casas[i][j]
            j += 1

        matriz.append(lista_aux)

        return self.checar_matriz(matriz)

    def checar_vitoria(self):
        if self.checar_matriz(self.casas) or self.checar_colunas() or self.checar_diagonais():
            return True
        else:
            return False

    def imprimir(self):
        self.rodar()
        for x, linha in enumerate(self.casas):
            for i, item in enumerate(linha):
                if not item:
                    print("  ", end=" ")
                else:
                    print(" " + str(item), end=" ")

                if i == 0 or i == 1:
                    print("|", end="")
            print("")
            if x == 0 or x == 1:
                print("———|———|———")




    