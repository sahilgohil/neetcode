import unittest

from BitManipulation import singleNumber, hammingWeight

class TestBitManipulation(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(singleNumber([2,2,1]), 1)
        self.assertEqual(singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(singleNumber([1]), 1)
    # def test_hamming_weight(self):
        # self.assertEqual(hammingWeight(1011),3)
        # self.assertEqual(hammingWeight(10011001111),7)

unittest.main()