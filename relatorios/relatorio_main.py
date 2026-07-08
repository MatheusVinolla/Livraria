from interface import *
from geral import *

from relatorios.relatorio_global import *
from relatorios.relatorio_processamento import *
from relatorios.relatorio_combinacao import *

def start(estoque,clientes,fiscal):
    alternativa = ''
    while alternativa != 0:
        limpar()
        tela_relatorio()
        menu_relatorio()
        alternativa = validar_alt(3)
        limpar()
        match alternativa: #RELATÓRIOS PARA MÓDULOS ESPECIFICOS
            case 1:#Estoque
                start_estoque(estoque)
            case 2:#Clientes
                start_clientes(clientes)
            case 3:#Compras
                start_compras(fiscal)
       



##################################################
#   STARTS para cada parte
def start_estoque(estoque):
    alternativa = ''
    while alternativa != 0:
        limpar() 
        menu_relatorio_geral()
        alternativa = validar_alt(4)
        limpar()
        match alternativa:
            case 1: #GLOBAL
                estoque_global(estoque)
                enter()
            case 2: #FILTRO
                estoque_global(estoque,False)
                enter()
            case 3: #PROCESSAMENTO
                lista_moda = estoque_processamento_moda(estoque)
                estoque_processamento_listar(lista_moda, estoque)
                enter()
            case 4: #COMBINAÇÃO
                menu_combinacao_estoque()
                alt = validar_alt(5,False)
                limpar()
                estoque_combinacao(estoque,alt)
                enter()

def start_clientes(clientes):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt()
        limpar()
        match alternativa:
            case 1: #GLOBAL
                clientes_global(clientes)
                enter()
            case 2: #FILTRO
                clientes_global(clientes,False)
                enter()
            case 3: #PROCESSAMENTO
                clientes_processamento(clientes)
                enter()
            case 4: #COMBINAÇÃO
                menu_combinacao_clientes()
                alt = validar_alt(5,False)
                limpar()
                clientes_combinacao(clientes,alt)
                enter()

def start_compras(fiscal):
    alternativa = ''
    while alternativa != 0:
        limpar()
        menu_relatorio_geral()
        alternativa = validar_alt()
        limpar()
        match alternativa:
            case 1: #GLOBAL
                compras_global(fiscal)
                enter()
            case 2: #FILTRO
                menu_anos = menu_compras_filtro(fiscal)
                compras_filtro(fiscal, menu_anos) 
                enter()
            case 3: #PROCESSAMENTO
                indices = compras_processamento_preco(fiscal)
                compras_processamento_listagem(indices,fiscal)
                enter()
            case 4: #COMBINAÇÃO
                menu_combinacao_compras()
                alt = validar_alt(saida=False)
                limpar()
                compras_combinacao(fiscal,alt)
                enter()
    

#############################################
#   Listagem COM FILTRO dos Relatórios

#   Compras não segue esse padrão, já que não tem
#   Como deletar uma compra
#   E como era apenas ela sozinha, decidi deixar ela
#   No arquivo main dos relatórios...

#############################################

def menu_compras_filtro(fiscal):
    """
    Retorna uma lista com os anos 
    organizados de forma crescente 
    """
    menu_anos = []
    for notas in fiscal:
        ano_nota = recolher_ano(fiscal[notas]['data'])
        if not(ano_nota in menu_anos):
            menu_anos.append(ano_nota)
    menu_anos.sort()
    return menu_anos



def compras_filtro(fiscal,menu_anos):
    #[21,22,33,44,55,11,00]
    for i,num in enumerate(menu_anos):
        print(f'\t[{i+1}] [{num}]')
    print()

    #VALIDADOR RÁPIDO 
    #Diferente do convencional já que não tem saída
    validos = []
    for num in range(len(menu_anos) + 1): #Colocar as opções validas
        if num != 0:
            validos.append(str(num))

    alt = input('Escolha o ano que deseja filtrar as compras por: ')
    while not(alt in validos):
        alt = input('\033[1;33mResposta Inválida, tente novamente >>> \033[m')

    ano_escolhido = int(menu_anos[int(alt) - 1])

    limpar()

    print('='*80)
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^14} |*|")

    for nota in fiscal:
        ano_nota = recolher_ano(fiscal[nota]['data'])
        if ano_nota == ano_escolhido:
            tudo = []
            tudo.append(nota)
            for c in fiscal[nota].values():
                tudo.append(c)
            print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^14} |*|")
            print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {formatar_cpf(tudo[4]):^14} |*|")
    print('='*80)









    





