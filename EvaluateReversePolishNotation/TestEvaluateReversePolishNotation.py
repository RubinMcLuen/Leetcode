import unittest
from EvaluateReversePolishNotation import *

class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["1","2","+","3","*","4","-"], 5)
        ]

    def test_stack(self):
        for tokens, expected in self.test_cases:
            solution = EvaluateReversePolishNotation(tokens)
            self.assertEqual(solution.evaluate_reverse_polish_notation_stack(), expected)

if __name__ == "__main__":
    unittest.main()