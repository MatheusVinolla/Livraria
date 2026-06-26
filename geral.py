def listagem(dicionario):
    print('_'*70)
    for nome,valor in dicionario.items():
        print(f': {nome.title():^20} |*| {valor:<20}')

    print('_'*70)


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


