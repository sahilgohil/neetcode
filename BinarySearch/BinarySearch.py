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

'''
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    r,c = 0,len(matrix[0])-1 # first row last colmns
    while r<len(matrix) and c>=0:
        currElement = matrix[r][c]
        if currElement == target:
            return True
        if currElement > target:
            c -= 1
        else:
            r += 1
    return False
