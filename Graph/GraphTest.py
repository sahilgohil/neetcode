import unittest
from Graph import numIslands
class TestGraph(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]),1)
        self.assertEqual(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]),3)
if __name__ == '__main__':
    unittest.main()