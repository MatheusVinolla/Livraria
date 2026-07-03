#   MÓDULO DE MANIPULAÇÃO DE ARQUIVOS EXTERNOS
from os import path

def start(arquivo,dicionario): #VERIFICAR A EXISTÊNCIA E CRIAR O ARQUIVO

    criacao = existe(arquivo)
    if criacao == True: #ARQUIVO EXISTENTE, VERIFICAR SE ESTÁ VAZIO 
        if vazio(arquivo):
            escrever(arquivo,dicionario)
    elif criacao == False: #ARQUIVO NÃO EXISTENTE, CRIAR
        criar(arquivo)
        escrever(arquivo,dicionario)
            

def escrever(arquivo,dicionario):
#   ESTILO DE ESCRITA CSV
    try:
        file = open(arquivo,'wt')
        for chave_geral in dicionario:
            linha = []
            linha.append(str(chave_geral))

            for dados in dicionario[chave_geral].values():
                linha.append(str(dados)) 

            linha = ','.join(linha)
            linha = linha + '\n'

            for campo in linha:
                file.write(campo)

        file.close() 
    except Exception as erro:
        mensagem_erro(arquivo,'ESCREVER',erro)
    
    
def existe(arquivo):
    try:
        file = open(arquivo,'rt')
        return True
    except FileNotFoundError:
        return False
    except Exception as erro:
       mensagem_erro(arquivo,'EXISTÊNCIA',erro) 
    


def criar(arquivo):
    try:
        file = open(arquivo,'wt')
    except Exception as erro:
        mensagem_erro(arquivo,'CRIAÇÃO',erro)

def transcrever(arquivo,lista):
#   TRANSCRIÇÃO MODO CSV | Lista para adicionar as chaves dos campos
#                          pois só adicionei os valores sem chaves 
    try:
        file = open(arquivo,'rt')
        dicionario = {}
        #chave,valor,valor,valor
        for linha in file:
            linha = linha.replace('\n','')
            conteudo = linha.split(',') #Lista com os elementos da Linha

            dicionario[conteudo[0]] = {} #Primeiro elemento é a chave
            for i,campo in enumerate(conteudo[1:]): #Excluindo a chave
                campo = converter_tipo(campo) #Função para converter os tipos de dados
                dicionario[conteudo[0]][lista[i]] = campo
        file.close()
        return dicionario
    except Exception as erro:
        mensagem_erro(arquivo,'TRANSCRIÇÃO',erro)             

def vazio(arquivo):
    try:
        if (path.getsize(arquivo) == 0):
            return True
        else:
            return False 
    except Exception as erro:
        mensagem_erro(arquivo,'TAMANHO',erro) 

def mensagem_erro(nome_arquivo,setor,erro):
#   Caso dê algum erro que o sistema operacional proiba
#   operações de manipulação de arquivos 
    alt = input(f"""\033[1;33m
                 !!!!  ALERTA !!!!
    {erro}
    HOUVE UM ERRO NA MANIPULAÇÃO DO ARQUIVO {nome_arquivo}
    O PROCEDIMENTO DE {setor} NÃO FOI FEITO COM SUCESSO
    PODENDO ACARRETAR EM PERCA DE DADOS, CONSULTE O 
    DESENVOLVER DO SISTEMA PARA MAIS DETALHES
    MESMO ASSIM DESEJA CONTINUAR? [S/N]
    >>> \033[m""")
    if (alt.upper() == 'N'):
        exit()
#######################################################
# Função para converter um tipo entre os 4 tipos
# primitivos mais básicos, bool, int, float, string
# usado para parte de transcrever os dicionários

def converter_tipo(dado): #True-False/ Inteiro / Float / String
    dado = str(dado) 

    if (dado.title() == 'True'): #BOOLEANO True
        return True 
    elif (dado.title() == 'False'): #BOOLEANO False
        return False      
    elif (dado.isdigit()): # INTEIRO
        dado = int(dado)
        return dado
    elif (isFloat(dado)): # FLOAT
        dado = float(dado)
        return dado
    else: # STRING
        dado = str(dado)
        return dado

def isFloat(dado):
    try:
        dado = float(dado)
        return True
    except:
        return False

