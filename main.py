from datetime import datetime
import logging

#logging.basicConfig(format="%(levelname)s>%(funcName)s: %(message)s", level=logging.DEBUG)

from sistema import *

class Main(object):
    def __init__(self, jogador1, jogador2):
        super().__init__()
        self.tabuleiro = Tabuleiro()
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def mainloop(self):
        self.tabuleiro.imprimir()
        while True: 
            if self.jogador1.jogar(self.tabuleiro):
                placar[0] += 1
                break
            elif self.tabuleiro.checar_velha():
                placar[2] += 1
                break
            logging.debug("jogo nao acabou, continuando")
            if self.jogador2.jogar(self.tabuleiro):
                placar[1] += 1
                break
            elif self.tabuleiro.checar_velha():
                placar[2] += 1
                break

random.seed()
jogador1 = Jogador(X, "MAQUINA", DIFICIL)
jogador2 = Jogador(O, "ALEATORIO", ALEATORIO)
placar = [0, 0, 0]

for i in range (10):
    print("iniciando novo jogo")
    print("partida #" + str(i))

    main = Main(jogador1, jogador2)
    main.mainloop()
    placar_str = str(datetime.now()) + "| partidas:" + str(i+1) + " " + jogador1.nome + ":" + str(placar[0]) + " " + jogador2.nome + ":" + str(placar[1]) + " velha:" + str(placar[2]) 
    print(placar_str)
    with open(ARQUIVO, "a+") as historico:
        historico.write(placar_str)
        historico.write("\n")