from os import makedirs

from jogador import *
from tabuleiro import *

class Main(object):
    def __init__(self, jogador1, jogador2, tabuleiro=Tabuleiro()):
        super().__init__()
        self.tabuleiro = tabuleiro 
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def processar_velha(self):
        if self.jogador1.tipo == INTELIGENTE:
            self.jogador1.perder()
        if self.jogador2.tipo == INTELIGENTE:
            self.jogador2.perder()
    
    def mainloop(self):
        if self.jogador1.tipo == INTELIGENTE:
            self.jogador1.init_cerebro()
        if self.jogador2.tipo == INTELIGENTE:
            self.jogador2.init_cerebro()

        self.tabuleiro.reset()
        self.tabuleiro.imprimir()
        
        while True: 
            if self.jogador1.jogar(self.tabuleiro):
                if self.jogador2.tipo == INTELIGENTE:
                    self.jogador2.perder()
                break
            elif self.tabuleiro.checar_velha():
                self.processar_velha()
                break
            logging.debug("jogo nao acabou, continuando")
            if self.jogador2.jogar(self.tabuleiro):
                if self.jogador1.tipo == INTELIGENTE:
                    self.jogador1.perder()
                break
            elif self.tabuleiro.checar_velha():
                self.processar_velha()
                break
            
makedirs(NOME_PASTA, exist_ok=True)
random.seed()

jogador1 = criar_jogador(codigo=X, tipo=ALEATORIO)
jogador2 = criar_jogador(codigo=O, tipo=INTELIGENTE)
tabuleiro = Tabuleiro()

if GRAVAR_HISTORICO:
    CABECALHO = "{}, {}, VELHA".format(jogador1.nome, jogador2.nome)
    with open(CAMINHO, "a+") as historico:
        historico.write(CABECALHO + "\n")

i = 0
while jogador2.vitorias <= jogador1.vitorias or i < 100:
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

    if GRAVAR_HISTORICO:
        placar_csv = "{}, {}, {}".format(jogador1.vitorias, jogador2.vitorias, tabuleiro.velhas)
        with open(CAMINHO, "a+") as historico:
            historico.write(placar_csv + "\n")
    
    i += 1