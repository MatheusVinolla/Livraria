#######################################################

#   Listagem GLOBAL dos Relatórios
#   Como a Listagem de Filtro era apenas mostrar os deletados
#   Só bastava alterar o valor booleano, então coloquei um outro parâmetro

############################################################

from geral import *

############################################################

def estoque_global(estoque,valor_verdade=True):
    print('='*120)
    print(f"     |*| {'ISBN':^5} |*| {'TÍTULO':^20} |*| {'AUTOR':^20} |*| {'ANO':^4} |*| {'PREÇO':^6} |*| {'CATEGORIA':^20} |*|")

    for isbn in estoque:
        if estoque[isbn]['status'] == valor_verdade:
            tudo = []
            tudo.append(isbn)
            for c in estoque[isbn].values():
                tudo.append(c)
            print(f"     |*| {' ':^5} |*| {' ':^20} |*| {' ':^20} |*| {' ':^4} |*| {' ':^6} |*| {' ':^20} |*|")
            print(f"     |*| {tudo[0]:^5} |*| {tudo[1]:^20} |*| {tudo[2]:^20} |*| {tudo[3]:^4} |*| {tudo[4]:^6} |*| {tudo[5]:^20} |*|")

    print('='*120)

############################################################

def clientes_global(clientes,valor_verdade=True):
    print('='*145) #099.412.224.10
    print(f"|*| {'CPF':^14} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^12} |*|")

    for cpf in clientes:
        if clientes[cpf]['status'] == valor_verdade:
            tudo = []
            tudo.append(cpf)
            for c in clientes[cpf].values():
                tudo.append(c)
            print(f"|*| {' ':^14} |*| {' ':^20} |*| {' ':^30} |*| {' ':^11} |*| {' ':^30} |*| {' ':^12} |*|")
            print(f"|*| {formatar_cpf(tudo[0]):^14} |*| {tudo[1]:^20} |*| {tudo[2]:^30} |*| {tudo[3]:^11} |*| {tudo[4]:^30} |*| {tudo[5]:^12} |*|")

    print('='*145)

##############################################################

def compras_global(fiscal):
    print('='*80)
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^14} |*|")

    for nota in fiscal:
        tudo = []
        tudo.append(nota)
        for c in fiscal[nota].values():
            tudo.append(c)
        print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^14} |*|")
        print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {formatar_cpf(tudo[4]):^14} |*|")

    print('='*80)

