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


msn = verificar_dia(5)
print(msn)


""" trabalhando com tipos de dados """

variavel = 123

match variavel:
    case int():
        print("A variável é um inteiro")
    case str():
        print("A variável é uma string")
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


msn2 = estruturais() 
print(msn2)
