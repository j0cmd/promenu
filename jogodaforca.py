# jogo da forca
# o jogo tem como objetivo buscar uma palavra em um arquivo com varias
# aprensentará o numero de letras da mesma, e tambem a opção de digitar 
# uma letra
# se tiver a letra digitada, a palavra a letra será adicionada caso 
# contrario um erro será marcado

import os
import random
import re


def definindo_palavra():
    caminho = os.path.abspath('br_utf8.txt')

    # abrindo o arquivo
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()

    # sorteio da palavra
    if linhas:
        linha_sorteada = random.choice(linhas)
        print(f'{repr(linha_sorteada)}')
        print(len(linha_sorteada))
    return linha_sorteada.rstrip('\n')


lista = []
def forma(palavra):
    print('eee', len(palavra))
    for letra in palavra:
        lista.append('__ ')
    lista[0] = palavra[0]
    print(lista)
    print(f'Palavra com {len(lista)} letras ')


def entrada(lista):
    palavra = definindo_palavra()
    forma(palavra)
    le = ''
    while le != 'fim':
        le = input('advinhe as letras ou (fim) para terminar ')
        le = le.lower()
        indices = [i for i, char in enumerate(palavra)]
        if le in palavra:
            for i in indices:
                if palavra[i] == le:
                    lista[i] = le
            print('tem')
        else:
            print('errado')
        print(lista)


def main_jogo():
    entrada(lista)
