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
    name = input('nome ')
    idade = input('idade ')
    profissao = input('profissao ')
    salario = input('salario ')

    cadastrando = [
        ('nome', name),
        ('idade', idade),
        ('profissao', profissao),
        ('salario', salario)
    ]
    cadastro = {valor: code for valor, code in cadastrando}
    # cadastro.update({'nome': name, 'idade': idade, 'profissao': profissao, 'salario': salario})
    print(cadastro)


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
    print(dados.keys())
    print(dados.values())
    print(dados.items())

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


# função main que chama todas as outras no sistema
def main():
    acessando_elementos()
    adicionando_elementos()
    metodos_dicionarios()
    comprensao_dict()
    condicionais_dict()
    compressoes_dict()
    escolha = input('escolha ')
    match escolha:
        case 'dictcomp':
            rhFuncionarios()
        case _:
            print('nao entendi...')
