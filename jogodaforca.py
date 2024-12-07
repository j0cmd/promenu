# jogo da forca
# o jogo tem como objetivo buscar uma palavra em um arquivo com varias
# aprensentará o numero de letras da mesma, e tambem a opção de digitar 
# uma letra
# se tiver a letra digitada, a palavra a letra será adicionada caso 
# contrario um erro será marcado

def forma(palavra):
    lista = []
    for letra in palavra:
        lista.append('__ ')
    indices = [i for i, char in enumerate(palavra) if char == letra]
    print(lista)
    print(indices)


def entrada():
    palavra = 'palavra'
    #  tamanho = len(palavra)
    #  print('__ '*tamanho)

    le = input('advinhe as letras ')
    if le in palavra:
        print('tem')
    else:
        print('errado')

    forma(palavra)

def main_jogo():
    entrada()


main_jogo()
