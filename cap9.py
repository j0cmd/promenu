# funções como objetos de primeira classe               

def suma(a, b):
    return a + b

def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calculadora(op, a, b):
    """ funções dentro de um dicionario atribuida a uma variavel """
    operacoes = {
        '+': suma,
        '-': sub,
        '*': mul,
        '/': div,
    }
    return operacoes[op](a, b)

# Funções de ordem superior

from functools import reduce


def soma(a, b):
    """ funcao criada para ser usada com a superior """
    return a + b


#  resultado = reduce(soma, [1, 2, 3, 4, 5, 6])
#  print('a soma foi ', resultado)

#  _______________________  usando outro exemplo ______________________________

def maior_que_5(num):
    return num > 5


#  resultado = filter(maior_que_5, [1, 2, 3, 4, 5, 6, 7, 8])
#  print(list(resultado))


#  _______________________ função que retorna outra função ____________________

from functools import partial

def somar(x, y):
    return x + y


# Exemplo personalizado
def soma_um(x):
    return x + 1

def soma_duas_vezes(func, num):
    return func(func(num))


#  print(soma_duas_vezes(soma_um, 2))

#  Funções aninhadas

def ola(nome):
    def func_interna(nome):
        if nome.lower() == 'maria':
            print(f'Ola {nome} como vai')
        else:
            print(f'Ola {nome}, boas vindas')
    func_interna(nome)

#  ___________________ chamada do app _____________________
def main_cap9():
    # Neste exemplo Funções como parametro, como objetos

    resultado = reduce(soma, [1, 2, 3, 4, 5, 6])
    print('a soma foi ', resultado)

    resultado = filter(maior_que_5, [1, 2, 3, 4, 5, 6, 7, 8])
    print(list(resultado))

    #  neste exemplo partial retorna não um objeto, mas uma função!
    soma_1 = partial(somar, 1)
    soma_2 = partial(somar, 1)
    print(soma_1(5) + soma_2(10))
    print(soma_2(6))

    print('exemplo personalizado ', soma_duas_vezes(soma_um, 2))

    ola('maria')

    return ''
