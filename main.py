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
                break
            elif self.tabuleiro.checar_velha():
                break
            logging.debug("jogo nao acabou, continuando")
            if self.jogador2.jogar(self.tabuleiro):
                break
            elif self.tabuleiro.checar_velha():
                break

random.seed()
jogador1 = Jogador(X, "MAQUINA", DIFICIL)
jogador2 = Jogador(O, "ALEATORIO", ALEATORIO)

with open(ARQUIVO, "a+") as historico:
    historico.write("# INICIO DA EXECUÇÃO:{}\n".format(datetime.now()))

for i in range (10):
    partida_display = i + 1
    print("iniciando novo jogo")
    print("partida #{}".format(partida_display))

    main = Main(jogador1, jogador2)
    main.mainloop()

    placar = "---- partidas:{} {}:{}({:.1f}%) {}:{}({:.1f}%) velha:{}({:.1f}%)"
    placar = placar.format(partida_display, jogador1.nome, jogador1.vitorias,
                          (jogador1.vitorias / partida_display)*100, jogador2.nome, 
                           jogador2.vitorias, (jogador2.vitorias / partida_display)*100,
                           main.tabuleiro.velhas, (main.tabuleiro.velhas / partida_display)*100
                           )
    print(placar)
    with open(ARQUIVO, "a+") as historico:
        historico.write(placar + "\n")

with open(ARQUIVO, "a+") as historico:
    historico.write("# FIM DA EXECUÇÃO:{}\n".format(datetime.now()))