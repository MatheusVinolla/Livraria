from geral import *

def start(estoque,clientes,fiscal):
    alternativa = ''
    while alternativa != 0:
        limpar()
        tela_relatorio()
        menu_relatorio()
        alternativa = validar_alt(alternativa,3)
        limpar()
        match alternativa:
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
        limpar()
        match alternativa:
            case 1: #GLOBAL
                estoque_global(estoque)
                enter()
            case 2: #FILTRO
                pass
            case 3: #PROCESSAMENTO
                pass
            case 4: #COMBINAÇÃO
                pass

def start_clientes(clientes):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt(alternativa,4)
        match alternativa:
            case 1: #GLOBAL
                pass
            case 2: #FILTRO
                pass
            case 3: #PROCESSAMENTO
                pass
            case 4: #COMBINAÇÃO
                pass

def start_compras(fiscal):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt(alternativa,4)
        match alternativa:
            case 1: #GLOBAL
                pass
            case 2: #FILTRO
                pass
            case 3: #PROCESSAMENTO
                pass
            case 4: #COMBINAÇÃO
                pass

    
#############################################
#   Listagem GLOBAL dos Relatórios

def estoque_global(estoque): 
    print('='*120)
    print(f"     |*| {'ISBN':^5} |*| {'TÍTULO':^20} |*| {'AUTOR':^20} |*| {'ANO':^4} |*| {'PREÇO':^6} |*| {'CATEGORIA':^20} |*|")

    for isbn in estoque:
        if estoque[isbn]['status'] == True:
            tudo = []
            tudo.append(isbn)
            for c in estoque[isbn].values():
                tudo.append(c)
            print(f"     |*| {' ':^5} |*| {' ':^20} |*| {' ':^20} |*| {' ':^4} |*| {' ':^6} |*| {' ':^20} |*|")
            print(f"     |*| {tudo[0]:^5} |*| {tudo[1]:^20} |*| {tudo[2]:^20} |*| {tudo[3]:^4} |*| {tudo[4]:^6} |*| {tudo[5]:^20} |*|")

    print('='*120)


def clientes_global(clientes): 
    print('='*145)
    print(f"|*| {'CPF':^11} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")

    for cpf in clientes:
        if clientes[cpf]['status'] == True:
            tudo = []
            tudo.append(cpf)
            for c in clientes[cpf].values():
                tudo.append(c)
            print(f"|*| {' ':^11} |*| {' ':^20} |*| {' ':^30} |*| {' ':^11} |*| {' ':^30} |*| {' ':^10} |*|")
            print(f"|*| {tudo[0]:^11} |*| {tudo[1]:^20} |*| {tudo[2]:^30} |*| {tudo[3]:^11} |*| {tudo[4]:^30} |*| {tudo[5]:^10} |*|")

    print('='*145)


def compras_global(fiscal): 
    print('='*80)
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^11} |*|")

    for nota in fiscal:
        tudo = []
        tudo.append(nota)
        for c in fiscal[nota].values():
            tudo.append(c)
        print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^11} |*|")
        print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {tudo[4]:^11} |*|")

    print('='*80)

