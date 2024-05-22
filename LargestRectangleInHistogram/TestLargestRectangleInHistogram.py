import unittest
from LargestRectangleInHistogram import *

class TestLargestRectangleInHistogram(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([7,1,7,2,2,4],8),
            ([1,3,7],7)
        ]

    def test_largest_rectangle_in_histogram_stack(self):
        for heights, expected in self.test_cases:
            solution = LargestRectangleInHistogram(heights)
            self.assertEqual(solution.largest_rectangle_in_histogram_stack(), expected)

if __name__ == "__main__":
    unittest.main()