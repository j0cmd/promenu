import array
import separador


def variavelDeApoio():
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokio', 2003, 35_450, 0.66, 80.14)
    traveler_ids = [('usa', '31195855'), ('bra', 'ce342567'), ('esp', 'xda205856')]
    print(f'\n ==//=={lax_coordinates} {city} {year} {pop} {chg} {area}')
    for passport in sorted(traveler_ids):
        print(f'{passport}')

    for country, _ in traveler_ids:
        print(country)



def registro():
    primeiro, segundo, terceiro = (1, 2, 3)
    print(primeiro, segundo, terceiro)


def expressaoGcomArray(symbols):
    myArray = array.array('I', (ord(symboll) for symboll in symbols))
    print(myArray)


def expressaoGeradora():
    symbols = '$¢£¥€¤'
    tt = tuple(ord(symbol) for symbol in symbols)
    print('genexp', tt)
    print(type(tt))
    expressaoGcomArray(symbols)


#   letras = ['A', 'K', 'Q']
letras = 'AKQ'
naips = ['espadas', 'paus', 'ouros', 'copas']

def naipes():
    baralho = [[le, n] for le in letras for n in naips]
    print(f'\n{baralho}\n')


def camisas():
    cores = ['preto', 'branca']
    tamanho = ['p', 'm', 'g']
    camisetas = [(color, size) for color in cores for size in tamanho]
    print(camisetas)


def myname2(sn):
    sn = [chr(n) for n in sn]
    print('my name 2 ', sn)


def myname():
    name = 'josinaldo'
    sn = [ord(n) for n in name]
    print('my name 1', sn)
    myname2(sn)


def compreesao():
    simbols = '$¢£¥€¤'
    codes = [s := ord(simbol) for simbol in simbols]
    print(s)
    print('retorno da list compreesion\n', codes)


def visaoGeral():
    print('2.2 visao geral das sequencias embutidas\n')


def main():
    print('tudo do capitulo 2')
    visaoGeral()
    compreesao()
    myname()
    camisas()
    naipes()
    expressaoGeradora()
    registro()
    separador.se('separador')
    variavelDeApoio()
    separador.se('variavel de apoio')
