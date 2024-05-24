from typing import List
'''
Subset

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsets(nums: List[int]) -> List[List[int]]:
    '''
    SUDO CODE
    here we will be making a decision tree where each char in the number has a choice to come in the subset or not
    every time we reach the end we have to put the made subset in the result
    and while backtracking remove the added character
    '''
    res = []
    def backtrack(i,sub):
        if i == len(nums):
            res.append(list(sub))
            return
        # choice not to come
        backtrack(i+1,sub)
        # choice to come
        sub.append(nums[i])
        backtrack(i+1,sub)
        sub.pop()
    backtrack(0,[])
    return res
print(subsets([1,2,3]))