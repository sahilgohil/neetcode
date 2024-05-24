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
# print(permute([1,2,3]))

'''
Subset 2

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def backtrack(i,sub):
        if i == len(nums):
            res.append(sub.copy())
            return
        # all subset with current value
        sub.append(nums[i])
        backtrack(i+1,sub)
        sub.pop()
        # all subset without current value
        while i+1<len(nums) and nums[i] == nums[i+1]:
            i+=1
        backtrack(i+1,sub)
    backtrack(0,[])
    return res

# print(subsetsWithDup([1,2,2]))

'''
Combination Sum 2

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res =[]
    candidates.sort()
    def backtrack(i,currSum,com):
        if currSum == target:
            res.append(com.copy())
            return
        if currSum > target or i == len(candidates):
            return
        # add the current element in the combination 
        com.append(candidates[i])
        backtrack(i+1,currSum+candidates[i],com)
        com.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        # not include the current element in the combination
        backtrack(i+1,currSum,com)
    backtrack(0,0,[])
    return res

# print(combinationSum2([10,1,2,7,6,1,5],8))

'''
Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

def exist(board: List[List[str]], word: str) -> bool:
    rows,cols = len(board), len(board[0])
    visit = set()
    def backtrack(r,c,i):
        if i == len(word):
            return True
        if r not in range(rows) or c not in range(cols) or board[r][c] != word[i] or (r,c) in visit:
            return False

        visit.add((r,c))
        res = (backtrack(r+1,c,i+1) or
               backtrack(r-1,c,i+1) or
               backtrack(r,c+1,i+1) or 
               backtrack(r,c-1,i+1))
        visit.remove((r,c))
        return res
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                if backtrack(i,j,0):
                    return True
    return False

# print(exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))
'''
Palindrome partition

Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.
'''
def partition( s: str) -> List[List[str]]:
    res = []
    part = []

    def backtrack(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i,len(s)):
            if isPalindrome(s,i,j):
                part.append(s[i:j+1])
                backtrack(j+1)
                part.pop()
    backtrack(0)
    return res
def isPalindrome(s,l,r):
    while(l<r):
        if s[l] != s[r]:
            return False
        l,r = l+1,r-1
    return True
print(partition("aab"))