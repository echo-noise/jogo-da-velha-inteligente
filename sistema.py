import logging
import random
from sys import exit

from cerebro import *

class Jogador(object):
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.cerebro = None
        self.vitorias = 0

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
            elif self.tipo == DIFICIL:
                jogada = self.pensar(tabuleiro)
                
                if jogada == None:
                    logging.error("possibilidade nao preenchida encontrada")
                    logging.debug("caminho do cerebro>" + str(self.cerebro.caminho))
                    exit(1)

                logging.debug("vai jogar em " + str(jogada))

                self.ultima_jogada = jogada
                linha = jogada[0]
                coluna = jogada[1]

            sucesso = tabuleiro.preencher(self.codigo, linha, coluna)

            if not sucesso and self.tipo == MANUAL:
                print("ja jogou nesta posicao")
            elif not sucesso:
                pass
                #logging.info("maquina jogou em uma posição ocupada, tentando de novo")
        
        logging.info("jogada finalizada....")
        tabuleiro.imprimir()
        if tabuleiro.checar_vitoria():
            print(self.nome + " GANHOU")
            self.vitorias += 1
            return True
        return False 

    def pensar(self, tabuleiro):
        logging.info("maquina pensando")
        
        if tabuleiro.rodadas == 1:
            self.cerebro = Arvore(raiz_comeca)
            return self.cerebro.ramo_atual.posicao
        elif tabuleiro.rodadas == 2:
            logging.debug("ainda nao implementado")
        else:
            logging.debug("numero de possibilidades: " + str(len(self.cerebro.ramo_atual.folhas)))

            for i, folha in enumerate(self.cerebro.ramo_atual.folhas):
                tentativas = []
                logging.debug("folha: " + str(i))
                logging.debug("condicoes: " + str(folha.condicao))
                
                for condicao in folha.condicao:
                    logging.debug("testando condicao: " + str(condicao) + " precisa estar vazio")
                    tentativas.append(tabuleiro.esta_vazio(condicao, tabuleiro.casas))
                
                if False in tentativas:
                    logging.debug("folha descartada, proxima")
                else:
                    self.cerebro.navegar(folha)
                    return self.cerebro.ramo_atual.posicao


class Tabuleiro(object):
    def __init__(self):
        # casas do tabuleiro
        self.casas = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.rodadas = 0
        self.velhas = 0

    def esta_vazio(self, coordenada, matriz):
        if len(coordenada) > 2:
            logging.error("erro na formatacao da arvore")
            exit(1)
        linha = coordenada[0]
        coluna = coordenada[1]
        if matriz[linha][coluna] == 0:
            logging.debug("sim")
            return True
        logging.debug("nao")
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
        #logging.info("função iniciada")
        zeros = []

        for linha in self.casas:
            if 0 in linha:
                zeros.append(True)
            else:
                zeros.append(False)

        #logging.debug("lista de zeros" + str(zeros))

        if True not in zeros:
            print("FIM DE JOGO - DEU VELHA")
            self.velhas += 1
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
    #    logging.info("funcao iniciada")
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

    #    logging.debug("diagonal1=" + str(lista_aux))
    #    logging.debug("estado da matriz: " + str(matriz))
    #    logging.info("processando segunda diagonal")

        lista_aux = [0, 0, 0]
        j = 0

        for i in range(2, -1, -1):
    #        logging.debug("j=" + str(j))
            lista_aux[j] = self.casas[i][j]
    #        logging.debug("i=" + str(i))
    #        logging.debug("valor=" + str(lista_aux[j]))
    #        logging.debug("listaaux dentro do loop=" + str(lista_aux))
            j += 1

        matriz.append(lista_aux)
    #    logging.debug("diagonal2=" + str(lista_aux))
    #    logging.debug("estado da matriz" + str(matriz))

        return self.checar_matriz(matriz)

    def checar_vitoria(self):
        logging.info("funcao iniciada ----------------")

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




    


