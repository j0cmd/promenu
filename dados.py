def analizandoDados():
    d = 'analizando dados...'

    usoMap()
    return d

def usoMap():
    s = ['espada', 'copas', 'ouros', 'pedepinto']
    r = ['A', 'k', 'Q']
    baralho = [(i, li)for i in s for li in r]
    print(baralho)
