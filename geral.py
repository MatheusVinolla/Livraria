import os
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
    tel = tel.replace('.','')
    return tel 


def validar_telefone(tel):
    tel = caracter_telefone(tel) 
    while not(len(tel) == 11) or not(tel.isdigit()):
        tel = input('\033[31mNúmero Inválido, tente novamente >>> \033[m')
        tel = caracter_telefone(tel)
    return tel

def formatar_tel(tel):
    #84999146181
    #(84) 9 9914-6181
    tel = str(tel)
    ddd = '(' + tel[:2] + ')' + ' '
    num = tel[2:]
    num1 = num[1:5] + '-' + num[5:]
    todo = ddd + num1
    return todo
    

def caracter_nome(nome): #Verifica se tem algum número
    for letra in nome:
        if (letra.isdigit()):
            return False
    return True


def validar_nome(nome): #E verifica também se o nome está vazio
    while (len(nome.strip()) == 0) and (caracter_nome(nome)):
        nome = input('\033[31mNome Inválido, tente novamente >>> \033[m')
    return nome


def validar_alt(num=4,saida=True):
    alt = input('Escolha a opção que deseja acessar >>> ')

    aceitavel = [] #COLOCAR OS INTERVALOS ACEITOS
    saida = 0 if (saida) else 1 #Contar o 0 [Saida] ou não
    for x in range(saida,num+1):
        aceitavel.append(str(x))

    while not (alt in aceitavel):
        alt = input('\033[1;31mResposta Inválida, tente novamente >>> \033[m')
    alt = int(alt)
    return alt


def validar_float(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except:
            valor = input('\033[31mResposta Inválida, tente novamente >>> \033[m')

#################################################
#   DATA Apenas    

def ano_inteiro_presente(ano):
    """
    Função criada para trabalhar com o validar_ano
    Retorna True se o valor for possível de se converter a inteiro
    E já testa logo se o valor é menor ou igual ao ano atual
    Retorna False no contrário
    """
    try:
        ano = int(ano)
        ano_atual = int(datetime.datetime.now().year)
        if ano > ano_atual:
            return False
        return True
    except:
        return False    

def validar_ano(ano): #Função para validar o ano para cadastrar um livro...
    while (len(ano) != 4) and not(ano_inteiro_presente(ano)):
        valor = input('\033[31mAno Inválido, tente novamente >>> \033[m')
    return ano

def caracter_data(data): #Tira caracteres que o usuário pode digitar na data
    data = data.strip()
    data = data.replace('\\','')       
    data = data.replace(',','')
    data = data.replace('-','') 
    data = data.replace('.','')   
    data = data.replace(' ','')   
    data = data.replace(':','')  
    data = data.replace(';','')  
    data = data.replace('_','')
    data = data.replace('|','')
    data = data.replace('/','')
    return data

def numeros_data(data): #Verificar se há letra
    for letra in data:
        if not(letra.isdigit()):
            return False
    return True

def validar_setor_data(data):
    ano = int(data[-4:])
    mes = int(data[2:4])
    dia = int(data[:2])
    # validar ano
    if not(ano_inteiro_presente(ano)):
        return False 
    # validar mes
    if ((mes < 0) or (mes > 12)):
        return False 
    # validadar dia 
    if ((dia < 0) or (dia > 31)):
       return False 
    return True

def validar_data(data):
    data = str(data)
    data = caracter_data(data) #Tira os caracteres não números /-.
    while not(len(data) == 8) or not(numeros_data(data)) or not(validar_setor_data(data)):
        data = input('\033[31mData Inválida, tente novamente >>> \033[m')
        data = caracter_data(data)         
    
    data = data[:2] + '/' + data[2:4] + '/' + data[4:]  
    return data
    #28/01/2008

def data_brasileira(data):
    """
    Pega o valor dado pela data do datetime
    E transforma ao padrão brasileiro... 
    """
    
    data = str(data) #2026-01-23 #ano, mes, dia
    ano = data[:4]
    mes = data[5:7]
    dia = data[-2:]
    data = dia + '/' + mes + '/' + ano    
    return data


####################################################
#   CPF Apenas
def caracter_cpf(cpf):
    cpf = str(cpf)
    cpf = cpf.replace(',','')
    cpf = cpf.replace('-','') 
    cpf = cpf.replace('.','')   
    cpf = cpf.replace(' ','')  
    return cpf 


def validar_cpf(cpf):
    cpf = caracter_cpf(cpf)
    while not(cpf_valido(cpf)):
        cpf = input('\033[31mCPF Inválido, tente novamente >>> \033[m')
        cpf = caracter_cpf(cpf)
    return cpf


def cpf_valido(cpf):
   #Verificar se tem letra 
    if not(cpf.isnumeric()):
        return False
    #Verificar o tamanho
    if not(len(cpf) == 11):
        return False
    #Verificar se o digito 1 corresponde ao padrão de CPF
    digito1 = 0
    for num in range(10,1,-1):
        digito1 += num * int(cpf[10 - num])  
    digito1 = 11 - (digito1 % 11)
    digito1 = digito1 if digito1 < 9 else 0 

    if not(digito1 == int(cpf[9])):
        return False    

    #Verificar se o digito 2 corresponde ao padrão de CPF
    digito2 = 0
    for num in range(11,1,-1):
        digito2 += num * int(cpf[11 - num])  
    digito2 = 11 - (digito2 % 11)
    digito2 = digito2 if digito2 < 9 else 0

    if not(digito2 == int(cpf[10])):
        return False    
    
    return True  


def formatar_cpf(cpf):
    cpf = str(cpf) #099.412.224.10
    final = ''
    for i,num in enumerate(cpf):
        final += str(num)
        if ((i != 0) and ((i + 1) % 3) == 0):
            final += '.' 
    return final
    
        


####################################
#   Funções Gerais

def limpar():
    nome = os.name 
    if nome == 'nt': #WINDOWS
        os.system('cls') 
    else: #POSIX
        os.system('clear')

def enter():
    print()
    input(' Digite ENTER para continuar '.center(50,"="))


def listagem(dicionario,compras=False): #Listagem especifica para função de pesquisar
    copia = dicionario.copy()
    if not(compras): #COMPRAS NÃO TEM STATUS, ENTÃO DÁ ERRO
        del copia['status']
    print('_'*70) 
    for nome,valor in copia.items():
        print(f': {nome.title():^20} |*| {valor:<20}')
    print('_'*70)


def recolher_ano(data,normal=True):
    """
    Apenas retornar o ano de uma string
    Na forma de inteiro para cálculo
    """
    data = str(data)
    if normal:
        ano = data[-4:]
    else:
        ano = data[:4]
    return int(ano)

def calcular_data(data1, data2):
    # Data 1 será a data entregue via o datetime onde o ano é primeiro
    #   E também pelo dia de hoje   
    # Data 2 será a data normal com o ano por último
    data1 = recolher_ano(data1,False)
    data2 = recolher_ano(data2) 
    calculo = data1 - data2
    return calculo


def gerador_id(lista): #O ID DA NOTA FISCAL
    while True: 
        n1 = str(randint(0,9))
        n2 = str(randint(0,9))
        n3 = str(randint(0,9))
        n4 = str(randint(0,9))
        n5 = n1 + n2 + n3 + n4
        if not(n5 in lista):
            return n5

def atualizar_campo(mensagem,antigo_valor):
    novo_valor = input(f"{mensagem}")
    if (len(novo_valor.strip()) == 0): #Variavel vazia, manter o dado anterior
        return antigo_valor
    else:
        return novo_valor 


def sobre():
    print("""\033[1;33m
    <<< TRABALHO DA DISCIPLINA DE ALGORITMOS E LÓGICA DE PROGRAMAÇÃO >>>
    TRABALHO: PyBooks
    AUTOR: Matheus Vínolla Medeiros e Silva
    UNIVERSIDADE: Universidade Federal do Rio Grande do Norte
    DIVISÃO: Centro de Ensino Superior do Seridó
    DOCENTE: Flavius Gorgônio 
    LICENÇA: Licença Livre GPU 3.0
    <<< ------------------------------------------------------------ >>>
    \033[m""")
    
