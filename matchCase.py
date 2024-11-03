# match case() "aprendendo match case "

"formatação basica da instrução match case"

"""Padroes literais """
""" comparação direta com valores especificos """
def verificar_dia(dia):
    match dia:
        case 'segunda':
            return f'hoje é {dia} feira'
        case 'terça':
            return f'hoje é {dia} feira'
        case 'quarta':
            return f'hoje é {dia} feira'
        case int():
            return 'vc digitou um inteiro'
        case _:
            print('dia nao computado')




""" trabalhando com tipos de dados """
def tipos():
    variavel = ['jomaia', 'trinta', (29, 3)]

    match variavel:
        case int():
            print("A variável é um inteiro")
        case str():
            print("A variável é uma string")
        case [str(name), *anos, (int(a), int(b))] if a > 20:
            print(f'o {name} tem {anos} anos e faz aniversario dia {a, b}')
        case _:
            print("Tipo de dado não identificado")


"""Usando Padrões Estruturais"""
def estruturais():
    dados = {'nome': 'João', 'nota': 10}
    match dados:
        case {'nome': 'João', 'nota': 10}:
            print("João tirou nota 10")
        case _:
            print("Nenhuma informação obtida")
    return ''





""" Exemplo 10. Desestruturando tuplas aninhadas—requer Python ≥ 3.10 """

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:  # (1)
            case [name, _, _, (lat, lon)] if lon <= 0:  # (2)
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

    msn = verificar_dia('terça')
    print(msn)

    msn2 = estruturais() 
    print(msn2)

    tipos()
