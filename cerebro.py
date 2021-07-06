import logging
from sys import exit
from constantes import *
from copy import copy, deepcopy

class Arvore(object):
    def __init__(self, raiz):
        self.raiz = raiz
        self.ramo_atual = copy(raiz)
        self.profundidade = 0
        self.caminho_indices = ["RAIZ"]
        self.caminho = [raiz]

    def reset(self):
        self.__init__(self.raiz)

    def navegar(self, ramo):
        self.caminho_indices.append(self.caminho[-1].filhos.index(ramo))
        self.caminho.append(ramo)
        self.ramo_atual = ramo
        self.profundidade += 1

    def add_e_navegar(self, ramo):
        self.caminho[-1].filhos.append(ramo)
        ramo.camada = self.profundidade + 1
        self.navegar(ramo)

    def aplicar_peso(self):
        for ramo in self.caminho[1:]:
            ramo.peso += 1

    def salvar_arquivo(self):
        with open(ARQUIVO_ARVORE, "a+") as arvoretxt:
            arvoretxt.write(getstr(self.raiz) + "\n")

class Folha(object):
    def __init__(self):
        self.filhos = []

class Node(Folha):
    def __init__(self, posicao, condicao=None, coord_adv=None):
        super().__init__()
        self.posicao = posicao
        self.condicao = [self.posicao] #casas que devem estar vazias

        if condicao:
            for item in condicao:
                if len(item) > 2:
                    logging.error("erro na formataçao da arvore")
                    exit(1)
                self.condicao.append(item)

class Neuronio(Folha):
    def __init__(self, estado_tabuleiro, jogada, camada=0):
        super().__init__()
        self.estado_tabuleiro = estado_tabuleiro
        self.jogada = jogada
        self.peso = 0
        self.camada = camada

def getstr(neuronio):
    spaces = "-" * (neuronio.camada) 
    string = "{}camada={}\n{}self.estado_tabuleiro = {}\n{}self.jogada = {}\n{}self.peso ={}\n{}filhos = (\n"
    string = string.format(spaces, neuronio.camada, spaces, neuronio.estado_tabuleiro, spaces, neuronio.jogada, spaces, neuronio.peso, spaces)

    for filho in neuronio.filhos:
        string += getstr(filho)
    
    return string 
