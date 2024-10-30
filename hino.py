import os

def hinofla():
    caminho = os.path.abspath('txt/output.txt')
    with open(caminho, 'r') as fla:
        conteudo = fla.read()
    return conteudo
