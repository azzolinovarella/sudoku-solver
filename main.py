from sudoku import Sudoku
import datetime as dt
import sys


try:
    algoritmo_busca = sys.argv[1].upper()  # Recebendo o algoritmo que irá realizar a busca
    input_problemas = sys.argv[2]  # Recebendo o nome do arquivo no terminal

    with open(input_problemas) as arqv:
        problemas = arqv.readlines()  # Problemas é uma lista em que cada elemente é uma string representando um problema

    if algoritmo_busca not in ['BFS', 'DFS', 'A*', 'AC3', 'BACKTRACKING']:
        print("Opção inválida!")
        sys.exit()

    T0 = dt.datetime.now()
    for problema_sudoku in problemas:
        sudoku = Sudoku(problema_sudoku)  # Cria o jogo sudoku
        print(f'========================================\n'
              f'Estado inicial:\n\n{sudoku}\n')
        t0 = dt.datetime.now()  # Iniciando a medida de tempo gasto

        if algoritmo_busca == 'BFS':
            sudoku.busca_largura()  # Inicia busca em largura
        elif algoritmo_busca == 'DFS':
            sudoku.busca_profundidade()  # Inicia busca em profundidade
        elif algoritmo_busca == 'A*':
            sudoku.busca_A_estrela()  # Inicia busca A*
        elif algoritmo_busca == 'AC3':
            sudoku.ac3()  # Inicia processo de AC-3
        else:  # i.e., Backtracking:
            sudoku.backtracking()  # Inicia busca usando backtracking

        tf = dt.datetime.now()  # Calculando tempo final
        print(f'Estado final: \n\n{sudoku}\n\n'
              f'String solução: {sudoku.solucao}\n\n'
              f'Tempo gasto: {tf-t0} (h:min:s:ms)\n'
              f'========================================\n\n')
    Tf = dt.datetime.now()
    print(f'Tempo total de execução: {Tf-T0} (h:min:s:ms)\n'
          f'Tempo médio de execução: {(Tf-T0)/len(problemas)} (h:min:s:ms)')


except (FileNotFoundError, IndexError):  # Se nao for fornecido nenhum arquivo de texto
    print('Não foi possivel acessar os dados no arquivo ou este não foi fornecido.')
    problema_sudoku = input('Insira manualmente o seu problema: ')  # Exemplo de problema: .......2143.......6........2.15..........637...........68...4.....23........7....
    algoritmo_busca = input('Insira o algoritmo que deseja usar ("BFS", "DFS", "A*", "AC3", "Backtracking"): ').upper()

    if algoritmo_busca not in ['BFS', 'DFS', 'A*', 'AC3', 'BACKTRACKING']:
        print("Opção inválida!")
        sys.exit()

    sudoku = Sudoku(problema_sudoku)
    print(f'========================================\n'
          f'Estado inicial:\n\n{sudoku}\n')
    t0 = dt.datetime.now()  # Iniciando a medida de tempo gasto

    if algoritmo_busca == 'BFS':
        sudoku.busca_largura()  # Inicia busca em largura
    elif algoritmo_busca == 'DFS':
        sudoku.busca_profundidade()  # Inicia busca em profundidade
    elif algoritmo_busca == 'A*':
        sudoku.busca_A_estrela()  # Inicia busca A*
    elif algoritmo_busca == 'AC3':
        sudoku.ac3()  # Inicia processo de AC-3
    else:  # i.e., Backtracking:
        sudoku.backtracking()  # Inicia busca usando backtracking

    tf = dt.datetime.now()  # Calculando tempo final
    print(f'Estado final: \n\n{sudoku}\n\n'
          f'String solução: {sudoku.solucao}\n\n'
          f'Tempo gasto: {tf - t0} (h:min:s:ms)\n'
          f'========================================\n\n')
