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
        print('definind uma funcao hash setando fix value')

        # usando a funcao hash para definir um obj como imutavel
        def fixed(o):
            try:
                hash(o)
            except TypeError:
                return False
            return True
        tf = (10, 'alpha', (1, 2))
        tm = (10, 'alpha', [1, 2])
        print(f'esse valor usa uma tupla aninhada a tupla {fixed(tf)}')
        print(f'esse valor usa uma lista aninhada a tupla {fixed(tm)}')
        print('exemplos de metodos em tupla\n')
        print('indice encontrado na posição ', tf.index('alpha'))
        print(tf.__len__())
    tuplasListImutaveis()


# 2.5 desempacotando sequencias e iteráveis
def unpacking():
    caminho = os.path.abspath('txt/unpacking.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    print(conteudo)

    # alguns exemplos de desempacotamento
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    print(f'as coordenadas == {latitude} {longitude}')

    # usando * para recolher itens em excesso
    def usando_asterisco():
        """
        *args: Definir parâmetros de função com *args para capturar argumentos 
        arbitrários em excesso é um recurso clássico do Python.
        """
        a, b, c, *args = range(1, 10)
        print('lista de 1 a 10 com lista de excesso', a, b, c, args)
        print('mais um exemplo', a, b, args, c)

    # 2.5.2 desempacotando em chamada de função
    def emChamada(a, b, c, d, *rest):
        """
            Em chamadas de função, podemos usar * múltiplas vezes:
        """
        return a, b, c, d, rest
    ch = emChamada(11, 12, 13, 4, *range(1, 18))
    print('em chamada de funcao', ch)
    usando_asterisco()

    # 2.5.3 Desempacotamento aninhado
    def umpckinkAninhado():
        """
        O alvo de um desempacotamento pode usar aninhamento, por exemplo
        (a, b, (c, d). O Python fará a coisa certa se o valor tiver a mesma
        estrutura aninhada. O Exemplo 8 mostra o desempacotamento aninhado
        em ação.
        """
        metro_areas = [
            ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # (1)
            ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
            ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
            ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
            ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
        ]
        print(f'{"":13} {"latitude":>13} {"longitude":>13}')
        for name, _, _, (latitude, longitude) in metro_areas:
            if longitude > 0:
                print(f'{name:15} | {latitude} | {longitude}')

    umpckinkAninhado()

# 2.6 pattern Matchin com sequencia
def patternMatchin():
    """ Agora vamos estudar pattern matching, que suporta maneiras
        ainda mais poderosas para desempacotar sequências.
    """
    

#    ####### acima todo o conteudo estudado#######
def menu():
    m = [
        (print('\n')),
        (print('2.2   visao geral| uma abordagem rapida sobre os temas')),
        (print('2.3.1 compressao | compressao de lista')),
        (print('2.3.2 compVsFM   | compreessao vs filter e map')),
        (print('2.3.3 cartesiano | produtos cartesianos')),
        (print('2.3.4 genexps    | expressao geradora')),
        (print('2.4 tuplas       | tupla nao sao apenas listas imutaveis')),
        (print('2.5 unpacking    | desempacotando sequencias e iteraveis'))
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
        case 'unpacking':
            print(unpacking())
        case _:
            print('fim')
