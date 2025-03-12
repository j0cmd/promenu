# Biblioteca de Funções

#  tail()

from operator import mul
def tail(seq,  n=1, key=None):
    return seq[-n:] if not key else key(seq[-n:])


ver = list(tail([3, 2, 'j'], 3, reversed))
#  print(ver)

#  ====================closure=======================

def funcao_externa(val_1):

    def funcao_interna(val_2):
        return val_1 + val_2
    return funcao_interna


var_func = funcao_externa(5)

#  print(var_func(3))

def message_externa():
    dic = {'pirata': 'Ahoy', 'ingles': 'Hello', 'portugues': 'Olá'}

    def message_interna(idioma, mess2):
        print(f'{dic[idioma]} {mess2} como vai você')
        return ''

    return message_interna


menssagem = message_externa()

print(menssagem('portugues', 'josinaldo '))
print(menssagem('ingles', 'bruna'))

#  Funções Pura
#  Imutabilidade
#  Recursão e composição de funções

#  Funções integradas úteis para programação Funcional
#  . map()
#  . filter()
#  . reduce()
#  . zip()

#  Funções de Redução
#  . any()
#  . all()
#  . len()
#  .sum()

#  Funções de Mapeamento
#  . zip()
#  . reversed()
#  . enumerate()

#  lambda

#  Bibliotécas
#  . functools
#  . intertools
#  . toolz
