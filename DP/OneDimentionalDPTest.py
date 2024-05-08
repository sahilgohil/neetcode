from OneDimentionalDP import climbing_stairs
from practice import minCostClimbingStairs, houseRobber
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
unittest.main()