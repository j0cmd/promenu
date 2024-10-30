import opcao1
import cap2
import sorteio
import hino
import visao_das_sequencias
import separador
import dados
import mdls.metodos
import mdls.metodos_listas

opcao = -1

'''---MENU--- '''
def m_n_menu():
    n_menu = (
        (print('//////// menu ////////')),
        (print('(1) essa é a primeira opão')),
        (print('(2) Uma coleção de sequencias')),
        (print('(3) Você pode sortear uma opção para estudar.')),
        (print('(4) lindo hino do mais querido')),
        (print('(5) executa exercicio de dicionarios')),
        (print('(6) visao geral das sequencias')),
        (print('(7) analize de dados')),
        (print('(8) metodos de string')),
        (print('(9) metodos de listas'))
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
                print(opcao1.opcao1())
                m_n_menu()
            case 2:
                print(cap2.main())
                m_n_menu()
            case 3:
                print(sorteio.sorte())
                m_n_menu()
            case 4:
                print(hino.hinofla())
                m_n_menu()
            case 5:
                print('opcao 5')
                m_n_menu()
            case 6:
                print(visao_das_sequencias.visaoGeral())
                m_n_menu()
            case 7:
                print(dados.analizandoDados())
                m_n_menu()
            case 8:
                print(mdls.metodos.mainMetodos())
                m_n_menu()
            case 9:
                print(mdls.metodos_listas.metodos_list())
                m_n_menu()
            case _:
                # itens = [iten for iten in n_menu]
                if opcao >= len(menu):
                    print(len(menu))
                    print('*** digite um numero valido da lista ***')

    except:
        if opcao != int:
            print('*** OPCAO INVALIDA : ***')
