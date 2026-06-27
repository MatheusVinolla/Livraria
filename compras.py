from geral import *
from datetime import datetime
def start()

def cadastrar(clientes,livros,fiscal):
    cpf = input('Insira o CPF do Cliente para pesquisar: ')
    if not(cpf in clientes):
        print('CPF/Cliente não encontrado, tente novamente...')
        return None
    isbn = input('Insira o ISBN do Livro que deseja adquirir: ')
    if not(isbn in livros):
        print('ISBN/Livro não encontrado, tente novamente...')
        return None
    print('Livro encontrado!')
    confirmar = input('Deseja confirmar a compra deste livro?')
    if (confirmar[0].upper() == 'S') or (confirmar == '\n'):
        fiscal[cpf] = {}
        fiscal[cpf]['isbn'] = isbn 
        fiscal[cpf]['data'] = datetime.now().replace(microsecond=0)  
        fiscal[cpf]['preco'] = livros[isbn]['preco']   
        return fiscal
    else:
        print('Ok, caso mude de escolha, saiba que estou aqui') 
        return None

def pesquisar(fiscal):
    cpf = input('Insira o CPF do Cliente para pesquisar:') 
    if not(cpf in fiscal):
        print('CPF/Cliente não encontrado no banco fiscal...')
        print('Faça uma compra no modo de cadastrar')
        print('Para adicionar o CPF no banco fiscal da livraria')
    else:
        print('CPF/Cliente encontrado com sucesso!')
        listagem(fiscal[cpf])
    
