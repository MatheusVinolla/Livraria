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
    },
    '60006': {
        'titulo': 'Fundação',
        'autor': 'Isaac Asimov',
        'ano': 2019,
        'preco': 35.50,
        'categoria': 'Ficção Científica',
        'status': True
    },
    '70007': {
        'titulo': 'Neuromancer',
        'autor': 'William Gibson',
        'ano': 2020,
        'preco': 42.00,
        'categoria': 'Ficção Científica',
        'status': True
    },
    '80008': {
        'titulo': '1984',
        'autor': 'George Orwell',
        'ano': 2018,
        'preco': 29.90,
        'categoria': 'Ficção Científica',
        'status': True
    },
    '90009': {
        'titulo': 'Orgulho e Preconceito',
        'autor': 'Jane Austen',
        'ano': 2016,
        'preco': 19.90,
        'categoria': 'Romance',
        'status': True
    },
    '11111': {
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'ano': 2020,
        'preco': 15.50,
        'categoria': 'Romance',
        'status': True
    },
    '22222': {
        'titulo': 'Drácula',
        'autor': 'Bram Stoker',
        'ano': 2022,
        'preco': 25.00,
        'categoria': 'Terror',
        'status': True
    },
    '33333': {
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
        'ano': 2021,
        'preco': 40.00,
        'categoria': 'Fantasia',
        'status': True
    },
    '44444': {
        'titulo': 'Harry Potter',
        'autor': 'J.K. Rowling',
        'ano': 2019,
        'preco': 35.00,
        'categoria': 'Fantasia',
        'status': True
    },
    '55555': {
        'titulo': 'Armas e Germes',
        'autor': 'Jared Diamond',
        'ano': 2014,
        'preco': 60.00,
        'categoria': 'História',
        'status': False # Outro soft delete
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



##############################################################################



copia = estoque.copy()
categorias_disponiveis = []

for isbn in copia: #COLOCAR AS CATEGORIAS TODAS DISPONIVEIS
    cat = copia[isbn]['categoria']
    if not(cat in categorias_disponiveis):
        categorias_disponiveis.append(cat)

temp_moda = []
temp_indices = []

categoria_moda = []

while len(copia) > 0: 
    maior = 0
    calculo = 0 
    #CONTAR QUANTAS VEZES HOUVE REPETIÇÃO
    for c in categorias_disponiveis: 
        for isbn in copia: #.count() para dicionario
            if copia[isbn]['categoria'] == c:
                calculo += 1         
        if calculo > maior:
            maior = calculo
            temp_moda.clear()
            temp_indices.clear()
            temp_moda.append(c) 
        elif calculo == maior:
            temp_moda.append(c)

    for c in temp_moda:
        categoria_moda.append(c)

    for isbn in copia:
        cat = copia[isbn]['categoria'] 
        for c in categoria_moda:
            if c == cat:
                temp_indices.append(isbn)

    for i in temp_indices:
        del copia[i] 

    categorias_disponiveis.clear()
    temp_moda.clear()
    temp_indices.clear()
          
print(categoria_moda) 

















