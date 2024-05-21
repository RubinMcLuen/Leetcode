import unittest
from ValidParentheses import *

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("[]", True),
            ("([{}])", True),
            ("[(])", False)
        ]

    def test_stack(self):
        for s, expected in self.test_cases:
            solution = ValidParentheses(s)
            self.assertEqual(solution.valid_parentheses_stack(), expected)

if __name__ == "__main__":
    unittest.main()