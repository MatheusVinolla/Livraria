#   MODÚLO DE ESTOQUE

from geral import *
from interface import *
from manipular_arquivos import escrever

#Dicionário com campos de teste
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
        'status': False  
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

campos = ['ISBN''TÍTULO','AUTOR','ANO','PREÇO','CATEGORIA']

#################################

def start(arquivo,dicionario):
    alternativa = ''
    while alternativa != 0:
        limpar()
        tela_estoque()
        menu_estoque()
        alternativa = validar_alt()
        limpar()
        match alternativa:
            case 1: #CADASTRAR
                tela_cadastrar()
                cadastrar(dicionario)
                escrever(arquivo,dicionario)
                enter()
            case 2: #ATUALIZAR
                tela_atualizar()
                atualizar(dicionario)
                escrever(arquivo,dicionario)
                enter()
            case 3: #PESQUISAR
                tela_pesquisar()
                pesquisar(dicionario)
                enter()
            case 4: #DELETAR
                tela_deletar()
                deletar(dicionario) 
                escrever(arquivo,dicionario)
                enter()


def cadastrar(dicionario):
    isbn = input('Insira o ISBN para CADASTRAR: ')

    titulo = input('Insira o TÍTULO para CADASTRAR: ')   
    titulo = validar_nome(titulo)

    autor = input('Insira o/a AUTOR/A para CADASTRAR: ')
    autor = validar_nome(autor)
    
    ano = input('Insira o ANO para CADASTRAR: ')
    ano = validar_ano(ano)

    preco = input('Insira o PREÇO para CADASTRAR: ')
    preco = validar_float(preco)

    categoria = input('Insira a CATEGORIA para CADASTRAR: ')
    categoria = validar_ano(categoria)
    
    dicionario[isbn] = {
    'titulo' : titulo,
    'autor' : autor,
    'ano' : ano,
    'preco' : preco,
    'categoria' : categoria,
    'status' : True
    }
    print()
    print('CADASTRAMENTO FEITO COM SUCESSO!')

def atualizar(livros):
    alvo = input('Insira o ISBN que deseja PESQUISAR no ESTOQUE >>> ')
    if (alvo in livros) and (livros[alvo]['status'] == True):       

        listagem(dicionario[alvo])
        print("Caso deseje manter os mesmos dados anterior, precione enter")
        print()

        titulo = atualizar_campo('Insira o novo TÍTULO para ATUALIZAR: ',livros[alvo]['titulo'])   
        titulo = validar_nome(titulo)

        autor = atualizar_campo('Insira novo o/a AUTOR/A para ATUALIZAR: ',livros[alvo]['autor'])
        autor = validar_nome(autor)
        
        ano = atualizar_campo('Insira o novo ANO para ATUALIZAR: ',livros[alvo]['ano'])
        ano = validar_ano(ano)

        preco = atualizar_campo('Insira o novo PREÇO para ATUALIZAR: ',livros[alvo]['preco'])
        preco = validar_float(preco)

        categoria = atualizar_campo('Insira a novo CATEGORIA para ATUALIZAR: ',livros[alvo]['categoria'])
        categoria = validar_ano(categoria)
        
        dicionario[isbn] = {
        'titulo' : titulo,
        'autor' : autor,
        'ano' : ano,
        'preco' : preco,
        'categoria' : categoria,
        'status' : True
        }
        print()
        print('ATUALIZAÇÃO FEITA COM SUCESSO!')
 
    else:
        print('ISBN/LIVRO NÃO Encontrado...tente novamente')


    
def pesquisar(dicionario):
    alvo = input('Insira o ISBN que deseja PESQUISAR no ESTOQUE >>> ')
    if (alvo in dicionario) and (dicionario[alvo]['status'] == True):
        print('ISBN/LIVRO Encontrado!')
        listagem(dicionario[alvo])
    else:
        print('ISBN/LIVRO NÃO Encontrado...tente novamente')

def deletar(dicionario):
    alvo = input('Insira o ISBN que deseja DELETAR no ESTOQUE >>> ')
    if (alvo in dicionario) and (dicionario[alvo]['status'] == True):
        print('ISBN/LIVRO Encontrado!')
        dicionario[alvo]['status'] = False
        print('EXCLUSÃO FEITA COM SUCESSO!')
    else:
        print('ISBN/LIVRO NÃO Encontrado...tente novamente')


