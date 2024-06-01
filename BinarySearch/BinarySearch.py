from typing import List
import collections

'''
Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''
def search(nums: List[int], target: int) -> int:
    l,r = 0,len(nums)-1
    while l<=r:
        mid = (r+l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return -1