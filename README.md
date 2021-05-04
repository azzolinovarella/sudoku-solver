# Sudoku Solver
Este projeto foi desenvolvido para a matéria "Inteligência Artificial" ministrada pelo Prof. Dr. Fabrício Olivetti de França, no primeiro quadrimestre de 2021 (2021.1) na Universidade Federal do ABC (UFABC.)
<br>

## Considerações Iniciais

Este projeto foi desenvolvido em Python utilizando a versão 3.7.0. Apesar disto, há suporte para **qualquer** versão do Python 3 (**NÃO** há suporte para Python 2).
<br>

## Instruções de execução

Para executar este projeto, basta inserir em seu terminal:

````
python -m main TIPO_DO_ALGORITMO ARQUIVO_DE_TEXTO
````
ou dependendo da versão instalada do Python deve-se executar:
````
python3 -m main TIPO_DO_ALGORITMO ARQUIVO_DE_TEXTO 
````

onde:
* TIPO_DO_ALGORITMO é o tipo de algoritmo utilizado para resolver os problemas sudoku. Esse valor pode assumir "bfs" (**Busca em largura**), "dfs" (**Busca em profundidade**), "A*" (**Busca A-estrela**), "AC3" (**Algoritmo AC-3**) ou "Backtracking" (**Busca Backtracking**)".

* ARQUIVO_DE_TEXTO é um arquivo ".txt" contendo um ou mais problemas sudoku por linhas no formato ".......2143.......6........2.15..........637...........68...4.....23........7...." (onde "." indica um espaço em branco).

Desta forma, temos como exemplos válidos de execução os seguintes comandos:
````
python -m main dfs arquivos_de_texto/teste.txt
````
````
python -m main A* arquivos_de_texto/problemas_faceis.txt
````
````
python -m main dfs arquivos_de_texto/exemplo_problemas.txt
````
Nos retornando, no caso do último exemplo (onde o primeiro problema é fácil, o segundo é médio e o último é difícil): 
````
========================================
Estado inicial:

|. 5 .|. 8 3|. 1 7|
|. . .|1 . .|4 . .|
|3 . 4|. . 5|6 . 8|
|-----+-----+-----|
|. . .|. 3 .|. . 9|
|. 9 .|8 2 4|5 . .|
|. . 6|. . .|. 7 .|
|-----+-----+-----|
|. . 9|. . .|. 5 .|
|. . 7|2 9 .|. 8 6|
|1 . 3|6 . 7|2 . 4|

Estado final:

|6 5 2|4 8 3|9 1 7|
|9 7 8|1 6 2|4 3 5|
|3 1 4|9 7 5|6 2 8|
|-----+-----+-----|
|8 2 5|7 3 6|1 4 9|
|7 9 1|8 2 4|5 6 3|
|4 3 6|5 1 9|8 7 2|
|-----+-----+-----|
|2 6 9|3 4 8|7 5 1|
|5 4 7|2 9 1|3 8 6|
|1 8 3|6 5 7|2 9 4|

String solução: 652483917978162435314975628825736149791824563436519872269348751547291386183657294

Tempo gasto: 0:00:00.004989 (h:min:s:ms)
========================================


========================================
Estado inicial:

|. . .|. . .|. 2 1|
|4 3 .|. . .|. . .|
|6 . 9|. . .|. . .|
|-----+-----+-----|
|2 . 1|5 . .|. . .|
|. . .|. . 6|3 7 8|
|. . .|. . 7|. 1 .|
|-----+-----+-----|
|. 6 8|9 . .|4 3 .|
|. . .|2 3 .|. 5 .|
|. . .|. 7 .|. . 9|

Estado final:

|8 5 7|3 4 9|6 2 1|
|4 3 2|8 6 1|5 9 7|
|6 1 9|7 5 2|8 4 3|
|-----+-----+-----|
|2 7 1|5 8 3|9 6 4|
|9 4 5|1 2 6|3 7 8|
|3 8 6|4 9 7|2 1 5|
|-----+-----+-----|
|7 6 8|9 1 5|4 3 2|
|1 9 4|2 3 8|7 5 6|
|5 2 3|6 7 4|1 8 9|

String solução: 857349621432861597619752843271583964945126378386497215768915432194238756523674189

Tempo gasto: 0:00:00.456796 (h:min:s:ms)
========================================


========================================
Estado inicial:

|. . .|. . .|. 2 1|
|4 3 .|. . .|. . .|
|6 . .|. . .|. . .|
|-----+-----+-----|
|2 . 1|5 . .|. . .|
|. . .|. . 6|3 7 .|
|. . .|. . .|. . .|
|-----+-----+-----|
|. 6 8|. . .|4 . .|
|. . .|2 3 .|. . .|
|. . .|. 7 .|. . .|

Estado final:

|8 5 7|3 4 9|6 2 1|
|4 3 2|8 6 1|5 9 7|
|6 1 9|7 5 2|8 4 3|
|-----+-----+-----|
|2 7 1|5 8 3|9 6 4|
|9 4 5|1 2 6|3 7 8|
|3 8 6|4 9 7|2 1 5|
|-----+-----+-----|
|7 6 8|9 1 5|4 3 2|
|1 9 4|2 3 8|7 5 6|
|5 2 3|6 7 4|1 8 9|

String solução: 857349621432861597619752843271583964945126378386497215768915432194238756523674189

Tempo gasto: 0:00:51.389542 (h:min:s:ms)
========================================


Tempo total de execução: 0:00:51.856036 (h:min:s:ms)
Tempo médio de execução: 0:00:17.285345 (h:min:s:ms)


````
Que são problemas sudoku iniciais seguidos suas respectivas soluções (montadas no grid e em string), o tempo gasto para cada problema e, por fim, o tempo médio de cada execução.

Obs1.: Caso o algoritmo ou o arquivo não seja fornecido no terminal, i.e., caso seja utilizado apenas:
```
python -m main
```
Uma mensagem aparecerá solicitando que o usuário insira, manualmente, o problema e o algoritmo desejado.

Obs2.: Caso seja recebido algum erro no terminal, substitua "python" por "python3", e.g.:
````
python3 -m main
````
