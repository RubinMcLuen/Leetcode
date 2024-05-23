import unittest
from TwoIntegerSum import *

class TestTwoIntegerSum(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1,2,3,4], 3, [1,2])
        ]

    def test_two_integer_sum_two_pointers(self):
        for nums, target, expected in self.test_cases:
            solution = TwoIntegerSum(nums, target)
            self.assertEqual(solution.two_integer_sum_two_pointers(), expected)

if __name__ == "__main__":
    unittest.main()
    