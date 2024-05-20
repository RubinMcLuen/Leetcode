import unittest
from StringEncodeAndDecode import *

class TestStringEncodeAndDecode(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["neet","code","love","you"],"neet#code#love#you#",["neet","code","love","you"]),
            (["we","say",":","yes"],"we#say#:#yes#", ["we","say",":","yes"])
        ]
    
    def test_encode(self):
        for strs, encoded, decoded in self.test_cases:
            solution = StringEncodeAndDecode(strs, encoded)
            self.assertEqual(solution.string_encode(), encoded)

    def test_decode(self):
        for strs, encoded, decoded in self.test_cases:
            solution = StringEncodeAndDecode(strs, encoded)
            self.assertEqual(solution.string_decode(), decoded)

if __name__ == "__main__":
    unittest.main()