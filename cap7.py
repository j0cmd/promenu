#  Esse capítulo e quase toda a Parte III do livro exploram as aplicações práticas de se tratar funções como objetos.

#  1 Atribuir uma função a uma variável
def saudacao(nome):
    return f'Olá, {nome}'


#  2 Passar uma funcao como argumento
def executar(funcao, valor):
    return funcao(valor)


def dobrar(numero):
    return numero * 2


# 3 Retornar uma função de outra função
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


# 4 Armazenar funções em estrutura de dados
def adicionar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


operacoes = {
    "soma": adicionar,
    "subtracao": subtrair
}

# 5 Usar funções em uma lista (ou iterar sobre elas)
def quadrado(x):
    return x * x

def cubo(x):
    return x * x * x


def main_cap7():
    # 1 Atribuir a função a uma variável
    diga_oi = saudacao
    print(diga_oi('Maria'))

    # 2 Passar uma funcao como argumento
    resultado = executar(dobrar, 5)
    print(resultado)
    print('executar é da ', type(executar))
    #  print(help(executar))

    # 3 Retornar uma funcao de outra funcao
    multiplicar_por_3 = criar_multiplicador(5)
    print(multiplicar_por_3(10))

    # 4 Armazenar funcões em uma estrutura de dados
    resultado_somado = operacoes["soma"](5, 10)
    resultado_subtraido = operacoes['subtracao'](4, 8)
    print(resultado_somado)
    print(resultado_subtraido)
    print(type(operacoes))

    # 5 Usar funções em uma lista (ou iterar sobre elas)
    funcoes = [quadrado, cubo]
    for funcao in funcoes:
        print(f'{funcao}', funcao(5))

    """Explicação:
    funções de primeira classe permite criar abstrações e implementações
    mais dinâmicas, contribuindo para o desenvolvimento de código modular
    e reutilizável.
    """
