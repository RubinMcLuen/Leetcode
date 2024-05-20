import unittest
from TwoSum import *

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([2,7,11,15],9,[0,1]),
            ([3,2,4],6,[1,2]),
            ([3,3],6,[0,1])
        ]

    def test_brute_force(self):
        for nums,target,expected in self.test_cases:
            solution = TwoSum(nums, target)
            self.assertEqual(solution.two_sum_brute_force(), expected)

    def test_hashing(self):
        for nums,target,expected in self.test_cases:
            solution = TwoSum(nums, target)
            self.assertEqual(solution.two_sum_hashing(), expected)

if __name__ == '__main__':
    unittest.main()