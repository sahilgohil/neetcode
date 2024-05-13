import unittest
from TDDPractice import uniquePaths,longestCommonSubsequence,maxProfit,change,minDistance,numDistinctPractice
from TwoDimentionalDP import findTargetSumWays, isInterleave, longestIncreasingPath, numDistinct

class TestTwoDimentionalDP(unittest.TestCase):
    def test_uniqpaths(self):
        self.assertEqual(uniquePaths(3,7),28)
    def test_longestCommonSubsequence(self):
        self.assertEqual(longestCommonSubsequence("abcde", "ace"),3)
    def test_maxprofit(self):
        self.assertEqual(maxProfit([1,2,3,0,2]),3)
    def test_change(self):
        self.assertEqual(change(5 , [1,2,5]),4)
    def test_targetSumWays(self):
        self.assertEqual(findTargetSumWays([1,1,1,1,1],3),5)
    def test_is_interleave(self):
        self.assertEqual(isInterleave("aabcc","dbbca", "aadbbbaccc"),False)
        self.assertEqual(isInterleave("","", ""),True)
    def test_longest_increasing_path(self):
        self.assertEqual(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]),4)
        self.assertEqual(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]),4)
    def test_num_distinct_subsequences(self):
        self.assertEqual(numDistinct("rabbbit","rabbit"),3)
        self.assertEqual(numDistinct("babgbag","bag"),5)
        self.assertEqual(numDistinctPractice("rabbbit","rabbit"),3)
        self.assertEqual(numDistinctPractice("babgbag","bag"),5)
    def test_min_distance(self):
        self.assertEqual(minDistance("horse", "ros"), 3)
        self.assertEqual(minDistance("intention", "execution"), 5)
unittest.main()