from typing import List

'''
Maximum Subarray

Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
'''
def maxSubArray(nums: List[int]) -> int:
    currMax = nums[0]
    currSum = nums[0]
    for i in range(1,len(nums)):
        currSum = max(0,currSum)
        currSum += nums[i]
        currMax = max(currMax,currSum)
    return currMax