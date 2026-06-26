#   MODÚLO DE ESTOQUE
from geral import *
estoque = {}


#################################

def start():
    alternativa = ''
    while alternativa != 0:
        menu()
        alternativa = validar_alt(alternativa)
        match alternativa:
            case 1: #CADASTRAR
                cadastrar(estoque)
                enter()
            case 2: #ATUALIZAR
                atualizar(estoque)
                enter()
            case 3: #PESQUISAR
                pesquisar(estoque)
                enter()
            case 4: #DELETAR
                deletar(estoque)
                enter()

campos = ['ISBN''TÍTULO','AUTOR','ANO','PREÇO','CATEGORIA']

def cadastrar(dicionario):
    isbn = input('Insira o ISBN para CADASTRAR: ')
    titulo = input('Insira o TÍTULO para CADASTRAR: ')   
    autor = input('Insira o/a AUTOR/A para CADASTRAR: ')
    ano = input('Insira o ANO para CADASTRAR: ')
    preco = input('Insira o PREÇO para CADASTRAR: ')
    preco = validar_float(preco)
    categoria = input('Insira a CATEGORIA para CADASTRAR: ')
    
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
    return dicionario

def atualizar(dicionario):
    pass
    
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


start() 
