#   MODÚLO DE CLIENTES

from geral import *
clientes = {} 


###########################################

def start():
    alternativa = ''
    while alternativa != 0:
        menu()
        alternativa = validar_alt(alternativa)
        match alternativa:
            case 1: #CADASTRAR
                cadastrar(clientes)
                enter()
            case 2: #ATUALIZAR
                atualizar(clientes)
                enter()
            case 3: #PESQUISAR
                pesquisar(clientes)
                enter()
            case 4: #DELETAR
                deletar(clientes)
                enter()

campos = ['cpf','titulo','email','telefone','endereco','nascimento']

def cadastrar(dicionario):
    cpf = input('Insira o CPF para CADASTRAR: ')
    cpf = validar_cpf(cpf)

    nome = input('Insira o NOME para CADASTRAR: ')
    nome = validar_nome(nome)

    email = input('Insira o EMAIL para CADASTRAR: ')
    email = validar_email(email)

    telefone = input('Insira o TELEFONE para CADASTRAR: ')
    telefone = validar_telefone(telefone)

    endereco = input('Insira o ENDEREÇO para CADASTRAR: ')
    endereco = validar_nome(endereco)

    nascimento = input('Insira a DATA DE NASCIMENTO para CADASTRAR: ')
    nascimento = validar_data(nascimento)

    dicionario[cpf] = {
    'cpf' : cpf,
    'nome' : nome,
    'email' : email,
    'telefone' : telefone,
    'endereco' : endereco,
    'nascimento' : nascimento,
    'status': True
    }
    print()
    print('CADASTRAMENTO FEITO COM SUCESSO!')
    return dicionario
    

def atualizar(data): #INCOMPLETA
    pass 

def pesquisar(dicionario):
    alvo = input('Insira o CPF que deseja PESQUISAR no BANCO >>> ')
    alvo = caracter_cpf(alvo) 
    if (alvo in dicionario) and (dicionario[alvo]['status'] == True):
        print()
        listagem(dicionario[alvo])
    else:
        print('CPF/CLIENTE NÃO Encontrado...tente novamente!')
         
def deletar(dicionario):
    alvo = input('Insira o CPF que deseja DELETAR no BANCO >>> ')
    if (alvo in dicionario) and (dicionario[alvo]['status'] == True):
        print()
        dicionario[alvo]['status'] = False
        print('EXCLUSÃO FEITA COM SUCESSO!')
    else:
        print('CPF/CLIENTE NÃO Encontrado...tente novamente!')

start() 
