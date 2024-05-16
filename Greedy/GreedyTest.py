import unittest

from Greedy import maxSubArray

class TestGreedy(unittest.TestCase):

    def test_max_sum_subarray(self):
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
unittest.main()