import unittest
from ValidPalindrome import *

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("Was it a car or a cat I saw?", True),
            ("tab a cat", False)
        ]

    def test_valid_palindrome_two_pointers(self):
        for s, expected in self.test_cases:
            solution = ValidPalindrome(s)
            self.assertEqual(solution.valid_palindrome_two_pointers(), expected)

if __name__ == '__main__':
    unittest.main()