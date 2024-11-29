import separador
import os


def visao_geral():
    caminho = os.path.abspath('txt/visaogeral.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def menu():
    m = [
        (print('visao geral')),
        (print('sequenci...'))
    ]
    return m


def mainCap2():
    visaoGeral = visao_geral()

    # menu de organização
    menu()
    msg = input('opçoes ')
    match msg:
        case 'visao geral':
            print(visaoGeral)
        case _:
            print('fim')
