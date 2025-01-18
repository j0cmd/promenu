2.2. Uma visão geral das sequências embutidas

A biblioteca padrão oferece uma boa seleção de tipos de sequências, implementadas em C:

Sequências contêiner

    Podem armazenar itens de tipos diferentes, incluindo contêineres aninhados e objetos de qualquer tipo. Alguns exemplos: list, tuple, e collections.deque.
Sequências planas

    Armazenam itens de algum tipo simples, mas não outras coleções ou referências a objetos. Alguns exemplos: str, bytes, e array.array.

Uma sequência contêiner mantém referências para os objetos que contém, que podem ser de qualquer tipo, enquanto uma sequência plana armazena o valor de seu conteúdo em seu próprio espaço de memória, e não como objetos Python distintos.



Outra forma de agrupar as sequências é por mutabilidade:

Sequências mutáveis

    Por exemplo, list, bytearray, array.array e collections.deque.
Sequências imutáveis

    Por exemplo, tuple, str, e bytes.

A Figura 2 ajuda a visualizar como as sequências mutáveis herdam todos os métodos das sequências imutáveis e implementam vários métodos adicionais. Os tipos embutidos concretos de sequências na verdade não são subclasses das classes base abstratas (ABCs) Sequence e MutableSequence, mas sim subclasses virtuais registradas com aquelas ABCs—como veremos no Capítulo 13. Por serem subclasses virtuais, tuple e list passam nesses testes:

>>> from collections import abc
>>> issubclass(tuple, abc.Sequence)
True
>>> issubclass(list, abc.MutableSequence)
True



Lembre-se dessas características básicas: mutável versus imutável; contêiner versus plana. Elas ajudam a extrapolar o que se sabe sobre um tipo de sequência para outros tipos.

O tipo mais fundamental de sequência é a lista: um contêiner mutável. Espero que você já esteja muito familiarizada com listas, então vamos passar diretamente para a compreensão de listas, uma forma potente de criar listas que algumas vezes é subutilizada por sua sintaxe parecer, a princípio, estranha. Dominar as compreensões de listas abre as portas para expressões geradoras que—entre outros usos—podem produzir elementos para preencher sequências de qualquer tipo. Ambas são temas da próxima seção.

