# MAPEAMENTO DO PYTHON
#  Classes
#  OBJETOS
#  ATRIBUTOS
#  METODOS

"""5 Classes"""

class Livro:
    # método construtor criando os atributos
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def mostrarInformacoes(self):
        print(f'titulo {self.titulo}')
        print(f'autor {self.autor}')
        print(f'genero {self.genero}')

def main_cap5():
    #  criar um objeto ou uma instancia 
    livro1 = Livro('Mapeando python', 'jo', 'informatica')
    #  acesso aos atributos de uma classe
    print(livro1.autor)
    print(livro1.genero)

    #  acesso aos metodos de uma classe
    print(livro1.mostrarInformacoes())
