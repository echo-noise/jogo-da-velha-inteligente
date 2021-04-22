# posiçoes nomeadas
LINHAS = {
    "SUP": 0,
    "MEIO": 1,
    "INF": 2,
}

COLUNAS = {
    "ESQ": 0,
    "MEIO": 1,
    "DIR": 2
}

class Arvore(object):
    def __init__(self, raiz):
        self.raiz = raiz

class Folha(object):
    def __init__(self, posicao, condicao):
        self.posicao = posicao
        self.condicao = condicao #casas que devem estar vazias
        self.folhas = []

# arvore1: jogador começa
raiz_comeca = Folha([LINHAS["SUP"], COLUNAS["ESQ"]], None)
# adversario nao joga no meio
raiz_comeca.folhas.append(Folha([LINHAS["SUP"], COLUNAS["DIR"]], 
                            [[LINHAS["MEIO"], COLUNAS["MEIO"]], 
                            [LINHAS["MEIO"], COLUNAS["DIR"],
                            [LINHAS["INF"], COLUNAS["DIR"]]]
                            ]))
# filhos da folha 0
# vitoria 
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["SUP"], COLUNAS["MEIO"]], 
                                          [[LINHAS["SUP"], COLUNAS["MEIO"]]
                                          ]))
# vitoria bloqueada
# caso 1: cantos vazios --------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]],
                                          [[LINHAS["INF"], COLUNAS["DIR"]],
                                          [[LINHAS["INF"], COLUNAS["ESQ"]]]
                                          ]))
# caso 2 ----------------------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]],
                                          [[LINHAS["INF"], COLUNAS["DIR"]]
                                          ]))
# filhos 
raiz_comeca.folhas[0].folhas[1].append(Folha([LINHAS["MEIO"], COLUNAS["DIR"]]
                                              [[LINHAS["MEIO"], COLUNAS["DIR"]   
                                              ]]))
raiz_comeca.folhas[0].folhas[1].append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"]]
                                              [[LINHAS["MEIO"], COLUNAS["MEIO"]   
                                              ]]))
# caso 3 ----------------------------------------------------------
raiz_comeca.folhas[0].folhas.append(Folha([LINHAS["INF"], COLUNAS["DIR"]],
                                            [[LINHAS["INF"], COLUNAS["DIR"]]
                                            ]))
# filhos
raiz_comeca.folhas[0].folhas[2].append(Folha([LINHAS["MEIO"], COLUNAS["MEIO"],
                                             [LINHAS["MEIO"], COLUNAS["MEIO"]]
                                            ]))
raiz_comeca.folhas[0].folhas[2].append(Folha([LINHAS["MEIO"], COLUNAS["ESQ"],
                                             [LINHAS["MEIO"], COLUNAS["ESQ"]]
                                            ]))

# alternativa 2
raiz_comeca.folhas.append(Folha([LINHAS["INF"], COLUNAS["ESQ"]], 
                            [[LINHAS["MEIO"], COLUNAS["MEIO"]], 
                            [LINHAS["MEIO"], COLUNAS["ESQ"],
                            [LINHAS["INF"], COLUNAS["ESQ"]]]
                            ]))


arvore_comeca = Arvore(raiz_comeca)
