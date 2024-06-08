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

'''
Koko eating bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
def minEatingSpeed(piles: List[int], h: int) -> int:
    def canEat(k):
        totalHours = 0
        for pile in piles:
            totalHours += (pile + k - 1)//k
        return totalHours <= h
    left,right = 1, max(piles)
    while left < right:
        mid = (left+right)//2
        if canEat(mid):
            right = mid
        else:
            left = mid + 1

    return left

'''
Find minimum in rotated sorted array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

def findMin(nums: List[int]) -> int:
    l,r= 0,len(nums)-1
    while l<=r:
        mid= (l+r)//2
        if nums[mid] > nums[r]:
            l = mid+1
        else:
            r = mid-1
    return nums[l]

'''
Search in roteted sorted array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''
def search(nums: List[int], target: int) -> int:
   l, r = 0, len(nums)-1

   while l<=r:
       mid = (l+r)//2
       if nums[mid] == target:
           return mid
       # left is sorted
       if nums[mid] >= nums[l]:
           if target < nums[mid] and target >= nums[l]:
               r = mid-1
           else:
               l = mid+1
       else:
           if target <= nums[r] and target > nums[mid]:
               l = mid + 1
           else:
               r = mid - 1

   return -1
           
'''

'''
class TimeMap:

    def __init__(self):
        self.store = {} #[value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
     
            
    def get(self, key: str, timestamp: int) -> str:
       res = ""
       values = self.store.get(key,[])
       l, r = 0, len(values)-1

       while l<=r:
           mid = (l+r)//2
           if values[mid][1] <= timestamp:
               res = values[mid][0]
               l = mid + 1
           else:
               r = mid-1
       return res
    
'''
Median of two sorted array

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A,B = nums1, nums2
    if len(B) < len(A):
        A,B = B,A
    total = (len(A) + len(B))
    half = total//2

    l, r = 0, len(A) - 1
    while True:
        i = (l+r)//2 # A pointer
        j = (half-i-2) # B pointer

        Aleft = A[i] if i >=0 else float('-infinity')
        Aright = A[i+1] if (i + 1) < len(A) else float('infinity')
        Bleft = B[j] if j >=0 else float('-infinity')
        Bright = B[j+1] if (j + 1) < len(B) else float('infinity')

        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright,Bright)
            else:
                return (max(Aleft,Bleft) + min(Aright,Bright))//2
        elif Aleft > Bright:
            r = i -1
        else:
            l = i+1