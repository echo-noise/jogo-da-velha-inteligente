import logging
from sys import exit

from sistema import *

class Main(object):
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador1 = Jogador()

    def teste_caminho1(self):
