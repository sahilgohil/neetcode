import heapq
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


'''
Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
'''

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    #if the hand length is not divisible by groupsize then we cant have
    if len(hand) % groupSize != 0:
        return False
    
    table = {} # each number -> count
    for n in hand:
        table[n] = 1 + table.get(n,0)
    # we need to heapify to get the min 
    minHeap = list(table.keys()) # will give the distinct set of numbers 
    heapq.heapify(minHeap)

    while minHeap:
        start = minHeap[0] # will give the minimum value
        for i in range(start, start + groupSize):
            if i not in table:
                return False
            table[i] -= 1

            if table[i] == 0:
                # if the value poping is the min
                if i != minHeap[0]:
                    return False
                heapq.heappop(minHeap)
    return True

'''
Merge triplet to form target triplet

A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
'''

def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    good = set()
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        for i, v in enumerate(t):
            if v == target[i]:
                good.add(i)
    return len(good) == 3

'''
Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''

def partitionLabels(s: str) -> List[int]:
    lastIndex = {} # c -> last index

    for i,c in enumerate(s):
        lastIndex[c] = i

    res = []
    start, end = 0, 0

    for i, c in enumerate(s):
        start += 1 

        end = max(end, lastIndex[c])

        if i == end:
            res.append(start)
            start = 0
    return res
