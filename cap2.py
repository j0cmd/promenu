import os


def visao_geral():
    caminho = os.path.abspath('txt/visaogeral.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def compeesoesList():
    print('\nveja o codigo para melhor compreender')
    print('Esse exemplo mostra uma compeessao de lista')
    symbols = '$¢£¥€¤'
    code = [ord(symbol) for symbol in symbols]
    print(code)


# funcao que compara listcomp com filter e map
def listcompVsMapFilter():
    symbols = '$¢£¥€¤'
    usandoCompressao = [ord(s) for s in symbols if ord(s) > 127]
    print(f'usando compressao {usandoCompressao}')

    usandoFilterMap = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(f'usando filter e map {usandoFilterMap}')


# listcomps para computar produto cartesiano
def listcomCartesiano():
    nuberlist = [1, 2, 3, 4, 5]
    leterlist = ['a', 'b']
    diversolist = ['lua', True, 333, ['lista']]

    amboslist = [(nuber, leter) for nuber in nuberlist
                 for leter in leterlist]
    print(amboslist)

    lista2 = [(leter, divers)for divers in diversolist for leter in leterlist
              ]
    print(lista2)


# avalia o uso de expressao geradora
def genexps():
    print('expressao geradora')
    symbols = '$¢£¥€¤'
    expgera = tuple(ord(symbol)for symbol in symbols)
    print(expgera)
    print(f'tipo de dado {type(expgera)}')

    def genexpsComCartesiano():
        print('\nexpressao geradora com um produto cartesiano')
        colors = ['black', 'white']
        size = ['p', 'm', 'g']
        for tshort in (f'{c} {s}' for c in colors for s in size):
            print(tshort)
    genexpsComCartesiano()


# avalia o uso de tuplas
def tuplas():
    caminho = os.path.abspath('txt/tuplas.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    print(conteudo)

    print('tuplas usadas como registro')
    cidade, ano, populacao, area = ('tokyo', 2003, 32.450, 8014)
    print(cidade, ano, populacao, area)


def tuplasListImutaveis():
    


#    ####### acima todo o conteudo estudado#######
def menu():
    m = [
        (print('\n')),
        (print('2.2   visao geral| uma abordagem rapida sobre os temas')),
        (print('2.3.1 compressao | compressao de lista')),
        (print('2.3.2 compVsFM   | compreessao vs filter e map')),
        (print('2.3.3 cartesiano | produtos cartesianos')),
        (print('2.3.4 genexps    | expressao geradora')),
        (print('tuplas'))
    ]
    return m


def mainCap2():
    menu()
    # menu de organização
    msg = input('\nescolha uma das opçoes ... ')
    match msg:
        case 'visao geral':
            print(visao_geral())
        case 'compressao':
            print(compeesoesList())
        case 'compVsFM':
            print(listcompVsMapFilter())
        case 'cartesiano':
            print(listcomCartesiano())
        case 'genexps':
            print(genexps())
        case 'tuplas':
            print(tuplas())
        case _:
            print('fim')
