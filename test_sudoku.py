import unittest
from sudoku import Sudoku


class SudokuTest(unittest.TestCase):
    def setUp(self) -> None:
        # Os dois primeiros são fáceis
        self.sudoku1 = Sudoku('.5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4')
        self.sudoku2 = Sudoku('2.6.3......1.65.7..471.8.5.5......29..8.194.6...42...1....428..6.93....5.7.....13')
        # O terceiro é de nível médio
        self.sudoku3 = Sudoku('..45.21781...9..3....8....46..45.....7.9...128.12.35..4.......935..6.8.7.9.3..62.')
        # O último é de nível difícil
        self.sudoku4 = Sudoku('.......2143.......6.9......2.15..........6378.....7.1..689..43....23..5.....7...9')

        # Solução de cada problema
        self.solucao1 = '652483917978162435314975628825736149791824563436519872269348751547291386183657294'
        self.solucao2 = '256734198891265374347198652514683729728519436963427581135942867689371245472856913'
        self.solucao3 = '964532178187694235235817964629451783573986412841273596416728359352169847798345621'
        self.solucao4 = '857349621432861597619752843271583964945126378386497215768915432194238756523674189'

    # Verificando se há a igualdade entre o problema resulvido pelo algoritmo e as soluções
    def test_busca_largura(self):
        self.assertEqual(self.sudoku1.busca_largura(), self.solucao1)
        self.assertEqual(self.sudoku2.busca_largura(), self.solucao2)
        self.assertEqual(self.sudoku3.busca_largura(), self.solucao3)
        self.assertEqual(self.sudoku4.busca_largura(), self.solucao4)

    def test_busca_profundidade(self):
        self.assertEqual(self.sudoku1.busca_profundidade(), self.solucao1)
        self.assertEqual(self.sudoku2.busca_profundidade(), self.solucao2)
        self.assertEqual(self.sudoku3.busca_profundidade(), self.solucao3)
        self.assertEqual(self.sudoku4.busca_profundidade(), self.solucao4)

    def test_busca_A_estrela(self):
        self.assertEqual(self.sudoku1.busca_A_estrela(), self.solucao1)
        self.assertEqual(self.sudoku2.busca_A_estrela(), self.solucao2)
        self.assertEqual(self.sudoku3.busca_A_estrela(), self.solucao3)
        self.assertEqual(self.sudoku4.busca_A_estrela(), self.solucao4)

    def test_backtracking(self):
        self.assertEqual(self.sudoku1.backtracking()[1], self.solucao1)
        self.assertEqual(self.sudoku2.backtracking()[1], self.solucao2)
        self.assertEqual(self.sudoku3.backtracking()[1], self.solucao3)
        self.assertEqual(self.sudoku4.backtracking()[1], self.solucao4)

    # No caso do AC3, deseja-se verificar se é possível tornar os problemas arco-consistentes
    def test_ac3(self):
        # O primeiro inconsistente tem dois 4 em seguidas (na posição 79 e 80)
        sudoku_errado1 = Sudoku('.5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.7244')
        # O outro inconsistente atribuiu o valor errado a variável na casa 2 (o correto seria um 5 e não um 7)
        sudoku_errado2 = Sudoku('276.3......1.65.7..471.8.5.5......29..8.194.6...42...1....428..6.93....5.7.....13')

        # Validando primeiro para os problemas já dados
        self.assertTrue(self.sudoku1.ac3())
        self.assertTrue(self.sudoku2.ac3())
        self.assertTrue(self.sudoku3.ac3())
        self.assertTrue(self.sudoku4.ac3())

        # Verificando para os problemas incosistentes (deve retornar False)
        self.assertFalse(sudoku_errado1.ac3())
        self.assertFalse(sudoku_errado2.ac3())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
