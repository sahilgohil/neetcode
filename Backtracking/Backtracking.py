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
# print(subsets([1,2,3]))


'''

Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    # will make a decision tree for the current element to go in the sum or not go 
    # base case, if the sum is the target then add the subset in the result
    # if the length of the current index is at the end then return
    def backtrack(i,com,currSum):
        if currSum == target:
            res.append(com.copy())
            return
        if i == len(candidates) or currSum > target:
            return
        
        # curr come in the sum
        com.append(candidates[i])
        backtrack(i,com,currSum+candidates[i])
        com.pop()
        backtrack(i+1,com,currSum)

    backtrack(0,[],0)
    return res
# print(combinationSum([2,3,6,7],7))

'''
Permutation

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

'''

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    # take the current and permute the rest
    # take the middle and permute the first and last
    # take the last and permute the first and second
    # base case if the length is one return the list of list
    if len(nums) == 1:
        return [nums.copy()]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
 
    return res
print(permute([1,2,3]))