from relatorio import *
from geral import *

def start(estoque,clientes,fiscal)
    alternativa = ''
    while alternativa != 0:
        limpar()
        tela_relatorio()
        menu_relatorio()
        alternativa = validar_alt(alternativa,3)
        limpar()
        case 1:#Estoque
            start_estoque(estoque)
            enter()
        case 2:#Clientes
            start_clientes(clientes)
            enter()
        case 3:#Compras
            start_compras(compras)
            enter()
       





#################################
#   STARTS para cada parte
def start_estoque(estoque):
    alternativa = ''
    while alternativa != 0:
        limpar() 
        menu_relatorio_geral()
        alternativa = validar_alt(alternativa,4)
        match alternativa:
            case 1: #GLOBAL
            case 2: #FILTRO
            case 3: #PROCESSAMENTO
            case 4: #COMBINAÇÃO

def start_clientes(clientes):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt(alternativa,4)
        match alternativa:
            case 1: #GLOBAL
            case 2: #FILTRO
            case 3: #PROCESSAMENTO
            case 4: #COMBINAÇÃO

def start_compras(fiscal):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt(alternativa,4)
        match alternativa:
            case 1: #GLOBAL
            case 2: #FILTRO
            case 3: #PROCESSAMENTO
            case 4: #COMBINAÇÃO

    
##############################################
#   Listagem dos Relatórios em si

