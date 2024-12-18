# compressoes de dict
""" 
Nesse modulo tem um estudo das funcionalidades dessa importante extrutura de
dados. Aprenda a extrutura e desenvolva exemplos criativos para a execução
"""
import separador

def compressoes_dict():
    separador.se('usando compressoes de dict')
    dial_codes = [
        (880, 'Bangladesh'),
        (55,  'Brazil'),
        (86,  'China'),
        (91,  'India'),
        (62,  'Indonesia'),
        (81,  'Japan'),
        (234, 'Nigeria'),
        (92,  'Pakistan'),
        (7,   'Russia'),
        (1,   'United States'),
    ]

    country_dial = {country: code for code, country in dial_codes}
    print(country_dial)

    code_in = {code: country.upper() 
               for country, code in sorted(country_dial.items()) if code < 70}
    print(code_in)



"""
Esses são alguns exemplos de como os dicionários podem ser usados em Python!
Eles são versáteis e combinam bem com diversas funcionalidades, permitindo uma
grande variedade de aplicações. O objetivo aqui é montar uma aplicação com
diversas funcionalidades onde posso escolher qual será executada sempre fazendo
uso das estruturas dos dicionarios
"""
def rhFuncionarios():
    print('ok, vamos criar um dicionario com alguns dados?')
    name = input('me diga seu nome... ')
    idade = input('sua idade... ')
    profissao = input('sua profissao... ')
    salario = input('seu salario... ')

    cadastrando = (
        ('nome', name),
        ('idade', idade),
        ('profissao', profissao),
        ('salario', salario)
    )
    cadastro = {valor: code for valor, code in cadastrando}
    # cadastro.update({'nome': name, 'idade': idade, 'profissao': profissao, 'salario': salario})
    print(cadastro)

    compressoes_dict()
    condicionais_dict()


dados = {'nome': 'joao', 'idade': 25}

# acesso aos elementos do dicionario
def acessando_elementos():
    print(dados['nome'])


# adição e atualização de items
def adicionando_elementos():
    dados['profissao'] = 'programador'
    dados['nome'] = 'josinaldo'
    dados['idade'] = 45
    print('depois dos dados adicionados ', dados)


def metodos_dicionarios():
    """
    primeira parte printa individualmente a keys, values e items do dicionario

    na segunda parte na funcao iterando_items um laço faz a iteração das chaves
    e valores
    """
    print('mostra os valores dos dados atraves dos metodos de dicionario\n')
    print(dados.keys())
    print(dados.values())
    print(dados.items())

    print('laço fazendo a iteração no dicionario\n')
    # O for é muito usado para iterar pelas chaves e valores de um dicionário.
    def iterando_items():
        for k, v in dados.items():
            print(f'chave {k} valor {v}')
    iterando_items()


def comprensao_dict():
    quadrados = {x: x**2 for x in range(1, 6)}
    print(quadrados)


def condicionais_dict():
    if dados['nome'] == 'josinaldo':
        print(f'nome encontrado {dados.keys()}')


def lambda_dict():
    pass

# acima fica o codigo
def menu():
    m = [
        (print('\n')),
        (print('dictcomp = mostra exemplos de compressoes de dicionarios')),
        (print('metodos = mostra os metodos usados em dicionarios')),
        (print('outros ...'))
    ]
    return m

# função main que chama todas as outras no sistema
def main():
    acessando_elementos()
    adicionando_elementos()
    comprensao_dict()
    menu()
    escolha = input('escolha uma opção acima ****** ')
    match escolha:
        case 'dictcomp':
            rhFuncionarios()
        case 'metodos':
            metodos_dicionarios()
        case _:
            print('nao entendi...')


