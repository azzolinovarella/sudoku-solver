class Sudoku:
    # Métodos 'mágicos':
    def __init__(self, problema: str) -> None:
        """
        :param problema: String contendo os valores iniciais do jogo sudoku.
        """
        problema = problema.rstrip('\n')  # Removendo possíveis '\n' implicitos na string

        self.problema = problema  # String contendo o problema (i.e., sem solução)
        self.solucao = None  # Incialmente, a solução não é preenchida (será preenchida após execução de algum algoritmo)

    def __repr__(self) -> str:
        """
        :return: Retorna o problema sudoku em formato de tabuleiro.
        """
        if self.solucao is not None:  # Se já foi encontrada alguma solução para o problema
            string_sudoku = self.solucao
        else:
            string_sudoku = self.problema  # Se não há solução, a string vai ser o problema inicial

        if len(string_sudoku) != 81:
            return 'Problema não foi inserido corretamente! Deve-se inserir um problema sudoku 9x9 (81 elementos).'

        tabuleiro = ''  # Representacao do jogo em tabuleiro --> inicialmente vazio
        n_barras = 0  # Numero de barras adicionadas na linha atual
        n_linhas = 0  # Numero de linhas completas (i.e., linha com 9 elementos)
        posicoes_barras = [x for x in range(0, 81, 3)]  # Posicoes que deve-se adicionar barras

        for pos in range(0, len(string_sudoku)):
            if pos in posicoes_barras:  # Se o valor estiver na lista de posicoes que deve-se adicionar barras
                tabuleiro += '|'  # Adiciona-se uma barra ao tabuleiro
                n_barras += 1  # Aumenta-se em 1 o numero de barras na linha
                if n_barras == 4:  # Se houver 4 barras
                    tabuleiro += '\n|'  # Vamos a proxima linha e adicionamos uma barra ao inicio desta
                    n_barras = 1  # Seta-se o numero de barras na linha para 1
                    n_linhas += 1  # Aumenta-se em 1 o numero de linhas completas
                    if n_linhas == 3:  # Se o numero de linhas completas for 3
                        tabuleiro += '-----+-----+-----|\n|'  # Adiciona-se uma linha separadora, pula-se uma linha e adiciona-se uma barra a proxima
                        n_linhas = 0  # Reseta-se o numero de linhas completas para 0
            else:
                tabuleiro += ' '  # Adicionamos um espaço como separador
            tabuleiro += string_sudoku[pos]  # Adicionamos o elemento a sua respectiva posicao no tabuleiro
        tabuleiro += '|'  # Por fim, adiciona-se uma ultima barra ao tabuleiro

        return tabuleiro  # Retorna o tabuleiro sudoku montado no formato correto

    # Métodos da classe:
    def busca_largura(self) -> str:  # a.k.a. "BFS"
        """
        :return: Solução do problema Sudoku usando busca em largura (BFS) ou uma mensagem de falha
        """
        try:
            estados = [self.problema]  # Listas de estados será, inicialmente, uma lista única contendo o estado inicial

            # "novos_estados" será a lista contendo cada novo estado, obtido pelo resultado de aplicar a acao "a" ao estado "s"
            novos_estados = [self.resultado(s, a) for s in estados for a in self.acoes(s)]

            while len(novos_estados) != 0:  # i.e., enquanto a lista novos_estados não estiver vazia
                for novo_estado in novos_estados:
                    if self.atingiu_objetivo(novo_estado):  # Se o estado atual for a solução
                        self.solucao = novo_estado  # Junta cada caracter da lista "novo_estado" para formar uma string e atualiza o estado atual
                        return self.solucao  # Retorna o estado atual que, por sua vez, é a solução
                novos_estados = [self.resultado(ns, a) for ns in novos_estados for a in self.acoes(ns)]

            return 'Não foi possível resolver o problema.'

        except MemoryError:
            print('Obtivemos um erro de memória! Não foi possível encontrar a solução do problema.')
            self.solucao = None
            return 'Não foi possível resolver o problema.'

    def busca_profundidade(self) -> str:  # a.k.a. "DFS"
        """
        :return: Solução do problema Sudoku usando busca em profundidade (DFS) ou uma mensagem de falha
        """
        try:
            estado = self.problema  # O estado atual é considerado o inicial

            if self.atingiu_objetivo(estado):  # Se o estado atual é a solução
                return estado

            fila = [estado]  # Fila inicialmente só contem o estado inicial
            while len(fila) != 0:
                acoes = self.acoes(estado)  # Ações possíveis naquele estado

                if len(acoes) != 0:
                    for a in reversed(acoes):  # Para que a expansão aconteça da esquerda para direita, usamos reversed ações
                        fila.append(self.resultado(estado, a))  # Adicionamos a fila os estados filhos de estado

                fila.remove(estado)  # Removemos o estado pai da fila
                estado = fila[-1]  # Pegamos o ultimo estado filho (primeiro estado filho da esquerda para direita)

                if self.atingiu_objetivo(estado):
                    self.solucao = estado
                    return self.solucao

            return 'Não foi possível resolver o problema.'

        except MemoryError:
            print('Obtivemos um erro de memória! Não foi possível encontrar a solução do problema.')
            self.solucao = None
            return 'Não foi possível resolver o problema.'

    # Como em nosso caso de modelagem do problema do Sudoku dois nós não podem apresentar o mesmo estado, usaremos estados como parâmetro
    def busca_A_estrela(self) -> str:  # a.k.a. A*
        """
        :return: Solução do problema Sudoku usando A* ou uma mensagem de falha
        """
        try:
            # Consideraremos que é uma lista única contendo o estado inicial
            estados = [self.problema]  # Gera uma lista a partir do estado inicial

            while len(estados) != 0:
                estado = self.melhor_estado(estados)  # Usa a heuristica e a função de custos para definir qual estado é menos custoso para expandir
                novos_estados = [self.resultado(estado, a) for a in self.acoes(estado)]  # Gera os novos estados a partir do melhor estado

                for s in novos_estados:  # Para cada estado em novos_estados, vamos verificar se algum é a solução
                    if self.atingiu_objetivo(s):
                        self.solucao = s
                        return self.solucao

                estados.remove(estado)  # Se o melhor estado ainda assim não é uma solução, removemos
                estados += novos_estados  # Adicionamos ao final da fila de estados os novos_estados

                if len(estados) == 0:  # Se a lista de estados ficar vazia, não encontramos a solução
                    return 'Não foi possível resolver o problema.'

        except MemoryError:
            print('Obtivemos um erro de memória! Não foi possível encontrar a solução do problema.')
            self.solucao = None
            return 'Não foi possível resolver o problema.'

    def ac3(self, csp: tuple = None) -> bool or str:
        """
        :param csp: Problema na modelagem CSP
        :return: Uma tupla onde o primeiro elemento é um bool indicando se o problema é arco consistente e o segundo o problema em modelo csp
        """
        try:
            if csp is None:  # Se o csp não for dado, vamos gera-lo usando uma função "gera_csp"
                csp = self.gera_csp(self.problema)  # Modela o problema como um problema csp

            fila = list(csp[2].keys())  # Fila vai ser a lista de arcos de restrição

            if len(fila) == 0:  # Se a fila está vazia, o problema já é arco consistente
                return True

            while len(fila) != 0:
                no1, no2 = fila.pop(0)  # Pegando o primeiro elemento e seu primeiro vizinho na fila
                revisado, csp = self.revisa(csp, no1, no2)  # Revisamos se os valores são validos

                if revisado:
                    D = csp[1]  # Pegamos o dominio

                    if len(D[no1]) == 0:  # Se há algum elemento com domínio 0, o problema é impossível de ser resolvido
                        return False

                    for k in self.vizinhos(no1):
                        if k != no2:
                            fila.append((k, no1))  # Para cada vizinho do no1 diferente do já verificado, o adicionamos a lista

            X, D, C = csp

            # Se o domínio de todos os nós tiverem apenas um elemento alcançamos a solução
            if all([len(D[k]) == 1 for k in D.keys()]):
                self.solucao = ''
                for x in X:
                    self.solucao += D[x].copy().pop()  # Adicionamos o valor a string "self.solucao"

            return True

        except MemoryError:
            print('Obtivemos um erro de memória! Não foi possível encontrar a solução do problema.')
            self.solucao = None
            return 'Não foi possível resolver o problema.'

    def backtracking(self, csp: tuple = None, atribuicao: dict = None) -> (dict, str):
        """
        :param csp: Problema na modelagem CSP
        :param atribuicao: Dicionário em que a chave é o nó e o valor é o número atribuido a ele (de 0 a 9)
        :return: Dicionário de atribuições e string do problema resolvido
        """
        try:
            if csp is None:  # Se o csp não foi dado, vamos obte-lo por tornar o problema arco consistente
                csp = self.gera_csp(self.problema)

            if atribuicao is None:  # Se atribuicao não foi dada será, inicialmente, um dict vazio
                atribuicao = {}

            X, D, C = csp
            D_0 = D.copy()  # Faremos uma cópia do domínio para voltarmos a ele caso o problema se torne inconcistente

            if len(atribuicao) == len(X):  # Se o número de valores atribuidos for igual ao de vars, alcançamos a solução
                self.solucao = "".join([atribuicao.get(x, ".") for x in sorted(X)])
                return atribuicao, self.solucao

            no = self.seleciona_var(csp, atribuicao)  # Selecionamos o melhor nó para expandirmos

            for v in self.ordena_valores(no, csp, atribuicao):
                if self.consistente(no, v, atribuicao):  # Se for possível atribuir aquele valor ao nó
                    atribuicao[no] = v
                    D[no] = {v}  # Como o atribuimos o valor à variável, mudaremos o csp
                    csp = X, D, C

                    arco_consistente = self.ac3(csp)  # Faremos uma verificação para ver se o problema é AC

                    if arco_consistente is True:  # Se o problema for arco consistente, prosseguiremos
                        atribuicao_n, solucao = self.backtracking(csp, atribuicao)
                        if len(atribuicao_n) != 0:
                            return atribuicao_n, self.solucao

                    del atribuicao[no]

                    D = D_0  # Se não chegamos na conclusão, devemos retornar ao domínio inicial

            return {}, None

        except (MemoryError, RecursionError):
            print('Obtivemos um erro de memória ou Recursão! Não foi possível encontrar a solução do problema.')
            self.solucao = None
            return 'Não foi possível resolver o problema.'

    # Métodos estáticos:
    @staticmethod
    def acoes(estado: str) -> list:
        """
        :param estado: É uma string que representa o estado do agente
        :return: Uma lista contendo as ações possíveis para o estado fornecido
        """
        estado = list(estado)  # Transformando o estado fornecido em uma lista onde cada elemento é um numero/ponto
        pos = estado.index('.')  # pos é a primeira posição não preenchida (i.e., que contem um ".")
        linha = []  # Inicialmente a linha em que aquele caracter está uma lista vazia que será preenchida no loop for
        coluna = []  # Inicialmente a coluna em que aquele caracter está uma lista vazia que será preenchida no loop for
        quadrante = []  # Inicialmente o quadrange em que aquele caracter está uma lista vazia que será preenchida no loop for

        for i in range(0, 9):
            # Pegando a linha em que aquele elemento está:
            if pos in range(i * 9, (i + 1) * 9):
                linha = set(estado[i * 9: (i + 1) * 9])
            # Pegando a coluna em que aquele elemento está:
            if pos in range(i, (i + 81), 9):
                coluna = set(estado[i: (i + 81): 9])
            # Para evitar trabalhos desnecessários (se ja encontramos a linha e a coluna):
            if linha != [] and coluna != []:
                break

        # Pegando quadrante em que aquele elemento está:
        for i in range(0, 81, 27):
            for j in range(i, i + 9, 3):
                if pos in range(j, j + 3) or pos in range(j + 9, j + 12) or pos in range(j + 18, j + 21):
                    quadrante = set(estado[j: j + 3] + estado[j + 9: j + 12] + estado[j + 18: j + 21])

        valores_proibidos = linha.union(coluna,
                                        quadrante)  # Juntando o conjunto dos numeros não permitidos (i.e., que já exitem na linha, coluna e/ou quadrante)
        valores_proibidos.remove(
            '.')  # Removendo '.' dos valores proibidos pois só serve para sinalizar que há um espaço livre
        num_possiveis = list({f'{i}' for i in range(1, 10)}.difference(valores_proibidos))  # Lista de números possíveis
        num_possiveis.sort()  # Apenas para manter padrão e termos certeza que vamos retornar os numeros possíveis em ordem
        return num_possiveis

    @staticmethod
    def resultado(estado: str, acao: str) -> str:
        """
        :param estado: É uma string que representa o estado do agente
        :param acao: É a ação que este agente ira fazer
        :return: O novo estado obtido após aplicação da ação no estado dado
        """
        novo_estado = estado.replace('.', acao, 1)  # Trocaremos o primeiro '.' pelo valor fornecido na ação
        return novo_estado

    @staticmethod
    def atingiu_objetivo(estado: str) -> bool:
        """
        :param estado: É uma string que representa o estado do agente
        :return: Retorna True se chegamos na solução correta ou False se a solução é invalida ou não está completa
        """
        if '.' in estado:
            return False

        estado = list(estado).copy()

        lista_linhas = [estado[i * 9:(i + 1) * 9] for i in range(0, 9)]  # Pega todas as linhas
        lista_colunas = [estado[i:i + 81:9] for i in range(0, 9)]  # Pega todas as colunas
        lista_quadrantes = [
            estado[i + j:(i + j) + 3] + estado[(i + j) + 9:(i + j) + 12] + estado[(i + j) + 18:(i + j) + 21]
            for i in range(0, 81, 27) for j in range(0, 9, 3)]  # Pega todos os quadrantes

        set_elementos = {f'{i}' for i in range(1, 10)}  # Set que contem os elementos que cada lista deve conter (usado para verificação)

        for linha, coluna, quadrante in zip(lista_linhas, lista_colunas, lista_quadrantes):
            # Se o conjunto de elementos da lista, coluna ou quadrante não for igual a {1,2,3,4,5,6,7,8,9} houve repetição e poranto a solução é inválida
            if set(linha) != set_elementos or set(coluna) != set_elementos or set(quadrante) != set_elementos:
                return False

        return True

    @staticmethod
    def custo(estado: str) -> int:  # g(n)
        """
        :param estado: É uma string que representa o estado do agente
        :return: Custo para irmos do nó inicial até o atual
        """
        # É a quantidade de movimentos possíveis (i.e., o tamanho da lista de ações) para o primeiro '.' do estado
        g = len(Sudoku.acoes(estado))
        return g

    @staticmethod
    def heuristica(estado: str) -> int:  # h(n)
        """
        :param estado: É uma string que representa o estado do agente
        :return:  Uma estimativa otimista de quantos valores devem ser inseridos para chegarmos na solução
        """
        # Conta a quantidade de '.' que existem no problema e, portanto, a quantidade de casas vazias (que é a quantidade minima de movimentos para resolver o problema)
        h = estado.count('.')
        return h

    @staticmethod
    def melhor_estado(estados: list) -> str:
        """
        :param estados: É uma string que representa o estado do agente
        :return: Retorna o estado menos custoso
        """
        menor_peso = Sudoku.heuristica(estados[0]) + Sudoku.custo(estados[0])  # Menor peso é, inicialmente, o do primeiro estado
        estado_menor_peso = estados[0]

        for estado in estados:
            if Sudoku.heuristica(estado) + Sudoku.custo(estado) < menor_peso:  # Se o peso do estado é o menor
                menor_peso = Sudoku.heuristica(estado) + Sudoku.custo(estado)
                estado_menor_peso = estado  # Estado é o estado menos custoso da lista

        return estado_menor_peso

    @staticmethod
    def gera_csp(problema: str) -> tuple:
        """
        :param problema: Problema sudoku em uma string
        :return: Problema modelado como um CSP
        """
        X = list()  # Posição de cada casa do tabuleiro
        D = dict()  # Conjunto de numeros de 1 a 9 que podem ser colocados naquela casa = {1, 2, ..., 9} para todos os nós
        C = dict()  # Dicionário onde chave é tupla de nós vizinhos e valor conjuntos de valores adimissíveis

        # Nest loop vamos preencher X e C
        for i in range(0, len(problema)):
            # Quem sabe mudar para algo do tipo "ij" onde "i" é linha e "j" coluna?
            X.append(i)  # Cada elemento do sudoku vai ser visto como sua posição na string input

            if problema[i] == '.':
                D[X[i]] = {str(n) for n in range(1, 10)}

            else:
                # Como a casa já é preenchida, consideraremos que X[i] é uma variável que só pode assumir um valor (i.e., constante)
                D[X[i]] = {str(problema[i])}

        # Restrições é o conjunto de (no, no_vizinho)
        for i in X:
            for j in Sudoku.vizinhos(i):
                C[(i, j)] = {(a, b) for a in D[i] for b in D[j] if a != b}

        return X, D, C

    @staticmethod
    def vizinhos(no: int) -> set:
        """
        :param no: Valor inteiro que representa uma posição no problema sudoku (vai de 0 a 80)
        :return: Set contendo todos os vizinhos daquele nó
        """
        n_linha = no // 9
        n_coluna = no % 9

        # Elementos vizinhos do no:
        viz_linha = [n for n in range(9 * n_linha, 9 * (n_linha + 1)) if n != no]
        viz_coluna = [n for n in range(n_coluna, n_coluna + 81, 9) if n != no]
        viz_quadrante = [n for k in range(0, 81, 27) for m in range(k, k + 9, 3)
                         for n in list(range(m, m + 3)) + list(range(m + 9, m + 12)) + list(range(m + 18, m + 21))
                         if no in range(m, m + 3) or no in range(m + 9, m + 12) or no in range(m + 18, m + 21)
                         if n != no]

        vizinhos = set(viz_linha + viz_quadrante + viz_coluna)  # Será o conjunto dos vizinhos na linha, coluna e quadrante

        return vizinhos

    @staticmethod
    def revisa(csp: tuple, no1: int, no2: int):
        """
        :param csp: Problema na modelagem CSP
        :param no1: Nó que terá seu domínio revisado
        :param no2: Nó que possivelmente mudará o dominio do no1
        :return: Indica se algo mudou no csp e, caso sim, o que mudou no dominio da variável
        """
        X, D, C = csp

        # Violam é o conjunto de valores de x que não permitidos em seu domínio
        violam = {x for x in D[no1] if len([(x, y) in C[no1, no2] for y in D[no2] if y != x]) == 0}

        if len(violam) != 0:  # Se existir pelo menos um valor de x que não é permitido em seu domínio
            D[no1] = D[no1].difference(violam)

            return True, (X, D, C)

        return False, csp

    @staticmethod
    def consistente(no: int, valor: int, atribuicao: dict) -> bool:
        """
        :param no: Valor inteiro que representa uma posição no problema sudoku (vai de 0 a 80)
        :param valor: Valor que deseja verificar se é ou não consistente para aquele nó
        :param atribuicao: Dicionário que contem os valores atribuidos a cada nó
        :return: Um booleano falando se é possível ou não atribuir aquele valor àquele nó
        """
        viz = Sudoku.vizinhos(no)
        for v in viz:
            if v in atribuicao.keys() and atribuicao[v] == valor:  # Verificamos se é possível adicionar aquele valor ao no
                return False

        return True

    @staticmethod
    def seleciona_var(csp: tuple, atribuicao: dict) -> int:
        """
        :param csp: Problema modelado como um csp
        :param atribuicao: Dicionário que contem os valores atribuidos a cada nó
        :return: A variável que é do tipo "falha primeiro", i.e., qual o nó que deve ser escolhido
        """
        # Deve "Falhar primeiro"
        X, D, C = csp

        aux_D = D.copy()
        [aux_D.pop(k) for k in atribuicao.keys()]

        var = min(aux_D, key=lambda key: len(aux_D[key]))  # Valor com o menor domínio possível

        return var

    @staticmethod
    def ordena_valores(no: int, csp: tuple, atribuicao: dict) -> list:
        """
        :param no: Valor inteiro que representa uma posição no problema sudoku (vai de 0 a 80)
        :param csp: Problema modelado como um csp
        :param atribuicao: Dicionário que contem os valores atribuidos a cada nó
        :return: Uma lista ordenando o domínio daquele nó em ordem de "Falha por ultimo"
        """
        X, D, C = csp

        viz = Sudoku.vizinhos(no)

        # É uma lista de tuplas onde o primeiro elemento é o valor e o segundo a ocorrencia dele no dominio de seus vizinhos
        valor_ocor = [(valor, sum([valor in D[v] for v in viz])) for valor in D[no] if no not in atribuicao.keys()]

        valor_ocor.sort(key=lambda t: t[1])
        valores = [v[0] for v in valor_ocor]  # Ordenação do valor com menos ocorrencia em cada vizinho

        return valores

