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