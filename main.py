import sorteio, separador
import cap2, cap3, cap4, cap5, cap7
import mdls.metodos_listas
from mdls import funcoesEmbutidas, metodos
import jogos.jogodaforca

opcao = -1

'''---MENU---  '''


def m_n_menu():
    """
    docstring
    """
    n_menu = (
        (print('//////// menu ////////')),
        (print('(1) sorteio de um capitulo do livro para estudo')),
        (print('(2) Uma coleção de sequencias')),
        (print('(3) dicinario e conjuntos.')),
        (print('(4) Texto em Unicode versus Bytes')),
        (print('(5) Fábrica de classes de dados')),
        (print('(6) visao geral das sequencias')),
        (print('(7) Parte ||: Funções como objetos')),
        (print('(8) metodos de string')),
        (print('(9) metodos de listas')),
        (print('(10) match case')),
        (print('(11) dicionarios')),
        (print('(12) funcoes embutidas')),
        (print('(25) jogos')),
    )
    return n_menu


menu = m_n_menu()


while opcao != 0:
    try:
        opcao = int(input('=== escolha uma opção: ou (0) para sair: ==='))
        print('='*46)
        separador.se('codigo')
        match opcao:
            case 1:
                print(sorteio.sorte())
                m_n_menu()
            case 2:
                print(cap2.mainCap2())
                m_n_menu()
            case 3:
                print(cap3.main())
                m_n_menu()
            case 4:
                print(cap4.main_cap4())
                m_n_menu()
            case 5:
                print(cap5.main_cap5())
                m_n_menu()
            case 6:
                print()
                m_n_menu()
            case 7:
                print(cap7.main_cap7())
                m_n_menu()
            case 8:
                print(metodos.mainMetodos())
                m_n_menu()
            case 9:
                print(mdls.metodos_listas.metodos_list())
                m_n_menu()
            case 10:
                print()
                m_n_menu()
            case 11:
                print()
                m_n_menu()
            case 12:
                print(funcoesEmbutidas.main_functions())
                m_n_menu()
            case 25:
                print(jogos.jogodaforca.main_jogo())
                m_n_menu()
            case _:
                if opcao >= len(menu):
                    print(f'*** digite um numero valido da\
                          lista entre 1 e {len(menu) - 1} ***')
                elif opcao <= -1:
                    print('numero negativo .')

    except ValueError:
        print('digite um numero valido')
