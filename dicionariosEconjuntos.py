# compressoes de dict
""" 
Nesse modulo tem um estudo das funcionalidades dessa importante extrutura de
dados. Aprenda a extrutura e desenvolva exemplos criativos para a execução
"""
def compressoes_dict():
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

dados = {'nome': 'joao', 'idade': 25}
# acesso aos elementos do dicionario
def acessando_elementos():
    print(dados['nome'])


# adição e atualização de items
def adicionando_elementos():
    dados['profissao'] = 'programador'
    dados['nome'] = 'josinaldo'
    dados['idade'] = 45
    print(dados)


def metodos_dicionarios():
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
    pass


# função main que chama todas as outras no sistema
def main():
    print('*** dicionario em funcionamento ***')
    acessando_elementos()
    adicionando_elementos()
    metodos_dicionarios()
    comprensao_dict()
