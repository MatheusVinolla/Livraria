#   MODÚLO DE CLIENTES

from geral import *
from interface import *
from manipular_arquivos import escrever

# Dicionário com campos para teste
clientes = {
    "12345678901": {
        "nome": "Frisk",
        "email": "frisk.determinado@undertale.com",
        "telefone": "11999990001",
        "endereco": "Ruínas Sala do Trono",
        "nascimento": "15092015",
        "status": True,
    },
    "23456789012": {
        "nome": "Sans the Skeleton",
        "email": "sans.badtime@undertale.com",
        "telefone": "13988880002",
        "endereco": "Nevadal Casa dos Irmãos",
        "nascimento": "01041995",
        "status": True,
    },
    "34567890123": {
        "nome": "Papyrus",
        "email": "great.papyrus@undertale.com",
        "telefone": "13988880003",
        "endereco": "Nevada Guarda Real",
        "nascimento": "22071997",
        "status": True,
    },
    "45678901234": {
        "nome": "Toriel Dreemurr",
        "email": "toriel.mae@undertale.com",
        "telefone": "11977770004",
        "endereco": "Ruínas Casa da Toriel",
        "nascimento": "08031980",
        "status": True,
    },
    "56789012345": {
        "nome": "Undyne",
        "email": "undyne.ngahhh@undertale.com",
        "telefone": "21966660005",
        "endereco": "Cachoeira Casa do Peixe",
        "nascimento": "12111992",
        "status": True,
    }
}

campos = ['nome','email','telefone','endereco','nascimento','status']

###########################################

def start(arquivo,dicionario):
    alternativa = ''
    while alternativa != 0:
        limpar()
        tela_clientes()
        menu_cliente()
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

    dicionario[cpf] = {
    'nome' : nome,
    'email' : email,
    'telefone' : telefone,
    'endereco' : endereco,
    'nascimento' : nascimento,
    'status': True
    }
    print()
    print('CADASTRAMENTO FEITO COM SUCESSO!')
    

def atualizar(dicionario): #INCOMPLETA
    alvo = input('Insira o CPF que deseja ATUALIZAR no BANCO >>> ')
    alvo = caracter_cpf(alvo) 
    if (alvo in dicionario) and (dicionario[alvo]['status'] == True):
        listagem(dicionario[alvo]) 

        print("Caso queira manter os mesmos dados anteriores do cliente, precione enter")
        print()

        nome = atualizar_campo('Insira o novo NOME para CADASTRAR: ',dicionario[alvo]['nome'])
        nome = validar_nome(nome)

        email = atualizar_campo('Insira o novo EMAIL para CADASTRAR: ',dicionario[alvo]['email'])
        email = validar_email(email)

        telefone = atualizar_campo('Insira o novo TELEFONE para CADASTRAR: ',dicionario[alvo]['telefone'])
        telefone = validar_telefone(telefone)

        endereco = atualizar_campo('Insira o novo ENDEREÇO para CADASTRAR: ',dicionario[alvo]['endereco'])
        endereco = validar_nome(endereco)

        nascimento = atualizar_campo('Insira a nova DATA DE NASCIMENTO para CADASTRAR: ',dicionario[alvo]['nascimento'])

        dicionario[alvo] = {
        'nome' : nome,
        'email' : email,
        'telefone' : telefone,
        'endereco' : endereco,
        'nascimento' : nascimento,
        'status': True
        }
        print()
        print('ATUALIZAÇÃO FEITA COM SUCESSO!')



    else:
        print('CPF/CLIENTE NÃO Encontrado...tente novamente!')


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
        return dicionario
    else:
        print('CPF/CLIENTE NÃO Encontrado...tente novamente!')

