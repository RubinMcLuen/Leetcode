import unittest
from GenerateParentheses import *

class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1, ["()"]),
            (3, ["((()))","(()())","(())()","()(())","()()()"])
        ]

    def test_stack(self):
        for n, expected in self.test_cases:
            solution = GenerateParentheses(n)
            self.assertEqual(solution.generate_parentheses_stack(), expected)

if __name__ == "__main__":
    unittest.main()