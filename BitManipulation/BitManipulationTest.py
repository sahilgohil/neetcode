import unittest

from BitManipulation import singleNumber, hammingWeight,missingNumber,getSum,reverse

class TestBitManipulation(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(singleNumber([2,2,1]), 1)
        self.assertEqual(singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(singleNumber([1]), 1)
    # def test_hamming_weight(self):
        # self.assertEqual(hammingWeight(1011),3)
        # self.assertEqual(hammingWeight(10011001111),7)
    def test_missing_number(self):
        self.assertEqual(missingNumber([3,0,1]),2)
    # def test_get_sum(self):
    #     self.assertEqual(getSum(1,2),3)
    #     self.assertEqual(getSum(-2,3),1)
    def test_reverse(self):
        self.assertEqual(reverse(123),321)
        self.assertEqual(reverse(-123),-321)
        self.assertEqual(reverse(120),21)

unittest.main()
