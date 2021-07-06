import logging
import random
from sys import exit
from abc import abstractmethod, ABCMeta
from copy import copy, deepcopy

from tabuleiro import *
from cerebro import *
from arvore_jogador_dificil import *

class Jogador(object, metaclass=ABCMeta):
    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.vitorias = 0
    
    @abstractmethod
    def jogar(self, tabuleiro):
        pass

    def imprimir_nome(self):
        print("{} ({})".format(self.nome, self.codigo))

    def processar_jogada(self, tabuleiro, jogada):
        linha = jogada[0]
        coluna = jogada[1]

        if not tabuleiro.preencher(self.codigo, linha, coluna):
            logging.error("erro")
            exit(1)

        tabuleiro.imprimir()
        if tabuleiro.checar_vitoria():
            self.vitorias += 1
            return True
        return False

    def jogada_aleatoria(self, tabuleiro):
        pos = [random.randint(0,2), random.randint(0,2)]
        while not (tabuleiro.esta_vazio(pos, tabuleiro.casas)):
            pos = [random.randint(0,2), random.randint(0,2)]
        return pos

class JogadorManual(Jogador):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome, MANUAL)
    
    def jogar(self, tabuleiro):        
        sucesso = False

        while not sucesso:
            linha = int(input("Linha>")) - 1
            coluna = int(input("coluna>")) - 1
        
            sucesso = tabuleiro.esta_vazio(linha, coluna)
            if not sucesso:
                print("ja jogou nesta posiçao")

        return super().processar_jogada(tabuleiro, [linha, coluna])

class JogadorAleatorio(Jogador):
    def __init__(self, codigo, nome="ALEATORIO"):
        super().__init__(codigo, nome, ALEATORIO)

    def jogar(self, tabuleiro):
        super().imprimir_nome()
        if tabuleiro.rodadas == 1 and forcar_canto:
            jogada = random.choice(CANTOS)
        elif tabuleiro.rodadas == 1 and forcar_meio:
            jogada = [LINHAS["MEIO"], COLUNAS["MEIO"]]
        else:
            jogada = super().jogada_aleatoria(tabuleiro)

        return super().processar_jogada(tabuleiro, jogada)

class JogadorDificil(Jogador):
    def __init__(self, codigo, nome="DIFICIL"):
        super().__init__(codigo, nome, DIFICIL)
        self.cerebro = None

    def jogar(self, tabuleiro):
        super().imprimir_nome()
        jogada = self.escolher_estrategia(tabuleiro)
        
        if jogada == None:
            logging.error("possibilidade nao preenchida encontrada")
            logging.debug("caminho do cerebro>" + str(self.cerebro.caminho))
            exit(1)

        logging.debug("vai jogar em " + str(jogada))
        return super().processar_jogada(tabuleiro, jogada)

    def escolher_estrategia(self, tabuleiro):
        if tabuleiro.rodadas == 1:
            self.cerebro = Arvore(iniciar_arvore1())
            return self.cerebro.ramo_atual.posicao
        elif tabuleiro.rodadas == 2:
            self.cerebro = Arvore(iniciar_arvore2())
        
        for i, folha in enumerate(self.cerebro.ramo_atual.filhos):
            aprovada = False
            
            for condicao in folha.condicao:
                if not tabuleiro.esta_vazio(condicao, tabuleiro.casas):
                    aprovada = False
                    break
                else:
                    aprovada = True
            
            if aprovada:
                self.cerebro.navegar(folha)
                return self.cerebro.ramo_atual.posicao

class JogadorInteligente(Jogador):
    def __init__(self, codigo, nome="INTELIGENTE"):
        super().__init__(codigo, nome, INTELIGENTE)
        self.neuronio_raiz = Neuronio(None, None)
        self.cerebro = None
        
        self.init_cerebro()

    def init_cerebro(self):
        self.cerebro = Arvore(self.neuronio_raiz)

    def jogar(self, tabuleiro):
        super().imprimir_nome()
        jogada = self.pensar(tabuleiro)
        return super().processar_jogada(tabuleiro, jogada)

    def perder(self):
        self.cerebro.aplicar_peso()
    
    def filtrar_ramos(self, neuronio):
        lista = []
        for ramo in self.cerebro.ramo_atual.filhos:
            if ramo.estado_tabuleiro == neuronio.estado_tabuleiro:
                lista.append(ramo)

        return lista

    def ramos_identicos(self, neuronio, lista):
        for i, ramo in enumerate(lista):
            if ramo.jogada == neuronio.jogada:
                return i
        return None 

    def menor_peso(self, neuronio, lista):
        lista.sort(key = lambda x: x.peso)

        if lista[0].peso < neuronio.peso:
            return lista[0]

        return neuronio

    def pensar(self, tabuleiro):
        jogada = self.jogada_aleatoria(tabuleiro)
        neuronio = Neuronio(deepcopy(tabuleiro.casas), jogada)
        existe = False

        # verificar se já existe uma lista para esse estado
        if self.cerebro.ramo_atual.filhos:
            lista = self.filtrar_ramos(neuronio)

            # procurar por ramos identicos ao neuronio gerado
            if lista:
                ramo_identico = self.ramos_identicos(neuronio, lista)

                # usar peso do neuronio identico
                if ramo_identico is not None:
                    neuronio = lista.pop(ramo_identico)
                    if lista:
                        neuronio = self.menor_peso(neuronio, lista)
                    existe = True

        if existe:
            self.cerebro.navegar(neuronio)
        else:
            self.cerebro.add_e_navegar(neuronio)
        
        return self.cerebro.ramo_atual.jogada

def criar_jogador(codigo=X, nome=None, tipo=MANUAL):
    if tipo == MANUAL:
        if nome is not None:
            return JogadorManual(codigo, nome)
        else:
            return JogadorManual(codigo, "MANUAL({})".format(codigo))
    elif tipo == ALEATORIO:
        if nome is not None:
            return JogadorAleatorio(codigo, nome)
        else:
            return JogadorAleatorio(codigo, "ALEATORIO({})".format(codigo))
    elif tipo == DIFICIL:
        if nome is not None:
            return JogadorDificil(codigo, nome)
        else:
            return JogadorDificil(codigo, "DIFICIL({})".format(codigo))
    elif tipo == INTELIGENTE:
        if nome is not None:
            return JogadorInteligente(codigo, nome)
        else:
            return JogadorInteligente(codigo, "INTELIGENTE({})".format(codigo))
    
