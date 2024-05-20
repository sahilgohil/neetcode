from typing import List

'''
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    return res

'''
Number of 1 bits

Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).
'''
def hammingWeight(n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res

'''
Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
def countBits(n: int) -> List[int]:
    dp = [0] * (n+1)
    offset = 1
    for i in range(1, len(dp)):
        if offset * 2 == i:
            offset = i
        dp[i] = dp[i-offset]
        
    return dp


'''
Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
'''

def reverseBits(n: int) -> int:
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31-i))

    return res