from datetime import datetime
import logging
from sistema import *

logging.basicConfig(format="%(levelname)s>%(funcName)s: %(message)s", level=logging.DEBUG)

class Main(object):
    def __init__(self, jogador1, jogador2, tabuleiro=Tabuleiro()):
        super().__init__()
        self.tabuleiro = tabuleiro 
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def mainloop(self):
        self.tabuleiro.reset()
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
jogador1 = Jogador(X, "ALEATORIO", ALEATORIO)
jogador2 = Jogador(O, "MAQUINA", DIFICIL)
tabuleiro = Tabuleiro()

with open(ARQUIVO, "a+") as historico:
    historico.write("# INICIO DA EXECUÇÃO:{}\n".format(datetime.now().replace(microsecond=0)))

for i in range (10000):
    partida_display = i + 1
    print("iniciando novo jogo")
    print("partida #{}".format(partida_display))

    main = Main(jogador1, jogador2, tabuleiro)
    main.mainloop()

    placar = "---- partidas:{} {}:{}({:.1f}%) {}:{}({:.1f}%) velha:{}({:.1f}%)"
    placar = placar.format(partida_display, jogador1.nome, jogador1.vitorias,
                          (jogador1.vitorias / partida_display)*100, jogador2.nome, 
                           jogador2.vitorias, (jogador2.vitorias / partida_display)*100,
                           tabuleiro.velhas, (tabuleiro.velhas / partida_display)*100
                           )
    print(placar)

    if jogador1.vitorias >= 1:
        logging.error("jogador aleatorio ganhou da maquina")
        logging.debug("caminho>" + str(jogador2.cerebro.caminho))
        exit(1)
    
    jogador2.cerebro = None
    
    with open(ARQUIVO, "a+") as historico:
        historico.write(placar + "\n")

with open(ARQUIVO, "a+") as historico:
    historico.write("# FIM DA EXECUÇÃO:{}\n".format(datetime.now().replace(microsecond=0)))