import unittest
from ValidSudoku import *

class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]], True),
            ([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]], False)
        ]
    
    def test_brute_force(self):
        for board, expected in self.test_cases:
            solution = ValidSudoku(board)
            self.assertEqual(solution.valid_sudoku_brute_force(), expected)

    def test_one_pass(self):
        for board, expected in self.test_cases:
            solution = ValidSudoku(board)
            self.assertEqual(solution.valid_sudoku_one_pass(), expected)

if __name__ == "__main__":
    unittest.main()