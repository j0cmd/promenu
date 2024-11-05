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

# acesso aos elementos do dicionario
def acessando_elementos():
    dados = {'nome': 'joao', 'idade': 25}
    print(dados['nome'])


def main():
    print('*** dicionario em funcionamento ***')
    acessando_elementos()


main()
