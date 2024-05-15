from typing import List
'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
'''
def uniquePaths(m: int, n: int) -> int:
    dp = [[1]*n for _ in range(m)]
    # for base cases first row and first column have only one way to reach the end on both sides
    # we will start with 1 row 1 column
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[-1][-1]

'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # increased the length to accomodate for the base case of empty strings
    m = len(text1) + 1
    n = len(text2) + 1

    dp = [[0]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1, n):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dpBuy = [0] * n
    dpSell = [0] * n
    dpCooldown = [0] * n
    # all the above three represents the max rpofit at the ith index
    # basecase 
    dpBuy[0] = -prices[0]
    for i in range(1,n):
        dpBuy[i] = max(dpBuy[i-1], dpCooldown[i-1] - prices[i])
        dpSell[i] = dpBuy[i-1] + prices[i]
        dpCooldown[i] = max(dpCooldown[i-1], dpSell[i-1])
    return max(dpSell[-1], dpCooldown[-1])


'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''

def change(amount: int, coins: List[int]) -> int:
    n = (amount+1)
    dp = [0] * n
    dp[0] = 1 # for amount 0 there are 1 combination by using no coins at all

    for c in coins:
        for a in range(c,n):
            dp[a] +=dp[a - c]
    return dp[amount]

'''
Find target sum to make up the target
'''
def findTargetSumWaysPractice(nums: List[int], target: int) -> int:
    cache = {} #(index, totalSoFar) -> number of ways

    def dfs(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i,total) in cache:
            return cache[(i,total)]
        cache[(i,total)] = (dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i]))
        return cache[(i,total)]
    return dfs(0,0)
'''
Edit distance
'''
def minDistance(word1: str, word2: str) -> int:
    cache = {} # i,j -> min operations
    def dfs(i,j):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if (i,j) in cache:
            return cache[(i,j)]
        if word1[i] == word2[j]:
            cache[(i,j)] = dfs(i+1,j+1)
        else:
            cache[(i,j)] = 1 + min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
        return cache[(i,j)]
    return dfs(0,0)


'''
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
'''

def numDistinctPractice(s: str, t: str) -> int:
    cache = {} #(i,j) -> numOfDistinct
    def dfs(i,j):

        # if the t is empty then there is only one way to make the empty subsequence by not putting any one on the characters
        if j == len(t):
            return 1

        # if the s is empty there are no way to make a sub sequence
        if i == len(s):
            return 0

        if (i,j) in cache:
            return cache[(i,j)]
        if s[i] == t[j]:
            cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
        else:
            cache[(i,j)] = dfs(i+1,j)
        return cache[(i,j)]
    return dfs(0,0)
    