######################################################

#   FILTRO COM PROCESSAMENTO
#   - ESTOQUE: Mostra o estoque de livros de acordo
#   com as categorias mais populares, ou seja, cal-
#   cula a moda das categorias
#   - CLIENTES: Mostra clientes com idade acima de 
#   de 18 anos
#   - COMPRAS: Mostra as compras ordenadas de forma
#   decrescente de preço

####################################################



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
        for isbn in estoque:
            if (estoque[isbn]['status'] == True) and (estoque[isbn]['categoria'] == categorias):
                tudo = []
                tudo.append(isbn)
                for c in estoque[isbn].values():
                    tudo.append(c)
                print(f"     |*| {' ':^5} |*| {' ':^20} |*| {' ':^20} |*| {' ':^4} |*| {' ':^6} |*| {' ':^20} |*|")
                print(f"     |*| {tudo[0]:^5} |*| {tudo[1]:^20} |*| {tudo[2]:^20} |*| {tudo[3]:^4} |*| {tudo[4]:^6} |*| {tudo[5]:^20} |*|")

    print('='*120)

#######################################################################################


def clientes_processamento(clientes):
    print('='*145)
    print(f"|*| {'CPF':^11} |*| {'NOME':^20} |*| {'EMAIL':^30} |*| {'TELEFONE':^11} |*| {'ENDEREÇO':^30} |*| {'NASCIMENTO':^10} |*|")

    for cpf in clientes:
        data = datetime.date.today()
        idade_valida = True if calcular_data(data,clientes[cpf]['nascimento']) >= 18 else False
        if (clientes[cpf]['status'] == True) and (idade_valida):
            tudo = []
            tudo.append(cpf)
            for c in clientes[cpf].values():
                tudo.append(c)
            print(f"|*| {' ':^11} |*| {' ':^20} |*| {' ':^30} |*| {' ':^11} |*| {' ':^30} |*| {' ':^10} |*|")
            print(f"|*| {tudo[0]:^11} |*| {tudo[1]:^20} |*| {tudo[2]:^30} |*| {tudo[3]:^11} |*| {tudo[4]:^30} |*| {tudo[5]:^10} |*|")

    print('='*145)


########################################################################################

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



