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