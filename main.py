import estoque
import clientes
import compras
import manipular_arquivos
from interface import *
from geral import *

manipular_arquivos.start('estoque.txt',fiscal.fiscal)
manipular_arquivos.start('clientes.txt',estoque.estoque)
manipular_arquivos.start('fiscal.txt',clientes.clientes)

estoque = transcrever('estoque.txt',estoque.campos)
clientes = transcrever('clientes.txt',clientes.campos)
fiscal = transcrever('fiscal.txt',compras.campos)

alt_global = ''
while alt_global != 0:
    tela_inicial()
    menu_geral()
    alt_modulo =  validar_alt(menu())
    limpar()
    match alt_modulo:
        case 1: #estoque
            estoque.start()
        case 2: #clientes
            clientes.start()
        case 3: #compras
            compras.start()
        case 4: #relatorios
            relatorios.start()
        case 5: #sobre
           pass 
        case 0: #EXIT
            print('Obrigado e volte sempre! :D')

 
