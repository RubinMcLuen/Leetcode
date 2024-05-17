import unittest
from ValidAnagram import *

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("anagram", "nagaram", True),
            ("rat", "car", False)
        ]

    def test_brute_force(self):
        for s, t, expected in self.test_cases:
            solution = ValidAnagram(s, t)
            self.assertEqual(solution.valid_anagram_brute_force(), expected)

    def test_sorting(self):
        for s, t, expected in self.test_cases:
            solution = ValidAnagram(s, t)
            self.assertEqual(solution.valid_anagram_sorting(), expected)

if __name__ == '__main__':
    unittest.main()