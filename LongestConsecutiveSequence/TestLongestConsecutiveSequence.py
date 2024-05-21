import unittest
from LongestConsecutiveSequence import *

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([2,20,4,10,3,4,5], 4),
            ([0,3,2,5,4,6,1,1], 7)
        ]

    def test_hash_set(self):
        for nums, expected in self.test_cases:
            solution = LongestConsecutiveSequence(nums)
            self.assertEqual(solution.longest_consecutive_sequence_hash_set(), expected)

if __name__ == "__main__":
    unittest.main()