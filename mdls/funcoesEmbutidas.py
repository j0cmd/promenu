""" nesse módulo o objetivo é mostrar como usa e para que serve todas
as funcoes embutidas do python"""

import os
import separador

def menu():
    menu = [
        (print('all')),
        (print('abs')),
        ]
    return menu


def main_functions():
    """ funcao principal """
    mf = ''
    while mf != 'fim':
        menu()
        mf = input('Qual funcao quer aprender? (fim) para terminar ')
        separador.se('codigo')
        match mf:
            case 'abs':
                print(mfabs())
            case 'all':
                print(mfAll())

def mfabs():
    caminho = os.path.abspath('txt/abs.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def mfAll():
    caminho = os.path.abspath('txt/all.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def mfany():
    pass


def mfascii():
    pass


def mfbim():
    pass


def mfbool():
    pass


def mfbytearray():
    pass


def mfbytes():
    pass


def mfcallable():
    pass


def mfchr():
    pass
