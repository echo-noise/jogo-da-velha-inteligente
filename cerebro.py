import logging
from constantes import *

class Arvore(object):
    def __init__(self, raiz):
        self.raiz = raiz
        self.ramo_atual = raiz
        self.profundidade = 0
        self.caminho = ["RAIZ"]

    def navegar(self, ramo):
        self.caminho.append(self.ramo_atual.folhas.index(ramo))
        self.ramo_atual = ramo
        self.profundidade += 1
        logging.info("profundidade da arvore=" + str(self.profundidade))
        logging.debug("caminho> " + str(self.caminho))


class Folha(object):
    def __init__(self, posicao, condicao=None):
        self.posicao = posicao
        self.condicao = [self.posicao] #casas que devem estar vazias
        self.folhas = []

        if condicao:
            for item in condicao:
                self.condicao.append(item)

# arvore1: jogador começa
raiz_comeca = Folha([LINHAS["SUP"], COLUNAS["ESQ"]])
# FOLHA 0: adversario nao joga no meio
raiz_comeca.folhas.append(Folha([LINHAS["SUP"], COLUNAS["DIR"]], 
                                [[LINHAS["MEIO"], COLUNAS["MEIO"]], 
                                 [LINHAS["SUP"], COLUNAS["MEIO"]],
                                 [LINHAS["INF"], COLUNAS["DIR"]]
                                ]))
# vitoria - f0f0
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["SUP"], COLUNAS["MEIO"]]))
# caso 1: cantos vazios f0f1--------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]],
                                          [[LINHAS["INF"], COLUNAS["DIR"]],
                                           [LINHAS["INF"], COLUNAS["ESQ"]]
                                          ]))
raiz_comeca.folhas[0].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
raiz_comeca.folhas[0].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]]))
# caso 2 ----------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
# filhos 
raiz_comeca.folhas[0].folhas[2].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["DIR"]]))
raiz_comeca.folhas[0].folhas[2].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]]))
# caso 3 ----------------------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]]))
# filhos f0f3
raiz_comeca.folhas[0].folhas[3].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]],
                                             [[LINHAS["MEIO"], COLUNAS["MEIO"]]
                                             ]))
raiz_comeca.folhas[0].folhas[3].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]],
                                             [[LINHAS["MEIO"], COLUNAS["ESQ"]]
                                             ]))

# alternativa 2: caNto inf esquerdo - folha 1 filho 0
raiz_comeca.folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]], 
                                [[LINHAS["MEIO"], COLUNAS["MEIO"]], 
                                 [LINHAS["MEIO"], COLUNAS["ESQ"]]
                                ]))
# vitoria 
raiz_comeca.folhas[1].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))
# vitoria bloqueada
# caso 1: cantos vazios --------------------------------------------
raiz_comeca.folhas[1].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]],
                                          [[LINHAS["INF"], COLUNAS["DIR"]],
                                           [LINHAS["INF"], COLUNAS["ESQ"]]
                                          ]))
raiz_comeca.folhas[1].folhas[1].folhas.append(Folha([LINHAS["SUP"], COLUNAS["DIR"]]))
raiz_comeca.folhas[1].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
# caso 2: tentar canto inf direito
raiz_comeca.folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
raiz_comeca.folhas[1].folhas[2].folhas.append(Folha([LINHAS["INF"], COLUNAS["MEIO"]]))
raiz_comeca.folhas[1].folhas[2].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]]))
# caso 3 ----------------------------------------------------------
raiz_comeca.folhas[1].folhas.append(Folha([LINHAS["SUP"], COLUNAS["DIR"]]))
# filhos
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha([LINHAS["SUP"], COLUNAS["MEIO"]]))
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]]))
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))

# folha 2 - adv jogou no meio
raiz_comeca.folhas.append(Folha([LINHAS["SUP"], COLUNAS["DIR"]]))
# vitoria f2f0f0
raiz_comeca.folhas[2].folhas.append(Folha([LINHAS["SUP"], COLUNAS["MEIO"]]))
# f2f0f1 vitoria bloqueada, obrigado a bloquear
raiz_comeca.folhas[2].folhas.append(Folha([LINHAS["INF"], COLUNAS["MEIO"]]))
# f2f0f1f0fx e f2f0f1f1fx: observar o meio
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["DIR"]]))

raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]]))

raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))

raiz_comeca.folhas[2].folhas[1].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]]))
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))


# f2f0f1f2 - adv comete erro e joga no canto inf dir
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]]))
# F2F0F1F2F0 - chance de ganhar por distracao
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))
# f2f0f1f2f1 - jogar na casa que resta e encerrar com velha
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas[0].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["DIR"]]))

# f2f0f1f3 - adv comete erro e joga no canto inf esq
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]]))
# F2F0F1F3F0 - chance de ganhar por distracao
raiz_comeca.folhas[2].folhas[1].folhas[2].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["DIR"]]))
# f2f0f1f3f1 - jogar na casa que resta e encerrar com velha
raiz_comeca.folhas[2].folhas[1].folhas[2].folhas[0].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"]]))