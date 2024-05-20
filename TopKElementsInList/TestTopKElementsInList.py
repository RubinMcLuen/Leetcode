import unittest
from TopKElementsInList import *

class TestTopKElementsInList(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1,2,2,3,3,3], 2, [3,2]),
            ([7,7], 1, [7])
        ]

    def test_bucket_sort(self):
        for nums, k, expected in self.test_cases:
            solution = TopKElementsInList(nums, k)
            self.assertEqual(solution.top_k_elements_in_list_bucket_sort(), expected)

if __name__ == "__main__":
    unittest.main()