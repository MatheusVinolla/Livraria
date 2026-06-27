from os import path
lista = ['nome','email','telefone','endereco','nascimento','status']
dicionario_teste = {
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
    },
}

def start(arquivo):
    global dicionario_teste

    criacao = existe(arquivo)
    if criacao == True: #ARQUIVO EXISTENTE, VERIFICAR SE ESTÁ VAZIO 
        if vazio(arquivo):
            escrever(arquivo,dicionario_teste)
    elif criacao == False: #ARQUIVO NÃO EXISTENTE, CRIAR
        criar(arquivo)
        escrever(arquivo,dicionario_teste)
            

def escrever(arquivo,dicionario):
    try:
        file = open(arquivo,'wt')
        for chave_geral in dicionario:
            linha = []
            linha.append(chave_geral) 
            for dados in dicionario[chave_geral].values():
                linha.append(str(dados)) 
            linha = ','.join(linha)
            linha = linha + '\n'

            for campo in linha:
                file.write(campo)

        file.close() 
    except Exception as erro:
        mensagem_erro('ESCREVER',erro)
    
    
def existe(arquivo):
    try:
        file = open(arquivo,'rt')
        return True
    except FileNotFoundError:
        return False
    except Exception as erro:
       mensagem_erro('EXISTÊNCIA',erro) 
    


def criar(arquivo):
    try:
        file = open(arquivo,'wt')
    except Exception as erro:
        mensagem_erro('CRIAÇÃO',erro)

def transcrever(arquivo,lista):
    try:
        file = open(arquivo,'rt')
        dicionario = {}
        #chave,valor,valor,valor
        for linha in file:
            linha = linha.replace('\n','')
            conteudo = linha.split(',')
            dicionario[conteudo[0]] = {}
            for i,campo in enumerate(conteudo[1:]):
                dicionario[conteudo[0]][lista[i]] = campo
        file.close()
        return dicionario
#dicionario[LIVRO E ETC] ={
# 'categoria' : 'informação'  }                
    except Exception as erro:
        mensagem_erro('TRANSCRIÇÃO',erro)             

def vazio(arquivo):
    try:
        if (path.getsize(arquivo) == 0):
            return True
        else:
            return False 
    except Exception as erro:
        mensagem_erro('TAMANHO',erro) 

def mensagem_erro(setor,erro):
    alt = input(f"""\033[1;33m
                 !!!!  ALERTA !!!!
    {erro}
    HOUVE UM ERRO NA MANIPULAÇÃO DE ARQUIVOS EXTERNOS
    O PROCEDIMENTO DE {setor} NÃO FOI FEITO COM SUCESSO
    PODENDO ACARRETAR EM PERCA DE DADOS, CONSULTE O 
    DESENVOLVER DO SISTEMA PARA MAIS DETALHES
    MESMO ASSIM DESEJA CONTINUAR? [S/N]
    >>> \033[m""")
    if (alt.upper() == 'N'):
        exit()


