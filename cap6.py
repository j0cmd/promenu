def print_duas_vezes(**kwargs):
    for chave, valor in kwargs.items():
       print(f'{chave}-{valor}!')


resultado = print_duas_vezes(nome='josinaldo', idade=45, profissao='programador')
print(resultado)
