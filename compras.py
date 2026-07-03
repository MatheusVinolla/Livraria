from interface import *
from geral import *
from datetime import datetime
from manipular_arquivos import escrever

# Dicionário teste conectando o de ESTOQUE com CLIENTES
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

campos = ['isbn','data','preco','cpf']

def start(arquivo,clientes,estoque,fiscal):
    alternativa = ''
    while alternativa != 0:
        tela_compra()
        menu_compra()
        alternativa = validar_alt(2)
        limpar()
        match alternativa:
            case 1:  #CADASTRAR
                tela_cadastrar()
                cadastrar(clientes,estoque,fiscal)
                escrever(arquivo,fiscal)
            case 2:  #PESQUISAR
                tela_pesquisar()
                pesquisar(fiscal)

def cadastrar(clientes,livros,fiscal):

    cpf = input('Insira o CPF do Cliente para pesquisar: ')
    if not(cpf in clientes):
        print('CPF/Cliente não encontrado, tente novamente...')
        return fiscal
    isbn = input('Insira o ISBN do Livro que deseja adquirir: ')
    if not(isbn in livros):
        print('ISBN/Livro não encontrado, tente novamente...')
        return fiscal
    print('Livro encontrado!')
    confirmar = input('Deseja confirmar a compra deste livro?')
    if (confirmar[0].upper() == 'S') or (confirmar == '\n'):
        id_compra = gerador_id(fiscal)
        fiscal[id_compra] = {}
        fiscal[id_compra]['cpf'] = cpf
        fiscal[id_compra]['isbn'] = isbn 
        fiscal[id_compra]['data'] = datetime.now().replace(microsecond=0)  
        fiscal[id_compra]['preco'] = livros[isbn]['preco']   
    else:
        print('Ok, caso mude de escolha, saiba que estou aqui') 

def pesquisar(fiscal):
    id_compra = input('Insira o ID DA COMPRA para pesquisar:') 
    if not(id_compra in fiscal):
        print('ID DA COMPRA não encontrado no banco fiscal...')
        print('Faça uma compra no modo de cadastrar')
        print('Para adicionar uma nova nota fiscal no banco fiscal da livraria')
    else:
        print('ID DA COMPRA encontrado com sucesso!')
        listagem(fiscal[id_compra])    
