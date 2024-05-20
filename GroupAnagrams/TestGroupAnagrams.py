import unittest
from GroupAnagrams import *

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["act","pots","tops","cat","stop","hat"],[["act", "cat"],["pots", "tops", "stop"],["hat"]]),
            (["x"],[["x"]]),
            ([""],[[""]])
        ]

    def test_sorting(self):
        for strs, expected in self.test_cases:
            solution = GroupAnagrams(strs)
            self.assertEqual(solution.group_anagrams_sorting(), expected)

    def test_hash_map(self):
        for strs, expected in self.test_cases:
            solution = GroupAnagrams(strs)
            self.assertEqual(solution.group_anagrams_hash_map(), expected)

if __name__ == "__main__":
    unittest.main()