import logging
from sys import exit
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
    def __init__(self, posicao, condicao=None, coord_adv=None):
        self.posicao = posicao
        self.condicao = [self.posicao] #casas que devem estar vazias

        self.folhas = []

        if condicao:
            for item in condicao:
                if len(item) > 2:
                    logging.error("erro na formataçao da arvore")
                    exit(1)
                self.condicao.append(item)

# arvore1: jogador começa
raiz_comeca = Folha(CANTO_SUP_ESQ)
# FOLHA 0: adversario nao joga no meio
raiz_comeca.folhas.append(Folha(CANTO_SUP_DIR, 
                                [MEIO, 
                                 MEIO_SUP,
                                 CANTO_INF_DIR
                                ]))
# vitoria - f0f0
raiz_comeca.folhas[0].folhas.append(Folha(MEIO_SUP))
# caso 1: cantos vazios f0f1--------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha(MEIO,
                                          [CANTO_INF_DIR,
                                           CANTO_INF_ESQ
                                          ]))
raiz_comeca.folhas[0].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
raiz_comeca.folhas[0].folhas[1].folhas.append(Folha(CANTO_INF_ESQ))
# caso 2 ----------
raiz_comeca.folhas[0].folhas.append(Folha(CANTO_INF_DIR))
# filhos 
raiz_comeca.folhas[0].folhas[2].folhas.append(Folha(BORDA_DIR))
raiz_comeca.folhas[0].folhas[2].folhas.append(Folha(MEIO))
# caso 3 ----------------------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha(CANTO_INF_ESQ))
# filhos f0f3
raiz_comeca.folhas[0].folhas[3].folhas.append(Folha(MEIO,
                                             [MEIO
                                             ]))
raiz_comeca.folhas[0].folhas[3].folhas.append(Folha(BORDA_ESQ,
                                             [BORDA_ESQ
                                             ]))

# alternativa 2: caNto inf esquerdo - folha 1 filho 0
raiz_comeca.folhas.append(Folha(CANTO_INF_ESQ, 
                                [MEIO, 
                                 BORDA_ESQ
                                ]))
# vitoria 
raiz_comeca.folhas[1].folhas.append(Folha(BORDA_ESQ))
# vitoria bloqueada
# caso 1: cantos vazios --------------------------------------------
raiz_comeca.folhas[1].folhas.append(Folha(MEIO,
                                          [CANTO_INF_DIR,
                                           CANTO_INF_ESQ
                                          ]))
raiz_comeca.folhas[1].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))
raiz_comeca.folhas[1].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
# caso 2: tentar canto inf direito
raiz_comeca.folhas[1].folhas.append(Folha(CANTO_INF_DIR))
raiz_comeca.folhas[1].folhas[2].folhas.append(Folha(MEIO_INF))
raiz_comeca.folhas[1].folhas[2].folhas.append(Folha(MEIO))
# caso 3 ----------------------------------------------------------
raiz_comeca.folhas[1].folhas.append(Folha(CANTO_SUP_DIR))
# filhos
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha(MEIO_SUP))
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha(MEIO))
raiz_comeca.folhas[1].folhas[3].folhas.append(Folha(BORDA_ESQ))

# folha 2 - adv jogou no meio
raiz_comeca.folhas.append(Folha(CANTO_SUP_DIR))
# vitoria f2f0f0
raiz_comeca.folhas[2].folhas.append(Folha(MEIO_SUP))
# f2f0f1 vitoria bloqueada, obrigado a bloquear
raiz_comeca.folhas[2].folhas.append(Folha(MEIO_INF))
# f2f0f1f0fx e f2f0f1f1fx: observar o meio
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha(BORDA_DIR))

raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha(CANTO_INF_DIR))
raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha(CANTO_INF_ESQ))

raiz_comeca.folhas[2].folhas[1].folhas[0].folhas.append(Folha(BORDA_ESQ))

raiz_comeca.folhas[2].folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha(CANTO_INF_ESQ))
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha(CANTO_INF_DIR))


# f2f0f1f2 - adv comete erro e joga no canto inf dir
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha(CANTO_INF_ESQ))
# F2F0F1F2F0 - chance de ganhar por distracao
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas.append(Folha(BORDA_ESQ))
# f2f0f1f2f1 - jogar na casa que resta e encerrar com velha
raiz_comeca.folhas[2].folhas[1].folhas[1].folhas[0].folhas.append(Folha(BORDA_DIR))

# f2f0f1f3 - adv comete erro e joga no canto inf esq
raiz_comeca.folhas[2].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
# F2F0F1F3F0 - chance de ganhar por distracao
raiz_comeca.folhas[2].folhas[1].folhas[2].folhas.append(Folha(BORDA_DIR))
# f2f0f1f3f1 - jogar na casa que resta e encerrar com velha
raiz_comeca.folhas[2].folhas[1].folhas[2].folhas[0].folhas.append(Folha(BORDA_ESQ))

# ---segunda arvore---
# 
raiz_segundo = Folha(None)
# oponente joga no canto 
raiz_segundo.folhas.append(Folha(MEIO))

# 2 os consecutivos na horizontal sup dir
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_SUP_DIR, [BORDA_DIR, BORDA_ESQ, 
                                                           MEIO_INF, CANTO_INF_DIR, 
                                                           CANTO_INF_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[0].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[0].folhas.append(Folha(BORDA_ESQ))
# distraçao
raiz_segundo.folhas[0].folhas[0].folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[0].folhas[1].folhas.append(Folha(CANTO_INF_DIR))

# 2.2 2 os consecutivos na horizontal sup esq
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_SUP_ESQ, [BORDA_DIR, BORDA_ESQ, 
                                                           MEIO_INF, CANTO_INF_DIR, 
                                                           CANTO_INF_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[1].folhas.append(Folha(BORDA_DIR))
# distraçao
raiz_segundo.folhas[0].folhas[1].folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[1].folhas[1].folhas.append(Folha(CANTO_INF_ESQ))

# 2.3 2 os consecutivos na horizontal inf esq
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_INF_ESQ, [BORDA_DIR, BORDA_ESQ, 
                                                           MEIO_SUP, CANTO_SUP_DIR, 
                                                           CANTO_SUP_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[2].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[0].folhas[2].folhas.append(Folha(BORDA_DIR))
# distraçao
raiz_segundo.folhas[0].folhas[2].folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[2].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))
# 2.4 os consecutivos na horizontal inf dir
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_INF_DIR, [BORDA_DIR, BORDA_ESQ, 
                                                           MEIO_SUP, CANTO_SUP_DIR, 
                                                           CANTO_SUP_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[3].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[3].folhas.append(Folha(BORDA_ESQ))
# distraçao
raiz_segundo.folhas[0].folhas[3].folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[3].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))

# 2 os consecutivos na vertical esquerda inf
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_INF_ESQ, [BORDA_DIR, CANTO_SUP_DIR, 
                                                           CANTO_INF_DIR]))
# distraçao
# 0.4.0
raiz_segundo.folhas[0].folhas[4].folhas.append(Folha(CANTO_SUP_DIR))
# 0.4.1
raiz_segundo.folhas[0].folhas[4].folhas.append(Folha(MEIO_SUP))
# distraçao
raiz_segundo.folhas[0].folhas[4].folhas[1].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[0].folhas[4].folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[4].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
# 0.4.2
raiz_segundo.folhas[0].folhas[4].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[4].folhas[2].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[4].folhas[2].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[4].folhas[2].folhas.append(Folha(BORDA_DIR))

# 2 os consecutivos na vertical esquerda sup
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_SUP_ESQ, [BORDA_DIR, CANTO_SUP_DIR, 
                                                           CANTO_INF_DIR]))
# distraçao
raiz_segundo.folhas[0].folhas[5].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[5].folhas.append(Folha(MEIO_INF))
# distraçao
raiz_segundo.folhas[0].folhas[5].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[0].folhas[5].folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[5].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))


# 2 os consecutivos na vertical direita sup
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_SUP_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                           CANTO_INF_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[6].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[6].folhas.append(Folha(MEIO_INF))
# distraçao
raiz_segundo.folhas[0].folhas[6].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[0].folhas[6].folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[6].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))

raiz_segundo.folhas[0].folhas[6].folhas.append(Folha(CANTO_INF_DIR))
#distraçao
raiz_segundo.folhas[0].folhas[6].folhas[2].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[6].folhas[2].folhas.append(Folha(BORDA_ESQ))

# 2 os consecutivos na vertical - direita inf
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_INF_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                           CANTO_INF_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[7].folhas.append(Folha(CANTO_SUP_ESQ))

# 2 os consecutivos na vertical - direita inf
raiz_segundo.folhas[0].folhas.append(Folha(CANTO_INF_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                           CANTO_INF_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[7].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[7].folhas.append(Folha(MEIO_SUP))
# distraçao
raiz_segundo.folhas[0].folhas[7].folhas[2].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[0].folhas[7].folhas[2].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[7].folhas[2].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[7].folhas[2].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[7].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[7].folhas[3].folhas.append(Folha(BORDA_ESQ))

# checar o espaçado - verticais
raiz_segundo.folhas[0].folhas.append(Folha(BORDA_DIR, [CANTO_INF_ESQ, CANTO_SUP_ESQ, BORDA_ESQ]))
# distraçao
raiz_segundo.folhas[0].folhas[8].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[8].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[0].folhas[8].folhas.append(Folha(MEIO_SUP))

raiz_segundo.folhas[0].folhas.append(Folha(BORDA_ESQ, [CANTO_INF_DIR, CANTO_SUP_DIR, BORDA_DIR]))
# distraçao
raiz_segundo.folhas[0].folhas[9].folhas.append(Folha(BORDA_ESQ))
# 0.9.1
raiz_segundo.folhas[0].folhas[9].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[0].folhas[9].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[0].folhas[9].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))
# 0.9.2
raiz_segundo.folhas[0].folhas[9].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[9].folhas.append(Folha(MEIO_SUP))

# checar espaçado - horizontais
raiz_segundo.folhas[0].folhas.append(Folha(MEIO_SUP, [CANTO_INF_ESQ, CANTO_INF_DIR]))
# distraçao - 0.10.0
raiz_segundo.folhas[0].folhas[10].folhas.append(Folha(BORDA_DIR))
# 0.10.1
raiz_segundo.folhas[0].folhas[10].folhas.append(Folha(CANTO_INF_DIR))
# 0.10.1.1
raiz_segundo.folhas[0].folhas[10].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))
# 0.10.1.2
raiz_segundo.folhas[0].folhas[10].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))
# 0.10.1.3
raiz_segundo.folhas[0].folhas[10].folhas[1].folhas.append(Folha(BORDA_ESQ))
# 0.10.1.4
raiz_segundo.folhas[0].folhas[10].folhas[1].folhas.append(Folha(MEIO_SUP))
# 0.10.2
raiz_segundo.folhas[0].folhas[10].folhas.append(Folha(MEIO_SUP))

# 0.11
raiz_segundo.folhas[0].folhas.append(Folha(MEIO_INF, [CANTO_SUP_ESQ, CANTO_SUP_DIR]))
# distraçao
# 0.11.0
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(MEIO_INF))
# 0.11.1
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(MEIO_SUP))
# 0.11.2
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[11].folhas[2].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[11].folhas[2].folhas.append(Folha(BORDA_DIR))
# 0.11.3
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(CANTO_INF_ESQ, [CANTO_SUP_DIR]))
raiz_segundo.folhas[0].folhas[11].folhas[3].folhas.append(Folha(CANTO_SUP_DIR))
# 0.11.4
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[11].folhas[4].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[0].folhas[11].folhas[4].folhas.append(Folha(CANTO_INF_ESQ))
# 0.11.5
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(CANTO_INF_DIR))

# distraçao12
raiz_segundo.folhas[0].folhas[11].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[0].folhas[11].folhas[1].folhas[0].folhas.append(Folha(CANTO_INF_DIR))

raiz_segundo.folhas[0].folhas[11].folhas[1].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[11].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[11].folhas[2].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[0].folhas[11].folhas[2].folhas.append(Folha(CANTO_INF_ESQ))

# 0.12 
raiz_segundo.folhas[0].folhas.append(Folha(BORDA_ESQ, [BORDA_DIR]))
# distraçao
# 0.12.0
raiz_segundo.folhas[0].folhas[12].folhas.append(Folha(MEIO_SUP))
# 0.12.1
raiz_segundo.folhas[0].folhas[12].folhas.append(Folha(CANTO_SUP_DIR, [CANTO_INF_ESQ]))
raiz_segundo.folhas[0].folhas[12].folhas[1].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[12].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[12].folhas[1].folhas.append(Folha(CANTO_SUP_DIR))
# 0.12.2
raiz_segundo.folhas[0].folhas[12].folhas.append(Folha(CANTO_INF_DIR, [MEIO_SUP, CANTO_SUP_DIR]))
# distraçao13
raiz_segundo.folhas[0].folhas[12].folhas[2].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[0].folhas[12].folhas[2].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[12].folhas[2].folhas.append(Folha(MEIO_INF))
# 0.12.3
raiz_segundo.folhas[0].folhas[12].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[12].folhas[3].folhas.append(Folha(CANTO_INF_DIR))
raiz_segundo.folhas[0].folhas[12].folhas[3].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[0].folhas[12].folhas[3].folhas.append(Folha(BORDA_DIR))

# 0.13 
raiz_segundo.folhas[0].folhas.append(Folha(MEIO_INF))
# 0.13.0
raiz_segundo.folhas[0].folhas[13].folhas.append(Folha(BORDA_DIR))
# 0.13.1
raiz_segundo.folhas[0].folhas[13].folhas.append(Folha(CANTO_INF_DIR))
# distraçao
raiz_segundo.folhas[0].folhas[13].folhas[1].folhas.append(Folha(CANTO_SUP_ESQ))
raiz_segundo.folhas[0].folhas[13].folhas[1].folhas.append(Folha(MEIO_SUP))
# 0.13.2
raiz_segundo.folhas[0].folhas[13].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[0].folhas[13].folhas[2].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[0].folhas[13].folhas[2].folhas.append(Folha(MEIO_INF))

# adv jogou no meio
raiz_segundo.folhas.append(Folha(CANTO_SUP_ESQ))

# adv joga no canto oposto
# 1.0
raiz_segundo.folhas[1].folhas.append(Folha(CANTO_SUP_DIR, [CANTO_INF_ESQ, MEIO_SUP,
                                                           MEIO_INF, BORDA_ESQ,
                                                           BORDA_DIR]))
# 1.0.1
raiz_segundo.folhas[1].folhas[0].folhas.append(Folha(MEIO_SUP))
# 1.0.2
raiz_segundo.folhas[1].folhas[0].folhas.append(Folha(MEIO_INF))

# ver os meios
# 1.0.1.1
raiz_segundo.folhas[1].folhas[0].folhas[1].folhas.append(Folha(BORDA_DIR))
# 1.0.1.2
raiz_segundo.folhas[1].folhas[0].folhas[1].folhas.append(Folha(BORDA_ESQ))
# adv forma diagonal
# 1.1
raiz_segundo.folhas[1].folhas.append(Folha(CANTO_INF_ESQ, [CANTO_INF_DIR, MEIO_SUP,
                                                           MEIO_INF, BORDA_ESQ,
                                                           BORDA_DIR]))
# 1.1.0
raiz_segundo.folhas[1].folhas[1].folhas.append(Folha(BORDA_ESQ))
# 1.1.1
raiz_segundo.folhas[1].folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[1].folhas[1].folhas[1].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[1].folhas[1].folhas[1].folhas.append(Folha(MEIO_SUP))
# adv forma linha no meio
# 1.1.2
raiz_segundo.folhas[1].folhas.append(Folha(MEIO_SUP, [BORDA_ESQ, BORDA_DIR]))
raiz_segundo.folhas[1].folhas[2].folhas.append(Folha(CANTO_SUP_DIR)) 
raiz_segundo.folhas[1].folhas[2].folhas.append(Folha(CANTO_INF_ESQ)) 
raiz_segundo.folhas[1].folhas[2].folhas[1].folhas.append(Folha(BORDA_ESQ)) 
raiz_segundo.folhas[1].folhas[2].folhas[1].folhas.append(Folha(BORDA_DIR)) 
# mesma coisa so que debaixo
# 1.1.3
raiz_segundo.folhas[1].folhas.append(Folha(MEIO_INF, [BORDA_ESQ, BORDA_DIR]))
raiz_segundo.folhas[1].folhas[3].folhas.append(Folha(CANTO_INF_ESQ)) 
raiz_segundo.folhas[1].folhas[3].folhas[0].folhas.append(Folha(BORDA_ESQ)) 
raiz_segundo.folhas[1].folhas[3].folhas[0].folhas.append(Folha(CANTO_INF_DIR)) 
raiz_segundo.folhas[1].folhas[3].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[1].folhas[3].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[1].folhas[3].folhas[1].folhas.append(Folha(MEIO_INF))
raiz_segundo.folhas[1].folhas[3].folhas[1].folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[1].folhas[3].folhas[1].folhas[1].folhas.append(Folha(BORDA_DIR))
# adv forma linha na vertical
# 1.1.4
raiz_segundo.folhas[1].folhas.append(Folha(BORDA_ESQ))
raiz_segundo.folhas[1].folhas[4].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[1].folhas[4].folhas.append(Folha(CANTO_SUP_DIR))
raiz_segundo.folhas[1].folhas[4].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[1].folhas[4].folhas[1].folhas.append(Folha(MEIO_INF))
# ao contrario
# 1.1.5
raiz_segundo.folhas[1].folhas.append(Folha(BORDA_DIR))
raiz_segundo.folhas[1].folhas[5].folhas.append(Folha(CANTO_INF_ESQ))
raiz_segundo.folhas[1].folhas[5].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[1].folhas[5].folhas[1].folhas.append(Folha(MEIO_SUP))
raiz_segundo.folhas[1].folhas[5].folhas[1].folhas.append(Folha(MEIO_INF))