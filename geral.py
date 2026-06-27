import datetime
from random import randint

######################################################
#   Validações:
def validar_email(email):
    while not('.'in email) and not('@' in email):
        email = input('\033[31mEmail Inválido, tente novamente >>> \033[m')
    return email

def caracter_telefone(tel):
    tel = tel.replace('-','')
    tel = tel.replace(' ','')
    tel = tel.replace('(','')
    tel = tel.replace(')','')
    return tel 

def validar_telefone(tel):
    tel = caracter_telefone(tel) 
    while not(len(tel) != 11) and not(tel.isdigit()):
        tel = input('\033[31mNúmero Inválido, tente novamente >>> \033[m')
    return tel

def validar_nome(nome):
    while (len(nome.strip()) == 0):
        nome = input('\033[31mNome Inválido, tente novamente >>> \033[m')
    return nome

def validar_alt(alt):
    alt = input('Escolha a opção que deseja acessar >>> ')
    while not (alt in '01234'):
        alt = input('\033[31mResposta Inválida, tente novamente >>> \033[m')
    return int(alt)


def validar_float(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except:
            valor = input('\033[31mResposta Inválida, tente novamente >>> \033[m')


def validar_data(data): #CONSTRUÇÃO
    return data
       
##################
#   CPF Apenas
def caracter_cpf(cpf):
    cpf = cpf.replace(',','')
    cpf = cpf.replace('-','') 
    cpf = cpf.replace('.','')   
    cpf = cpf.replace(' ','')  
    return cpf 


def validar_cpf(cpf):
    cpf = caracter_cpf(cpf)
    while not(cpf_valido(cpf)):
        cpf = input('\033[31mCPF Inválido, tente novamente >>> \033[m')
    return cpf


def cpf_valido(cpf):
   #Verificar se tem letra 
    if not(cpf.isnumeric()):
        return False
    #Verificar o tamanho
    if not(len(cpf) == 11):
        return False

    digito1 = 0
    for num in range(10,1,-1):
        digito1 += num * int(cpf[10 - num])  
    digito1 = 11 - (digito1 % 11)
    digito1 = digito1 if digito1 < 9 else 0 

    if not(digito1 == int(cpf[9])):
        return False    

    digito2 = 0
    for num in range(11,1,-1):
        digito2 += num * int(cpf[11 - num])  
    digito2 = 11 - (digito2 % 11)
    digito2 = digito2 if digito2 < 9 else 0

    if not(digito2 == int(cpf[10])):
        return False    
    
    return True  

####################################
#   Funções Gerais

def enter():
    print()
    input(' Digite ENTER para continuar '.center(50,"="))


def menu():
    print("""
    [1] CADASTRAR
    [2] ATUALIZAR
    [3] PESQUISAR
    [4] DELETAR
    [0] Sair...
    """)

def listagem(dicionario):
    print('_'*70)
    del dicionario['status']
    for nome,valor in dicionario.items():
        print(f': {nome.title():^20} |*| {valor:<20}')

    print('_'*70)

def gerador_id(lista):
    while True: 
        n1 = str(randint(0,9))
        n2 = str(randint(0,9))
        n3 = str(randint(0,9))
        n4 = str(randint(0,9))
        n5 = int(n1 + n2 + n3 + n4)
        if not(n5 in lista):
            return n5
