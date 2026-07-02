from interface import *
from geral import *
from teste import fiscal


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
                start_compras(compras)
       



#################################
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
                estoque_processamento(estoque)
                enter()
            case 4: #COMBINAÇÃO
                estoque_combinacao(estoque)
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
                clientes_combinacao(clientes)
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
                compras_combinacao(fiscal)
                enter()
    
#############################################
#   Listagem GLOBAL dos Relatórios
#   Como a Listagem de Filtro era apenas mostrar os deletados
#   Só bastava alterar o valor booleano, então coloquei um outro parâmetro


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


def clientes_global(clientes,valor_verdade=True): 
    print('='*145)
    print(f"|*| {'CPF':^11} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")

    for cpf in clientes:
        if clientes[cpf]['status'] == valor_verdade:
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

#############################################
#   Listagem COM FILTRO dos Relatórios

#   Compras não segue esse padrão, já que não tem
#   Como deletar uma compra

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
        print(f'\t[{i+1}] [{num}]',end='')
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
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^11} |*|")

    for nota in fiscal:
        ano_nota = recolher_ano(fiscal[nota]['data'])
        if ano_nota == ano_escolhido:
            tudo = []
            tudo.append(nota)
            for c in fiscal[nota].values():
                tudo.append(c)
            print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^11} |*|")
            print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {tudo[4]:^11} |*|")
    print('='*80)



####################################################
#   Listagem COM COMBINAÇÃO DE DADOS dos Relatórios

def combinacao_estoque(estoque,alt):
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




def combinacao_clientes(clientes,alt):
        # print(f"|*| {'CPF':^11} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")
    cabecalho_cpf = (f"     |*| {'CPF':^11} |*| ")
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
            espaco_campo = (f"{' ':^11} |*|")
            cabecalho_campo = (f"{'TELEFONE':^11} |*|")
            filtro = 'telefone'
            tam = 11
        case 4: #ENDEREÇO
            espaco_campo = (f"{' ':^30} |*|")
            cabecalho_campo = (f"{'ENDEREÇO':^30} |*|")
            filtro = 'endereco'
            tam = 30 
        case 5: #NASCIMENTO
            espaco_campo = (f"{' ':^10} |*|")
            cabecalho_campo = (f"{'NASCIMENTO':^10} |*|")
            filtro = 'nascimento'
            tam = 10
    titulo = cabecalho_cpf + cabecalho_campo
    print(titulo)

    espaco_inicial = (f"     |*| {' ':^11} |*| ")
    espaco_final = espaco_inicial + espaco_campo
    
    for cpf in clientes:
        if clientes[cpf]['status'] == True:
            print(espaco_final)
            texto_isbn = (f"     |*| {cpf:^11} |*| ")
            texto_campo = (f"{clientes[cpf][filtro]}".center(tam))
            texto_bonito = " |*|"
            texto_final = texto_isbn + texto_campo + texto_bonito
            print(texto_final)


def combinacao_compras(fiscal,alt):        
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
            espaco_campo = (f"{' ':^11} |*|")
            cabecalho_campo = (f"{'CPF':^11} |*|")
            filtro = 'cpf'
            tam = 11 


    titulo = cabecalho_id_compra + cabecalho_campo
    print(titulo)

    espaco_inicial = (f"     |*| {' ':^11} |*| ")
    espaco_final = espaco_inicial + espaco_campo
    
    for id_compra in fiscal:
        print(espaco_final)
        texto_id_compra = (f"     |*| {id_compra:^11} |*| ")
        texto_campo = (f"{fiscal[id_compra][filtro]}".center(tam))
        texto_bonito = " |*|"
        texto_final = texto_id_compra+ texto_campo + texto_bonito
        print(texto_final)


##########################################
#   FILTRO COM PROCESSAMENTO

def compras_processamento_preco(fiscal):
    """
    Retorna os indices de um dicionário, organizados de forma 
    decrescente via o critério de preço
    >>> indices_permanentes: [] 
    """
    copia = fiscal.copy()
    indices = []
    indices_permanentes = []

    while len(copia) > 0:
        maior = -1
        for notas in copia:
            preco_nota = copia[notas]['preco']
            if preco_nota > maior:
                maior = preco_nota
                indices.clear()
                indices.append(notas)
            elif preco_nota == maior:
                indices.append(notas)
        for i in indices:
            indices_permanentes.append(i)
            del copia[i]
        indices.clear()
    return indices_permanentes



def compras_processamento_listagem(indices,fiscal):
    print('='*80)
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^11} |*|")

    for i in indices:
        tudo = []
        tudo.append(i)
        for c in fiscal[i].values():
            tudo.append(c)
        print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^11} |*|")
        print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {tudo[4]:^11} |*|")

    print('='*80)




def estoque_processamento_moda(estoque):
    """
    Faz o calculo de moda das categorias dos livros e retorna
    Uma lista organizada via essas categorias
    >>> categorias_modas: []
    """
    copia = estoque.copy()
    categorias_disponiveis = []

    for isbn in copia: #COLOCAR TODAS AS CATEGORIAS DISPONIVEIS
        cat = copia[isbn]['categoria']
        if not(cat in categorias_disponiveis):
            categorias_disponiveis.append(cat)

    temp_moda = []
    temp_indices = []

    categoria_moda = []

    while len(copia) > 0:
        maior = 0
        #CONTAR QUANTAS VEZES HOUVE REPETIÇÃO DA CATEGORIA
        for c in categorias_disponiveis:
            calculo = 0
            for isbn in copia:      #.count() para dicionario
                if copia[isbn]['categoria'] == c:
                    calculo += 1    #Até aqui foi o contador 
            if calculo > maior:
                maior = calculo
                temp_moda.clear()
                temp_moda.append(c)
            elif calculo == maior:
                temp_moda.append(c)

def estoque_processamento_listar(lista_moda, estoque):
    print('='*120)
    print(f"     |*| {'ISBN':^5} |*| {'TÍTULO':^20} |*| {'AUTOR':^20} |*| {'ANO':^4} |*| {'PREÇO':^6} |*| {'CATEGORIA':^20} |*|")

    for categorias in lista_moda:
        if estoque[isbn]['status'] == valor_verdade:
            tudo = []
            tudo.append(isbn)
            for c in estoque[isbn].values():
                tudo.append(c)
            print(f"     |*| {' ':^5} |*| {' ':^20} |*| {' ':^20} |*| {' ':^4} |*| {' ':^6} |*| {' ':^20} |*|")
            print(f"     |*| {tudo[0]:^5} |*| {tudo[1]:^20} |*| {tudo[2]:^20} |*| {tudo[3]:^4} |*| {tudo[4]:^6} |*| {tudo[5]:^20} |*|")

    print('='*120)
            


    

def clientes_processamento(clientes): 
    print('='*145)
    print(f"|*| {'CPF':^11} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")

    for cpf in clientes:
        data = datetime.date.today()
        idade_valida = True if calcular_data(data,clientes[cpf]['nascimento']) >= 18 else False
        if (clientes[cpf]['status'] == valor_verdade) and (idade_valida):
            tudo = []
            tudo.append(cpf)
            for c in clientes[cpf].values():
                tudo.append(c)
            print(f"|*| {' ':^11} |*| {' ':^20} |*| {' ':^30} |*| {' ':^11} |*| {' ':^30} |*| {' ':^10} |*|")
            print(f"|*| {tudo[0]:^11} |*| {tudo[1]:^20} |*| {tudo[2]:^30} |*| {tudo[3]:^11} |*| {tudo[4]:^30} |*| {tudo[5]:^10} |*|")

    print('='*145)







