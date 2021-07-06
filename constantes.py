from os import path, makedirs
from datetime import datetime

PASTA_LOGS = "logs"
makedirs(PASTA_LOGS, exist_ok=True)

# codigos 
X = "x" 
O = "o"

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

CANTO_SUP_ESQ = [LINHAS["SUP"], COLUNAS["ESQ"]]
CANTO_SUP_DIR = [LINHAS["SUP"], COLUNAS["DIR"]]
CANTO_INF_ESQ = [LINHAS["INF"], COLUNAS["ESQ"]]
CANTO_INF_DIR = [LINHAS["INF"], COLUNAS["DIR"]]
MEIO_SUP = [LINHAS["SUP"], COLUNAS["MEIO"]]
MEIO_INF = [LINHAS["INF"], COLUNAS["MEIO"]]
MEIO = [LINHAS["MEIO"], COLUNAS["MEIO"]]
BORDA_ESQ = [LINHAS["MEIO"], COLUNAS["ESQ"]]
BORDA_DIR = [LINHAS["MEIO"], COLUNAS["DIR"]]

CANTOS = [CANTO_SUP_DIR, CANTO_INF_ESQ, CANTO_INF_DIR, CANTO_SUP_ESQ, BORDA_DIR, BORDA_ESQ, MEIO_SUP, MEIO_INF]

# tipos de jogadores
MANUAL = 1
ALEATORIO = 2
DIFICIL = 3
INTELIGENTE = 4

# arquivos de historico e log
NOME_ARQUIVO = "historico"
NOME_PASTA = "historicos"

INICIO_EXECUCAO = datetime.now().replace(microsecond = 0)
ARQUIVO = "{}_{}.csv".format(NOME_ARQUIVO, INICIO_EXECUCAO)
CAMINHO = path.join(NOME_PASTA, ARQUIVO)
GRAVAR_HISTORICO = 1

ARQUIVO_LOG = path.join(PASTA_LOGS, "log{}.txt".format(INICIO_EXECUCAO))
ARQUIVO_ARVORE= path.join(PASTA_LOGS, "arvore{}.txt".format(INICIO_EXECUCAO))

# debug
forcar_meio = 0
forcar_canto = 0