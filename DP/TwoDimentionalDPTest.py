import unittest
from TDDPractice import uniquePaths,longestCommonSubsequence,maxProfit,change

class TestTwoDimentionalDP(unittest.TestCase):
    def test_uniqpaths(self):
        self.assertEqual(uniquePaths(3,7),28)
    def test_longestCommonSubsequence(self):
        self.assertEqual(longestCommonSubsequence("abcde", "ace"),3)
    def test_maxprofit(self):
        self.assertEqual(maxProfit([1,2,3,0,2]),3)
    def test_change(self):
        self.assertEqual(change(5 , [1,2,5]),4)
unittest.main()