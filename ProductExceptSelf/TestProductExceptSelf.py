import unittest
from ProductExceptSelf import *

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1,2,4,6],[48,24,12,8]),
            ([-1,0,1,2,3],[0,-6,0,0,0])
        ]

    def test_brute_force(self):
        for nums, expected in self.test_cases:
            solution = ProductExceptSelf(nums)
            self.assertEqual(solution.product_except_self_brute_force(), expected)

    def test_division(self):
        for nums, expected in self.test_cases[:-1]:
            solution = ProductExceptSelf(nums)
            self.assertEqual(solution.product_except_self_division(), expected)

    def test_prefix_suffix(self):
        for nums, expected in self.test_cases:
            solution = ProductExceptSelf(nums)
            self.assertEqual(solution.product_except_self_prefix_suffix(), expected)

if __name__ == "__main__":
    unittest.main()