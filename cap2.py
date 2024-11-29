import separador
import os


def visao_geral():
    caminho = os.path.abspath('txt/visaogeral.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def compeesoesList():
    print('veja o codigo para melhor compeessao')
    print('Esse exemplo mostra uma compeessao de lista')
    symbols = '$¢£¥€¤'
    code = [ord(symbol) for symbol in symbols]
    print(code)

# acima todo o conteudo estudado
def menu():
    m = [
        (print('visao geral')),
        (print('compressao')),
        (print('sequenci...')),
    ]
    return m


def mainCap2():
    visaoGeral = visao_geral()
    compressao = compeesoesList()
    # menu de organização
    menu()
    msg = input('opçoes ')
    match msg:
        case 'visao geral':
            print(visaoGeral)
        case 'comprssao':
            print(compressao)
        case _:
            print('fim')
