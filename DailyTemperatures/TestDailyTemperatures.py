import unittest
from DailyTemperatures import *

class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([30,38,30,36,35,40,28],[1,4,1,2,1,0,0]),
            ([22,21,20],[0,0,0])
        ]

    def test_stack(self):
        for temperatures, expected in self.test_cases:
            solution = DailyTemperatures(temperatures)
            self.assertEqual(solution.daily_temperatures_stack(), expected)

if __name__ == "__main__":
    unittest.main()

    