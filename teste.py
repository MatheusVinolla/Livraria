fiscal = {
    '1542': {  # ID da compra aleatório de 4 dígitos
        'isbn': '10001',  # Conecta com 'Noites Brancas'
        'data': '25/06/2026',
        'preco': 22.50,
        'cpf': '12345678901'  # Frisk
    },
    '8821': {
        'isbn': '20002',  # Conecta com 'Duna'
        'data': '26/06/2026',
        'preco': 45.00,
        'cpf': '23456789012'  # Sans
    },
    '0439': {
        'isbn': '40004',  # Conecta com 'O Iluminado'
        'data': '27/06/2026',
        'preco': 39.90,
        'cpf': '34567890123'  # Papyrus
    },
    '9105': {
        'isbn': '50005',  # Conecta com 'Maus'
        'data': '27/06/2026',
        'preco': 49.90,
        'cpf': '45678901234'  # Quarto CPF solicitado
    }
}

estoque = {
    '10001': {
        'titulo': 'Noites Brancas',
        'autor': 'Dostoievski',
        'ano': 2023,
        'preco': 22.50,
        'categoria': 'Romance',
        'status': True
    },
    '20002': {
        'titulo': 'Duna',
        'autor': 'Frank Herbert',
        'ano': 2021,
        'preco': 45.00,
        'categoria': 'Ficção Científica',
        'status': True
    },
    '30003': {
        'titulo': 'Sapiens',
        'autor': 'Yuval Harari',
        'ano': 2015,
        'preco': 55.90,
        'categoria': 'História',
        'status': False  # Exemplo de livro com soft delete aplicado
    },
    '40004': {
        'titulo': 'O Iluminado',
        'autor': 'Stephen King',
        'ano': 2017,
        'preco': 39.90,
        'categoria': 'Terror',
        'status': True
    },
    '50005': {
        'titulo': 'Maus',
        'autor': 'Art Spiegelman',
        'ano': 2005,
        'preco': 49.90,
        'categoria': 'Quadrinhos',
        'status': True
    }
}




















#   ORDENAR DICIONARIO POR ONDEM CRESCENTE DE UM DADO CRITÉRIO
def testando():
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







copia = estoque.copy()
categorias_disponiveis = []
temp_moda = []
categoria_moda = []
while len(copia) > 0: 
    maior = 0
    for isbn in copia:
        cat = copia[isbn]['categoria']
        if not(cat in categorias_disponiveis):
            categorias_disponiveis.append(cat)

    calculo = 0
    for c in categorias_disponiveis: 
        for isbn in copia:
            if copia[isbn]['categoria'] == c:
                calculo += 1        

        if calculo > maior:
            maior = calculo
            temp_moda.clear()
            temp_moda.append(c) 
        elif calculo == maior:
            temp_moda.append(c)

    for c in temp_moda:
        categoria_moda.append(c)


    for categoria_moda 

    for isbn in copia:
        cat = copia[isbn]['categoria'] 
        for c in categoria_moda:
            if c == cat:
                del copia[isbn]  
    categorias_disponiveis.clear()
    temp_moda.clear()
          
print(categoria_moda) 

















