"""5 Classes de dados"""
# -------------FABRICA DE CLASSES---------------
#  A ideia desses capitulos iniciais do livro é falar de opcoes 
#  pre prontas que o python oferece, posteriomente iremos ver como
#  podemos criar nossos proprios OBJETOS

#  vamos ver tres diferentes fabricas de classe
#  1º collections.NamadTuple
#  2º typing.NamadTuple
#  3º @dataclasses.dataclass


import separador
from collections import namedtuple
from typing import NamedTuple
import os
from dataclasses import dataclass
import cap5_a

#  separador.se('namedtuple')
#  especificando as categorias
def produtosUsados():
    Produto = namedtuple('Produto', 'tipo marca quantidade preço')
    Ferramentas = namedtuple('Ferramentas', ['nome', 'preço', 'quantidade'])

    todosOsProdutos(Produto, Ferramentas)

#  especificando os produtos
def todosOsProdutos(Produto, Ferramentas):
    tomadas = Produto('tomada', 'energiza', 40, 15.50)
    fios = Produto('fio', 'energiza', '15kg', '125,00')
    alicate = Ferramentas('Alicate', '17,30', '01')

    lista_itens = [fios, tomadas, alicate]
    for itens in lista_itens:
        print('comprados ', itens)


#  separador.se('@dataclass')


#  classe comum
class Pessoa:
    def __init_(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa (nome = {self.nome}, idade = {self.idade})'


@dataclass(frozen=True)
class Pessoas:
    nome: str
    idade: int

    def estudando(self):
        print(f'Eu {self.nome} estou estudando python fluente \
              aos {self.idade} anos')


@dataclass
class Person:
    fastname: str
    lastname: str


if __name__ == '__main__':
    jo1 = Person('jo', 'maia')
    jo2 = Person('jo', 'maia')
    maria = Person('mary', 'jane')
    print('jo1 == jo2 ', (jo1 == jo2))


def resumo():
    caminho = os.path.abspath('txt/cap5.md')
    with open(caminho, 'r') as texto:
        conteudo = texto.read()
    print(conteudo)


separador.se('codigo')
def main_cap5():
    separador.se('namedtuple')
#   especificando as categorias
    produtosUsados()
    print('\n')
    separador.se('@dataclass')
    pessoa1 = Pessoas('jo', 45)
    pessoa1.estudando()
    pessoa2 = Pessoas('maria', 15)
    print(pessoa2)
    print(pessoa1)
    print(type(pessoa1), '\n')
    resumo()
    print(cap5_a.order1)
