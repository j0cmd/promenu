import os

def menu():
    menu = [(print('método len')),
            (print('método capitalize')),
            (print('método upper')),
            (print('metodo lower')),
            (print('metodo count')),
            (print('metodo find')),
            (print('metodo rfind')),
            (print('metodo startswith')),
            (print('metodo endswith')),
            (print('metodo index')),
            (print('metodo split')),
            (print('metodo rsplit')),
            (print('metodo join')),
            (print('metodo strip')),
            (print('metodo lstrip')),
            (print('metodo rstrip')),
            (print('metodo removeprefix')),
            (print('metodo removesuffix')),
            (print('metodo replace')),
            (print('metodo format')),
            (print('metodo center')),
            (print('metodo ljust')),
            (print('metodo rjust')),
            (print('metodo partition')),
            (print('(resumo) ver todos os metodos'))
            ]
    return menu

def mainMetodos():
    menu()
    opcao = ''
    while opcao != 'fim':
        opcao = input('Digite um metodo ou Digite fim: ')
        match opcao:
            case 'len':
                print(metodo_len())
                menu()
            case 'capitalize':
                print(metodo_capitalize())
                menu()
            case 'upper':
                print(metodo_upper())
                menu()
            case 'lower':
                print(metodo_lower())
                menu()
            case 'count':
                print(metodo_count())
                menu()
            case 'find':
                print(metodo_find())
                menu()
            case 'rfind':
                print(metodo_rfind())
                menu()
            case 'startswith':
                print(metodo_startswith())
                menu()
            case 'endswith':
                print(metodo_endswith())
                menu()
            case 'index':
                print(metodo_index())
                menu()
            case 'split':
                print(metodo_split())
                menu()
            case 'rsplit':
                print(metodo_rsplit())
                menu()
            case 'join':
                print(metodo_join())
                menu()
            case 'strip':
                print(metodo_strip())
                menu()
            case 'lstrip':
                print(metodo_lstrip())
                menu()
            case 'rstrip':
                print(metodo_rstrip())
                menu()
            case 'removeprefix':
                print(metodo_removeprefix())
                menu()
            case 'removesuffix':
                print(metodo_removesuffix())
                menu()
            case 'replace':
                print(metodo_replace())
                menu()
            case 'format':
                print(metodo_format())
                menu()
            case 'center':
                print(metodo_center())
                menu()
            case 'ljust':
                print(metodo_ljust())
                menu()
            case 'rjust':
                print(metodo_rjust())
                menu()
            case 'partition':
                print(metodo_partition())
                menu()
            case 'resumo':
                print(resumo())
                menu()
            case _:
                print('error')

    return opcao


# Abaixo todos os métodos
def metodo_len():
    caminho = os.path.abspath('txt/len.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_capitalize():
    caminho = os.path.abspath('txt/capitalize.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_upper():
    try:
        caminho = os.path.abspath('txt/uper.txt')
        with open(caminho, 'r') as texto:
            conteudo = texto.read()
        return conteudo

    except FileNotFoundError:
        return 'Arquivo nao encontrado'


def metodo_lower():
    try:
        caminho = os.path.abspath('txt/lower.txt')
        with open(caminho, 'r') as texto:
            conteudo = texto.read()
            return conteudo

    except FileNotFoundError:
        return 'Arquivo nao encontrado'
    except NameError:
        return 'erro, tente o nome novamente'


def metodo_count():
    caminho = os.path.abspath('txt/count.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    print(conteudo)


def metodo_find():
    caminho = os.path.abspath('txt/find.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    diga = conteudo.find('Sintaxe')
    print('diggggggggggggggga', diga)
    return conteudo


def metodo_rfind():
    caminho = os.path.abspath('txt/rfind.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_startswith():
    caminho = os.path.abspath('txt/startswith.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_endswith():
    caminho = os.path.abspath('txt/endswith.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_index():
    caminho = os.path.abspath('txt/index.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_split():
    caminho = os.path.abspath('txt/split.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_rsplit():
    caminho = os.path.abspath('txt/rsplit.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_join():
    caminho = os.path.abspath('txt/join.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_strip():
    caminho = os.path.abspath('txt/strip.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_lstrip():
    caminho = os.path.abspath('txt/lstrip.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_rstrip():
    caminho = os.path.abspath('txt/rstrip.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_removeprefix():
    caminho = os.path.abspath('txt/removeprefix.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_removesuffix():
    caminho = os.path.abspath('txt/removesuffix.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_replace():
    caminho = os.path.abspath('txt/replace.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_format():
    caminho = os.path.abspath('txt/format.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_center():
    caminho = os.path.abspath('txt/center.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_ljust():
    caminho = os.path.abspath('txt/ljust.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_rjust():
    caminho = os.path.abspath('txt/rjust.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def metodo_partition():
    caminho = os.path.abspath('txt/partition.txt')
    with open(caminho, 'r', encoding='utf-8') as texto:
        conteudo = texto.read()
    return conteudo


def resumo():
    caminho = os.path.abspath('txt/resumo.txt')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    return conteudo
