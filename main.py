import logging
import random

# tipos de jogadores
MANUAL = 0
ALEATORIO = 1

#logging.basicConfig(format="%(levelname)s>%(funcName)s: %(message)s", level=logging.DEBUG)

class Jogador(object):
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo

    def jogar(self, tabuleiro):
        logging.info("funcao iniciada")
        print(self.nome)
        sucesso = False

        while not sucesso:
            if self.tipo == MANUAL:
                linha = int(input("Linha>")) - 1
                coluna = int(input("coluna>")) - 1
            elif self.tipo == ALEATORIO:
                linha = random.randint(0,2)
                coluna = random.randint(0,2)

            sucesso = tabuleiro.preencher(self.codigo, linha, coluna)
            
            if not sucesso and self.tipo == MANUAL:
                print("ja jogou nesta posicao")
            elif not sucesso:
                logging.info("maquina jogou em uma posição ocupada, tentando de novo")
        
        logging.info("jogada finalizada....")
        tabuleiro.imprimir()
        if tabuleiro.checar_vitoria():
            print(self.nome + " GANHOU")
            return True
        return False 

    def jogar_aleatorio(self, tabuleiro):
        logging.info("funcao iniciada")
        print(self.nome)

class Tabuleiro(object):
    def __init__(self):
        super().__init__()
        # casas do tabuleiro
        self.casas = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
                    
    def preencher(self, jogador, linha, coluna):
        if self.casas[linha][coluna] == 0:
            self.casas[linha][coluna] = jogador
            return True
        else:
            return False

    def checar_velha(self):
        logging.info("função iniciada")
        zeros = []

        for linha in self.casas:
            if 0 in linha:
                zeros.append(True)
            else:
                zeros.append(False)

        logging.debug("lista de zeros" + str(zeros))

        if True not in zeros:
            print("FIM DE JOGO - DEU VELHA")
            return True
        else:
            return False

    # checa uma unica linha
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
        logging.info("funcao iniciada")
        lista_aux = [[0,0,0], [0,0,0], [0,0,0]]

        for i in range(0,3):
            for j in range(3):
                lista_aux[j][i] = self.casas[i][j]
        return self.checar_matriz(lista_aux)

    # converte as diagonais em linhas 
    def checar_diagonais(self):
        logging.info("funcao iniciada")
        lista_aux = [0,0,0]
        matriz = []

        for i in range(3):
            lista_aux[i] = self.casas[i][i]

        matriz.append(lista_aux)

        logging.debug("diagonal1=" + str(lista_aux))
        logging.debug("estado da matriz: " + str(matriz))
        logging.info("processando segunda diagonal")

        lista_aux = [0, 0, 0]
        j = 0

        for i in range(2, -1, -1):
            logging.debug("j=" + str(j))
            lista_aux[j] = self.casas[i][j]
            logging.debug("i=" + str(i))
            logging.debug("valor=" + str(lista_aux[j]))
            logging.debug("listaaux dentro do loop=" + str(lista_aux))
            j += 1

        matriz.append(lista_aux)
        logging.debug("diagonal2=" + str(lista_aux))
        logging.debug("estado da matriz" + str(matriz))

        return self.checar_matriz(matriz)

    def checar_vitoria(self):
        logging.info("funcao iniciada ----------------")

        if self.checar_matriz(self.casas) or self.checar_colunas() or self.checar_diagonais():
            return True
        else:
            return False

    def imprimir(self):
        for linha in self.casas:
            print(linha)

class Main(object):
    def __init__(self):
        super().__init__()
        self.tabuleiro = Tabuleiro()
        self.jogador1 = Jogador(1, "JOGADOR 1", MANUAL)
        self.jogador2 = Jogador(-1, "MAQUINA", ALEATORIO)
        self.fim = False

    def mainloop(self):
        self.tabuleiro.imprimir()
        while not self.fim: 
            self.fim = self.jogador1.jogar(self.tabuleiro)

            if self.fim:
                break
            else:
                logging.debug("jogador1 não ganhou, checando velha...")
                self.fim = self.tabuleiro.checar_velha()

                if self.fim:
                    break
                else:
                    logging.debug("vez do jogador 2...")
                    self.fim = self.jogador2.jogar(self.tabuleiro)

                    if self.fim:
                        break
                    else:
                        logging.debug("ninguem ganhou, procurando velha!")
                        self.fim = self.tabuleiro.checar_velha()

random.seed()
main = Main()
main.mainloop()

    


