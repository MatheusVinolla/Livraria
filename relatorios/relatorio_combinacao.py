####################################################

#   Listagem COM COMBINAÇÃO DE DADOS dos Relatórios

##################################################
from geral import *

def estoque_combinacao(estoque,alt):
    cabecalho_isbn = (f"     |*| {'ISBN':^5} |*| ")
    match alt:
        case 1: #TITULO 
            espaco_campo = (f"{' ':^20} |*|")
            cabecalho_campo = (f"{'TÍTULO':^20} |*|")
            filtro = 'titulo'
            tam = 20
        case 2: #AUTOR
            espaco_campo = (f"{' ':^20} |*|")
            cabecalho_campo = (f"{'AUTOR':^20} |*|")
            filtro = 'autor'
            tam = 20
        case 3: #ANO
            espaco_campo = (f"{' ':^4} |*|")
            cabecalho_campo = (f"{'ANO':^4} |*|")
            filtro = 'ano'
            tam = 4
        case 4: #PREÇO
            espaco_campo = (f"{' ':^6} |*|")
            cabecalho_campo = (f"{'PREÇO':^6} |*|")
            filtro = 'preco'
            tam = 6
        case 5: #CATEGORIA
            espaco_campo = (f"{' ':^20} |*|")
            cabecalho_campo = (f"{'CATEGORIA':^20} |*|")
            filtro = 'categoria'
            tam = 20

    titulo = cabecalho_isbn + cabecalho_campo
    print(titulo)

    espaco_inicial = (f"     |*| {' ':^5} |*| ")
    espaco_final = espaco_inicial + espaco_campo

    for isbn in estoque:
        if estoque[isbn]['status'] == True:
            print(espaco_final)
            texto_isbn = (f"     |*| {isbn:^5} |*| ")
            texto_campo = f"{estoque[isbn][filtro]}".center(tam)
            texto_bonito = " |*|"
            texto_final = texto_isbn + texto_campo + texto_bonito
            print(texto_final)

####################################################################################


def clientes_combinacao(clientes,alt):
        # print(f"|*| {'CPF':^14} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")
    cabecalho_cpf = (f"     |*| {'CPF':^14} |*| ")
    match alt:
        case 1: #NOME
            espaco_campo = (f"{' ':^20} |*|")
            cabecalho_campo = (f"{'NOME':^20} |*|")
            filtro = 'nome'
            tam = 20
        case 2: #EMAIL
            espaco_campo = (f"{' ':^30} |*|")
            cabecalho_campo = (f"{'EMAIL':^30} |*|")
            filtro = 'email'
            tam = 30
        case 3: #TELEFONE
            espaco_campo = (f"{' ':^15} |*|")
            cabecalho_campo = (f"{'TELEFONE':^15} |*|")
            filtro = 'telefone'
            tam = 15
        case 4: #ENDEREÇO
            espaco_campo = (f"{' ':^30} |*|")
            cabecalho_campo = (f"{'ENDEREÇO':^30} |*|")
            filtro = 'endereco'
            tam = 30
        case 5: #NASCIMENTO
            espaco_campo = (f"{' ':^12} |*|")
            cabecalho_campo = (f"{'NASCIMENTO':^12} |*|")
            filtro = 'nascimento'
            tam = 12
    titulo = cabecalho_cpf + cabecalho_campo
    print(titulo)

    espaco_inicial = (f"     |*| {' ':^14} |*| ")
    espaco_final = espaco_inicial + espaco_campo

    for cpf in clientes:
        if clientes[cpf]['status'] == True:
            print(espaco_final)
            texto_isbn = (f"     |*| {formatar_cpf(cpf):^14} |*| ")
            if filtro == 'telefone':
                texto_campo = (f"{formatar_tel(clientes[cpf][filtro])}".center(tam))
            else:
                texto_campo = (f"{clientes[cpf][filtro]}".center(tam))
            texto_bonito = " |*|"
            texto_final = texto_isbn + texto_campo + texto_bonito
            print(texto_final)

################################################################################

def compras_combinacao(fiscal,alt):
    # print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^11} |*|")
    cabecalho_id_compra = (f"     |*| {'NOTA FISCAL':^11} |*| ")
    match alt:
        case 1: #ISBN
            espaco_campo = (f"{' ':^5} |*|")
            cabecalho_campo = (f"{'ISBN':5} |*|")
            filtro = 'isbn'
            tam = 5
        case 2: #DATA
            espaco_campo = (f"{' ':^10} |*|")
            cabecalho_campo = (f"{'DATA':^10} |*|")
            filtro = 'data'
            tam = 10
        case 3: #PREÇO
            espaco_campo = (f"{' ':^5} |*|")
            cabecalho_campo = (f"{'PREÇO':^5} |*|")
            filtro = 'preco'
            tam = 5
        case 4: #CPF
            espaco_campo = (f"{' ':^14} |*|")
            cabecalho_campo = (f"{'CPF':^14} |*|")
            filtro = 'cpf'
            tam = 14


    titulo = cabecalho_id_compra + cabecalho_campo
    print(titulo)

    espaco_inicial = (f"     |*| {' ':^11} |*| ")
    espaco_final = espaco_inicial + espaco_campo

    for id_compra in fiscal:
        print(espaco_final)
        texto_id_compra = (f"     |*| {id_compra:^11} |*| ")
        if filtro == 'cpf':
            texto_campo = (f"{formatar_cpf(fiscal[id_compra][filtro])}".center(tam))
        else:
            texto_campo = (f"{fiscal[id_compra][filtro]}".center(tam))
        texto_bonito = " |*|"
        texto_final = texto_id_compra+ texto_campo + texto_bonito
        print(texto_final)

