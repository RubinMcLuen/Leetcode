import unittest
from CarFleet import *

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([1,4],[3,2],10,1),
            ([4,1,0,7],[2,2,1,1],10,3)
        ]
    
    def test_stack(self):
        for pos, spd, target, expected in self.test_cases:
            solution = CarFleet(pos,spd,target)
            self.assertEqual(solution.car_fleet_stack(),expected)

if __name__ == "__main__":
    unittest.main()