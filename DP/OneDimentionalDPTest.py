from OneDimentionalDP import climbing_stairs
from practice import minCostClimbingStairs, houseRobber, houseRobber2, longestPalindrome, decodeWays, coinChange
import unittest

class TestClimbingStairs(unittest.TestCase):
    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(2), 2)
        self.assertEqual(climbing_stairs(3), 3)
    def test_min_cost_climbing_stairs(self):
        self.assertEqual(minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
    def test_house_robber(self):
        self.assertEqual(houseRobber([1, 2, 3, 4, 5]), 9)
        self.assertEqual(houseRobber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    def test_house_robber_2(self):
        self.assertEqual(houseRobber2([2,3,2]),3)
    def test_longest_palindromic_substring(self):
        self.assertEqual(longestPalindrome("cbbd"),"bb")
    def test_decode_ways(self):
        self.assertEqual(decodeWays("226"),3)
    def test_coin_change(self):
        self.assertEqual(coinChange([1,2,5], 11),3)
unittest.main()