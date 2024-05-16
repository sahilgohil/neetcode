import unittest

from Greedy import maxSubArray, canJump

class TestGreedy(unittest.TestCase):

    def test_max_sum_subarray(self):
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
    def test_can_jump(self):
        self.assertEqual(canJump([3,2,1,1,4]),True)
        self.assertEqual(canJump([3,2,1,0,4]),False)
unittest.main()