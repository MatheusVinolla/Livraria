import biblioteca
import usuarios
import compras
from relatorios import relatorio_main

import manipular_arquivos
from interface import *
from geral import *

manipular_arquivos.start('estoque.txt',biblioteca.estoque)
manipular_arquivos.start('clientes.txt',usuarios.clientes)
manipular_arquivos.start('fiscal.txt',compras.fiscal)

estoque_dicio = manipular_arquivos.transcrever('estoque.txt',biblioteca.campos)
clientes_dicio = manipular_arquivos.transcrever('clientes.txt',usuarios.campos)
fiscal_dicio = manipular_arquivos.transcrever('fiscal.txt',compras.campos)

alt_global = ''
while alt_global != 0:
    limpar()
    tela_inicial()
    menu_geral()
    alt_global = validar_alt(5)
    limpar()
    match alt_global:
        case 1: #estoque
            biblioteca.start('estoque.txt',estoque_dicio)
        case 2: #clientes
            usuarios.start('clientes.txt',clientes_dicio)
        case 3: #compras
            compras.start('fiscal.txt',clientes_dicio,estoque_dicio,fiscal_dicio)
        case 4: #relatorios
            relatorio_main.start(estoque_dicio,clientes_dicio,fiscal_dicio)
        case 5: #sobre
            tela_sobre()
            sobre()
            enter() 
        case 0: #EXIT
            print('Obrigado e volte sempre! :D')

 
