# jogo da forca
# o jogo tem como objetivo buscar uma palavra em um arquivo com varias
# aprensentará o numero de letras da mesma, e tambem a opção de digitar 
# uma letra
# se tiver a letra digitada, a palavra a letra será adicionada caso 
# contrario um erro será marcado
import os
import random

def definindo_palavra():
    caminho = os.path.abspath('br_utf8.txt')

    # abrindo o arquivo
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()

    #  linhas = [linhas.strip() for linha in linhas if linha.strip()]

    # sorteio da palavra
    if linhas:
        linha_sorteada = random.choice(linhas)
        print(f'{linha_sorteada}')
    return linha_sorteada


lista = []
def forma(palavra):
    for letra in palavra:
        lista.append('__ ')
    #  indices = [i for i, char in enumerate(palavra) if char == letra]
    print(lista)
    print(len(lista))

    #  if le in palavra:
        #  letra = palavra.enumerate(le)
        #  lista.insert(letra, le)
    #  print(indices)

    #  for i in indices:
        #  indices.insert('aa')
    #  print(indices)


def entrada(lista):
    palavra = definindo_palavra()

    forma(palavra)
    le = input('advinhe as letras ')
    indices = [i for i, char in enumerate(palavra)]
    if le in palavra:
        for i in indices:
            if palavra[i] == le:
                lista.insert(i, le)
        print('tem')
    else:
        print('errado')
    print(lista)


def main_jogo():
    entrada(lista)
