from cerebro import Node, Arvore
from constantes import *

def iniciar_arvore1():
    raiz_comeca = Node(CANTO_SUP_ESQ)
    raiz_comeca.filhos.append(Node(CANTO_SUP_DIR, 
                                    [MEIO, 
                                     MEIO_SUP,
                                     CANTO_INF_DIR
                                    ]))
    raiz_comeca.filhos[0].filhos.append(Node(MEIO_SUP))
    raiz_comeca.filhos[0].filhos.append(Node(MEIO,
                                              [CANTO_INF_DIR,
                                               CANTO_INF_ESQ
                                              ]))
    raiz_comeca.filhos[0].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[0].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_comeca.filhos[0].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[0].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_comeca.filhos[0].filhos[2].filhos.append(Node(MEIO))
    raiz_comeca.filhos[0].filhos.append(Node(CANTO_INF_ESQ))
    raiz_comeca.filhos[0].filhos[3].filhos.append(Node(MEIO,
                                                 [MEIO
                                                 ]))
    raiz_comeca.filhos[0].filhos[3].filhos.append(Node(BORDA_ESQ,
                                                 [BORDA_ESQ
                                                 ]))
    
    raiz_comeca.filhos.append(Node(CANTO_INF_ESQ, 
                                    [MEIO, 
                                     BORDA_ESQ
                                    ]))
    raiz_comeca.filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_comeca.filhos[1].filhos.append(Node(MEIO,
                                              [CANTO_INF_DIR,
                                               CANTO_INF_ESQ
                                              ]))
    raiz_comeca.filhos[1].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_comeca.filhos[1].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[1].filhos[2].filhos.append(Node(MEIO_INF))
    raiz_comeca.filhos[1].filhos[2].filhos.append(Node(MEIO))
    raiz_comeca.filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_comeca.filhos[1].filhos[3].filhos.append(Node(MEIO_SUP))
    raiz_comeca.filhos[1].filhos[3].filhos.append(Node(MEIO))
    raiz_comeca.filhos[1].filhos[3].filhos.append(Node(BORDA_ESQ))
    
    raiz_comeca.filhos.append(Node(CANTO_SUP_DIR))
    raiz_comeca.filhos[2].filhos.append(Node(MEIO_SUP))
    raiz_comeca.filhos[2].filhos.append(Node(MEIO_INF))
    raiz_comeca.filhos[2].filhos[1].filhos.append(Node(BORDA_DIR))
    
    raiz_comeca.filhos[2].filhos[1].filhos[0].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[2].filhos[1].filhos[0].filhos.append(Node(CANTO_INF_ESQ))
    
    raiz_comeca.filhos[2].filhos[1].filhos[0].filhos.append(Node(BORDA_ESQ))
    
    raiz_comeca.filhos[2].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_comeca.filhos[2].filhos[1].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_comeca.filhos[2].filhos[1].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    
    
    raiz_comeca.filhos[2].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_comeca.filhos[2].filhos[1].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_comeca.filhos[2].filhos[1].filhos[1].filhos[0].filhos.append(Node(BORDA_DIR))
    
    raiz_comeca.filhos[2].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_comeca.filhos[2].filhos[1].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_comeca.filhos[2].filhos[1].filhos[2].filhos[0].filhos.append(Node(BORDA_ESQ))

    return raiz_comeca

def iniciar_arvore2():
    # ---segunda arvore---
    raiz_segundo = Node(None)
    raiz_segundo.filhos.append(Node(MEIO))
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_SUP_DIR, [BORDA_DIR, BORDA_ESQ, 
                                                               MEIO_INF, CANTO_INF_DIR, 
                                                               CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[0].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[0].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[0].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[0].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_SUP_ESQ, [BORDA_DIR, BORDA_ESQ, 
                                                               MEIO_INF, CANTO_INF_DIR, 
                                                               CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[1].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[1].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_INF_ESQ, [BORDA_DIR, BORDA_ESQ, 
                                                               MEIO_SUP, CANTO_SUP_DIR, 
                                                               CANTO_SUP_ESQ]))
    raiz_segundo.filhos[0].filhos[2].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[2].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[2].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_INF_DIR, [BORDA_DIR, BORDA_ESQ, 
                                                               MEIO_SUP, CANTO_SUP_DIR, 
                                                               CANTO_SUP_ESQ]))
    raiz_segundo.filhos[0].filhos[3].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[3].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[3].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[3].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_INF_ESQ, [BORDA_DIR, CANTO_SUP_DIR, 
                                                               CANTO_INF_DIR]))
    raiz_segundo.filhos[0].filhos[4].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[4].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[4].filhos[1].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[4].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[4].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[4].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[4].filhos[2].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[4].filhos[2].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[4].filhos[2].filhos.append(Node(BORDA_DIR))
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_SUP_ESQ, [BORDA_DIR, CANTO_SUP_DIR, 
                                                               CANTO_INF_DIR]))
    raiz_segundo.filhos[0].filhos[5].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[5].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[5].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[5].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[5].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_SUP_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                               CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[6].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[6].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[6].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[6].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[6].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    
    raiz_segundo.filhos[0].filhos[6].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[6].filhos[2].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[6].filhos[2].filhos.append(Node(BORDA_ESQ))
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_INF_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                               CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[7].filhos.append(Node(CANTO_SUP_ESQ))
    
    raiz_segundo.filhos[0].filhos.append(Node(CANTO_INF_DIR, [BORDA_ESQ, CANTO_SUP_ESQ, 
                                                               CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[7].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[7].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[7].filhos[2].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[7].filhos[2].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[7].filhos[2].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[7].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[7].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[7].filhos[3].filhos.append(Node(BORDA_ESQ))
    
    raiz_segundo.filhos[0].filhos.append(Node(BORDA_DIR, [CANTO_INF_ESQ, CANTO_SUP_ESQ, BORDA_ESQ]))
    raiz_segundo.filhos[0].filhos[8].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[8].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[8].filhos.append(Node(MEIO_SUP))
    
    raiz_segundo.filhos[0].filhos.append(Node(BORDA_ESQ, [CANTO_INF_DIR, CANTO_SUP_DIR, BORDA_DIR]))
    raiz_segundo.filhos[0].filhos[9].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[9].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[9].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[9].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[9].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[9].filhos.append(Node(MEIO_SUP))
    
    raiz_segundo.filhos[0].filhos.append(Node(MEIO_SUP, [CANTO_INF_ESQ, CANTO_INF_DIR]))
    raiz_segundo.filhos[0].filhos[10].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[10].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[10].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[10].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[10].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[10].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[10].filhos.append(Node(MEIO_SUP))
    
    raiz_segundo.filhos[0].filhos.append(Node(MEIO_INF, [CANTO_SUP_ESQ, CANTO_SUP_DIR]))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[11].filhos[2].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(CANTO_INF_ESQ, [CANTO_SUP_DIR]))
    raiz_segundo.filhos[0].filhos[11].filhos[3].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos[4].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[0].filhos[11].filhos[4].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(CANTO_INF_DIR))
    
    raiz_segundo.filhos[0].filhos[11].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos[1].filhos[0].filhos.append(Node(CANTO_INF_DIR))
    
    raiz_segundo.filhos[0].filhos[11].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[11].filhos[2].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[11].filhos[2].filhos.append(Node(CANTO_INF_ESQ))
    
    raiz_segundo.filhos[0].filhos.append(Node(BORDA_ESQ, [BORDA_DIR]))
    raiz_segundo.filhos[0].filhos[12].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[12].filhos.append(Node(CANTO_SUP_DIR, [CANTO_INF_ESQ]))
    raiz_segundo.filhos[0].filhos[12].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[12].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[12].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[12].filhos.append(Node(CANTO_INF_DIR, [MEIO_SUP, CANTO_SUP_DIR]))
    raiz_segundo.filhos[0].filhos[12].filhos[2].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[12].filhos[2].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[12].filhos[2].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[12].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[12].filhos[3].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[12].filhos[3].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[12].filhos[3].filhos.append(Node(BORDA_DIR))
    
    raiz_segundo.filhos[0].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[0].filhos[13].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[0].filhos[13].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[0].filhos[13].filhos[1].filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[0].filhos[13].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[0].filhos[13].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[0].filhos[13].filhos[2].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[0].filhos[13].filhos[2].filhos.append(Node(MEIO_INF))
    
    raiz_segundo.filhos.append(Node(CANTO_SUP_ESQ))
    raiz_segundo.filhos[1].filhos.append(Node(CANTO_INF_ESQ, [CANTO_INF_DIR, MEIO_SUP,
                                                               MEIO_INF, BORDA_ESQ,
                                                               BORDA_DIR]))
    raiz_segundo.filhos[1].filhos[0].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[1].filhos[0].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[1].filhos[0].filhos[1].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[0].filhos[1].filhos.append(Node(MEIO_SUP))
    
    raiz_segundo.filhos[1].filhos.append(Node(CANTO_SUP_DIR , [CANTO_INF_DIR, MEIO_SUP,
                                                                MEIO_INF, BORDA_ESQ,
                                                                BORDA_DIR]))
    raiz_segundo.filhos[1].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[1].filhos[1].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[1].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[1].filhos[1].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[1].filhos[1].filhos.append(Node(BORDA_DIR))
    
    raiz_segundo.filhos[1].filhos.append(Node(MEIO_SUP, [BORDA_ESQ, BORDA_DIR, CANTO_INF_DIR, CANTO_INF_ESQ]))
    raiz_segundo.filhos[1].filhos[2].filhos.append(Node(CANTO_SUP_DIR)) 
    raiz_segundo.filhos[1].filhos[2].filhos.append(Node(CANTO_INF_ESQ)) 
    raiz_segundo.filhos[1].filhos[2].filhos[1].filhos.append(Node(BORDA_ESQ)) 
    raiz_segundo.filhos[1].filhos[2].filhos[1].filhos.append(Node(BORDA_DIR)) 
    
    raiz_segundo.filhos[1].filhos.append(Node(MEIO_INF, [BORDA_ESQ, BORDA_DIR, CANTO_INF_DIR, CANTO_INF_ESQ]))
    raiz_segundo.filhos[1].filhos[3].filhos.append(Node(CANTO_INF_ESQ, [BORDA_DIR, BORDA_ESQ])) 
    raiz_segundo.filhos[1].filhos[3].filhos[0].filhos.append(Node(BORDA_ESQ)) 
    raiz_segundo.filhos[1].filhos[3].filhos[0].filhos.append(Node(BORDA_DIR)) 
    raiz_segundo.filhos[1].filhos[3].filhos.append(Node(CANTO_SUP_DIR, [BORDA_DIR, BORDA_ESQ])) 
    raiz_segundo.filhos[1].filhos[3].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[1].filhos[3].filhos[1].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[1].filhos[3].filhos[1].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[1].filhos[3].filhos[1].filhos[2].filhos.append(Node(BORDA_ESQ))
    raiz_segundo.filhos[1].filhos[3].filhos[1].filhos[2].filhos.append(Node(BORDA_DIR))
    
    raiz_segundo.filhos[1].filhos[3].filhos.append(Node(BORDA_DIR)) 
    raiz_segundo.filhos[1].filhos[3].filhos[2].filhos.append(Node(CANTO_INF_ESQ)) 
    raiz_segundo.filhos[1].filhos[3].filhos[2].filhos.append(Node(CANTO_SUP_DIR)) 
    raiz_segundo.filhos[1].filhos[3].filhos.append(Node(BORDA_ESQ)) 
    raiz_segundo.filhos[1].filhos[3].filhos[3].filhos.append(Node(CANTO_INF_ESQ)) 
    raiz_segundo.filhos[1].filhos[3].filhos[3].filhos.append(Node(CANTO_SUP_DIR)) 
    
    raiz_segundo.filhos[1].filhos.append(Node(BORDA_ESQ, [CANTO_INF_DIR]))
    raiz_segundo.filhos[1].filhos[4].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[1].filhos[4].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[1].filhos[4].filhos[1].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[1].filhos[4].filhos[1].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[4].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[4].filhos[2].filhos.append(Node(CANTO_SUP_DIR))
    
    raiz_segundo.filhos[1].filhos.append(Node(BORDA_DIR, [CANTO_INF_DIR]))
    raiz_segundo.filhos[1].filhos[5].filhos.append(Node(CANTO_SUP_DIR, [MEIO_SUP, MEIO_INF]))
    raiz_segundo.filhos[1].filhos[5].filhos[0].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[1].filhos[5].filhos[0].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[5].filhos[0].filhos.append(Node(CANTO_INF_DIR))
    raiz_segundo.filhos[1].filhos[5].filhos[0].filhos.append(Node(CANTO_INF_ESQ))
    
    raiz_segundo.filhos[1].filhos[5].filhos.append(Node(MEIO_SUP, [CANTO_SUP_DIR, CANTO_INF_ESQ]))
    raiz_segundo.filhos[1].filhos[5].filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[1].filhos[5].filhos[1].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[1].filhos[5].filhos.append(Node(MEIO_INF, [CANTO_INF_ESQ, CANTO_SUP_DIR]))
    raiz_segundo.filhos[1].filhos[5].filhos[2].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[1].filhos[5].filhos[2].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[1].filhos[5].filhos.append(Node(CANTO_INF_ESQ))
    raiz_segundo.filhos[1].filhos[5].filhos[3].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[5].filhos[3].filhos.append(Node(MEIO_SUP))
    
    raiz_segundo.filhos[1].filhos[5].filhos.append(Node(CANTO_SUP_DIR))
    
    raiz_segundo.filhos[1].filhos.append(Node(CANTO_SUP_DIR))
    raiz_segundo.filhos[1].filhos[6].filhos.append(Node(MEIO_SUP))
    raiz_segundo.filhos[1].filhos[6].filhos.append(Node(MEIO_INF))
    raiz_segundo.filhos[1].filhos[6].filhos[1].filhos.append(Node(BORDA_DIR))
    raiz_segundo.filhos[1].filhos[6].filhos[1].filhos.append(Node(BORDA_ESQ))

    return raiz_segundo