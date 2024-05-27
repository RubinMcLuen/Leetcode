import unittest
from ThreeSum import *

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
            ([0,1,1],[]),
            ([0,0,0],[[0,0,0]])
        ]

    def test_three_sum_two_pointers(self):
        for nums, expected in self.test_cases:
            solution = ThreeSum(nums)
            self.assertEqual(solution.three_sum_two_pointers(), expected)

if __name__ == "__main__":
    unittest.main()

    