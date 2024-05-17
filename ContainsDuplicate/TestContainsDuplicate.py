import unittest
from ContainsDuplicate import *

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4], False),
            ([1, 2, 3, 1], True),
            ([1, 1, 1, 1], True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], False)
        ]

    def test_brute_force(self):
        for nums, expected in self.test_cases:
            solution = ContainsDuplicate(nums)
            self.assertEqual(solution.contains_duplicate_brute_force(), expected)

    def test_sorting(self):
        for nums, expected in self.test_cases:
            solution = ContainsDuplicate(nums)
            self.assertEqual(solution.contains_duplicate_sorting(), expected)

    def test_hashing(self):
        for nums, expected in self.test_cases:
            solution = ContainsDuplicate(nums)
            self.assertEqual(solution.contains_duplicate_hashing(), expected)

if __name__ == '__main__':
    unittest.main()
