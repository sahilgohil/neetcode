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

'''
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Solution is :
start from the last index and check if the jump from that index is greater or equal to the goal then we can shift the goal to closer point to starting position 

at the end of the loop if we reach the end 0 then we return the true and false otherwise
'''
def canJump(nums: List[int]) -> bool:
    goal = len(nums) -1

    for i in range(len(nums) -1,-1,-1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False
print(canJump([3,2,1,1,4]))
print(canJump([3,2,1,0,4]))