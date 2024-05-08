import unittest
from TDDPractice import uniquePaths

class TestTwoDimentionalDP(unittest.TestCase):
    def test_uniqpaths(self):
        self.assertEqual(uniquePaths(3,7),28)

unittest.main()