import os
import separador


def menu():
    menu = [(print(separador.se('metodos de listas'))),
            (print('metodo append')),
            (print('metodo extend')),
            ]
    return menu


def metodos_list():
    menu()
    opcao = ''
    while opcao != 'fim':
        opcao = input('digite um metodo, ou fim para sair ')
        match opcao:
            case 'append':
                print(metodo_append())
                menu()
            case 'extend':
                print(metodo_extend())
                menu()
            case _:
                print('precisa escolher uma opcao valida')


def metodo_append():
    caminho = os.path.abspath('txt/append.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_extend():
    caminho = os.path.abspath('txt/extend.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo
