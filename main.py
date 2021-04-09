import logging

logging.basicConfig(format="%(levelname)s>%(funcName)s: %(message)s", level=logging.DEBUG)

class Jogador(object):
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def jogar(self, tabuleiro):
        logging.info("funcao iniciada")
        print(self.nome)
        sucesso = False
        while not sucesso:
            linha = int(input("Linha>")) - 1
            coluna = int(input("coluna>")) - 1
            sucesso = tabuleiro.preencher(self.codigo, linha, coluna)
            logging.info("sucesso ao jogar")
        tabuleiro.imprimir()
        if tabuleiro.checar_vitoria():
            print(self.nome + " GANHOU")
            return True
        return False 

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
            print("ja jogou nesta posicao")
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

    def checar_linha(self, linha):
        if 0 in linha or not(linha[0] == linha[1] == linha[2]):
            return False
        else:
            return True

    def checar_linhas(self, matriz):
        for linha in matriz:
            if self.checar_linha(linha):
                return True

    def checar_colunas(self):
        # kkkk piada
        logging.info("funcao iniciada")
        lista_aux = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(0,3):
            for j in range(3):
                lista_aux[j][i] = self.casas[i][j]
        return self.checar_linhas(lista_aux)

    def checar_diagonal(self):
        logging.info("funcao iniciada")
        lista_aux = [0,0,0]
        resultados = []
        for i in range(3):
            lista_aux[i] = self.casas[i][i]
        resultados.append(self.checar_linha(lista_aux))
        logging.debug("diagonal1=" + str(lista_aux))
        logging.debug("resultados=" + str(resultados))

        logging.info("processando segunda diagonal")
        lista_aux = [0, 0, 0]

        j = 0
        for i in range(2, -1, -1):
            logging.debug("j =" + str(j))
            lista_aux[j] = self.casas[i][j]
            logging.debug("i=" + str(i))
            logging.debug("valor=" + str(lista_aux[j]))
            logging.debug("listaaux dentro do loop=" + str(lista_aux))
            j += 1
        resultados.append(self.checar_linha(lista_aux))
        logging.debug("diagonal2=" + str(lista_aux))
        logging.debug("resultados=" + str(resultados))

        if True in resultados:
            return True
        else:
            return False

    def checar_vitoria(self):
        logging.info("funcao iniciada")
        for linha in self.casas:
            logging.debug("checando linha " + str(linha) + "--------")
            if self.checar_linhas(self.casas):
                return True
            elif self.checar_colunas():
                return True
            elif self.checar_diagonal():
                return self.checar_diagonal()

    def imprimir(self):
        for linha in self.casas:
            print(linha)

class Main(object):
    def __init__(self):
        super().__init__()
        self.tabuleiro = Tabuleiro()
        self.jogador1 = Jogador(1, "JOGADOR 1")
        self.jogador2 = Jogador(-1, "JOGADOR 2")
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
                    logging.debug("ninguem ganhou, procurando velha!")
                    self.fim = self.tabuleiro.checar_velha()

main = Main()
main.mainloop()

    


