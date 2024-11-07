def menu():
    menu = [ 
        (print('all')),
        (print('abs'))
    ]
    return menu


def main_functions():
    menu()
    mf = ''
    while mf != 'fim':
        mf = input('Qual funcao quer aprender? (fim) para terminar')
        match mf:
            case 'all':
                print(mfAll())


def mfAll():
    print('funcao All mostrada')
