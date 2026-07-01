from geral import validar_alt,limpar

fiscal = {
    '1542': {  # ID da compra aleatório de 4 dígitos
        'isbn': '10001',  # Conecta com 'Noites Brancas'
        'data': '25/06/2026',
        'preco': 22.50,
        'cpf': '12345678901'  # Frisk
    },
    '8821': {
        'isbn': '20002',  # Conecta com 'Duna'
        'data': '26/06/2026',
        'preco': 45.00,
        'cpf': '23456789012'  # Sans
    },
    '0439': {
        'isbn': '40004',  # Conecta com 'O Iluminado'
        'data': '27/06/2026',
        'preco': 39.90,
        'cpf': '34567890123'  # Papyrus
    },
    '9105': {
        'isbn': '50005',  # Conecta com 'Maus'
        'data': '27/06/2026',
        'preco': 49.90,
        'cpf': '45678901234'  # Quarto CPF solicitado
    }
}
def recolher_ano(data):
    ano = data[-4:]
    return int(ano)

def menu_filtro_compras(fiscal):
    menu_anos = []
    for notas in fiscal:
        ano_nota = recolher_ano(fiscal[notas]['data'])
        if not(ano_nota in menu_anos):
            menu_anos.append(ano_nota)
    menu_anos.sort()
    return menu_anos
 
def filtro_compras(fiscal,menu_anos):
    #[21,22,33,44,55,11,00]
    for i,num in enumerate(menu_anos):
        print(f'\t[{i+1}] [{num}]',end='')
    print()

    #VALIDADOR RÁPIDO
    validos = []
    for num in range(len(menu_anos) + 1):
        if num != 0:
            validos.append(str(num))
    alt = input('Escolha o ano que deseja filtrar as compras por: ') 
    while not(alt in validos):
        alt = input('\033[1;33mResposta Inválida, tente novamente >>> \033[m')

    ano_escolhido = int(menu_anos[int(alt) - 1])

    limpar() 

    print('='*80)
    print(f"     |*| {'NOTA FISCAL':^11} |*| {'ISBN':^5} |*| {'DATA':^10} |*| {'PREÇO':^5} |*| {'CPF':^11} |*|")

    for nota in fiscal:
        ano_nota = recolher_ano(fiscal[nota]['data'])
        if ano_nota == ano_escolhido:
            tudo = []
            tudo.append(nota)
            for c in fiscal[nota].values():
                tudo.append(c)
            print(f"     |*| {' ':^11} |*| {' ':^5} |*| {' ':^10} |*| {' ':^5} |*| {' ':^11} |*|")
            print(f"     |*| {tudo[0]:^11} |*| {tudo[1]:^5} |*| {tudo[2]:^10} |*| {tudo[3]:^5} |*| {tudo[4]:^11} |*|")

    print('='*80)

filtro_compras(fiscal,menu_filtro_compras(fiscal))
    alt = validar_alt(len(menu_anos) - 1) 
