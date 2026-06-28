#   MODÚLO DE ESTOQUE

from geral import *
from interface import *
from manipular_arquivos import escrever

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

campos = ['ISBN''TÍTULO','AUTOR','ANO','PREÇO','CATEGORIA']

#################################

def start(arquivo,dicionario):
    alternativa = ''
    while alternativa != 0:
        tela_estoque()
        menu_estoque()
        alternativa = validar_alt(alternativa)
        limpar()
        match alternativa:
            case 1: #CADASTRAR
                tela_cadastrar()
                estoque = cadastrar(dicionario)
                escrever(arquivo,dicionario)
                enter()
            case 2: #ATUALIZAR
                tela_atualizar()
                estoque = atualizar(dicionario)
                escrever(arquivo,dicionario)
                enter()
            case 3: #PESQUISAR
                tela_pesquisar()
                pesquisar(dicionario)
                enter()
            case 4: #DELETAR
                tela_deletar()
                estoque = deletar(dicionario) 
                escrever(arquivo,dicionario)
                enter()


def cadastrar(dicionario):
    isbn = input('Insira o ISBN para CADASTRAR: ')
    titulo = input('Insira o TÍTULO para CADASTRAR: ')   
    autor = input('Insira o/a AUTOR/A para CADASTRAR: ')
    ano = input('Insira o ANO para CADASTRAR: ')
    ano = validar_ano(ano)
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

def atualizar(livros): #PASS DESENVOLVIMENTO AINDA
   # alvo = input('Insira o ISBN que deseja PESQUISAR no ESTOQUE >>> ')
   # if (alvo in livros) and (livros[alvo]['status'] == True):
   #     print('ISBN/LIVRO Encontrado!')
   #     listagem(livros[alvo])
   #     alt_atualizar = input('Escolha o campo que deseja alterar >>>')

   #     livros[alvo]['titulo'] = input('Insira o novo TÍTULO para ATUALIZAR: ') if alt_atualizar in '16' else titulo 

   #     autor = input('Insira o/a novo/a AUTOR/A para ATUALIZAR: ')if alt_atualizar in '26' else autor

   #     ano = input('Insira o novo ANO para ATUALIZAR: ')if alt_atualizar in '36'

   #     preco = input('Insira o novo PREÇO para ATUALIZAR: ')if alt_atualizar in '46'
   #     preco = validar_float(preco) 

   #     categoria = input('Insira a nova CATEGORIA para ATUALIZAR: ')if alt_atualizar in '56'

   #     del livros[alvos] 
   #     livros[alvos] = {
   #     'titulo' : titulo,
   #     'autor' : autor,
   #     'ano' : ano,
   #     'preco' : preco,
   #     'categoria' : categoria,
   #     'status' : True
   #     }
   #     print()
   #     print('ATUALIZAÇÃO FEITA COM SUCESSO!')

   #         case _:#INTACTO/INVALIDO
   #                 print('Opção escolhida para permanência dos dados')
   #             
   #     return livros
   #                             
   #         
   # 

   #     
   # else:
   #     print('ISBN/LIVRO NÃO Encontrado...tente novamente')


    
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
        return dicionario
    else:
        print('ISBN/LIVRO NÃO Encontrado...tente novamente')
        return dicionario


