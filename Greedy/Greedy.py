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
# print(canJump([3,2,1,1,4]))
# print(canJump([3,2,1,0,4]))

'''
Jump Game 2

find the min jumps to reach the last index

'''

def jump(nums: List[int]) -> int:
    res = 0

    l = r = 0
    while r < len(nums) -1:
        farthest = 0
        for i in range(l ,r+1):
            farthest = max(farthest, i+nums[i])
        l = r+1
        r = farthest
        res += 1
    return res

# print(jump([2,3,1,1,4]))

'''

Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

'''

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost): # if i dont have enough gas then return 0
        return -1
    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total <0:
            total = 0
            start = i+1

    return start
print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))