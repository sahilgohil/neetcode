# Unique Paths
'''
given m x n matrix find the number of unique paths to reach the destination end
SUDO Code

crearte dp with m x n and assign default value of 1 as there is always one way to reach that cell either from above or from the left
loop through each cell (start from 1 row and 1 column as the base cases are satisfied)
the unique ways at each cell are the ways from the above row and left column's sum
return the last cell

'''

from typing import List


def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)] # initialise with 1 for the base cases

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[-1][-1]
'''
given two strings find the length of the longest common subsequence
we create dp in a way that dp[i][j] will be text1[:i] and text2[:j]
their default value will be 0
we start looping from 1 row 1 column as rows and columns before are for empty string base cases
for each cell we have two choices
    1 if the characters at i and j matched
        then we take the previous length's value and add 1 to it
    2 else 
        we get the maximum value from both the previous length of text1 and text2
'''
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1) + 1 # include base case for empty string
    n = len(text2) + 1 # include base case for empty string
    dp = [[0] * n for _ in range(m)]

    for i in range(1,m):
        for j in range(1, n):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


'''
Best Time to Buy and Sell Stock with Cooldown

there are three states that we need to keep track of
1 dpbuy = have the max profit at ith day if we by the stock
2 dpsell = have the max profit at the ith day if we sell the stock
3 dpcooldown = have the max profit at the ith day if we cooldown

return the max of sell, cooldown

SUDO Code 
n is the length of the prices
dp_buy = 

'''

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dpBuy = [0] * n
    dpSell = [0] * n
    dpCooldown = [0] * n
    dpBuy[0] = -prices[0] # profit at the day 0 will be negative as we just bought the stock
    for i in range(1, n):
        dpBuy[i] = max(dpBuy[i-1], dpCooldown[i-1] - prices[i]) # either previous buy or buy from cooldown
        dpSell[i] = dpBuy[i-1] + prices[i] # sell the stock using the previous buy price (note buy price is already negative)
        dpCooldown[i] = max(dpCooldown[i-1], dpSell[i-1]) # cooldown will have max profit after selling or previous cooldown

    return max(dpSell[-1],dpCooldown[-1])
# print(maxProfit([1,2,3,0,2]))

'''
Problem - Coin Change II
given the amount and unlimited set of coins, return the possible combinations available that make up to that amount

here we make dp of length amount + 1 with default value of 0, we increase the size of dp because, we need to accomodate the amount 0
base case, amount 0 will require only 1 combinations that by putting no coins in the combinations

SUDO Code
n is (amount + 1)
dp is [0] * n
base case dp[0] is 1

loop for each coin
    for amountA from coin to the targetAmount
        increment the previous possible combinations available for the amount using the coin
return the dp[amount]
'''

def change(amount: int, coins: List[int]) -> int:
    cache = {} # (index, total) -> number of combination of the amount
    def dfs(idx, total):
        if total > amount:
            return 0
        if idx == len(coins):
            return 1 if total == amount else 0
        if (idx, total) in cache:
            return cache[(idx,total)]
        # either the current coin comes in the combination or it doesnt
        cache[(idx,total)] = dfs(idx+1,total+coins[idx]) + dfs(idx,total+coins[idx]) + dfs(idx+1, total)
        return cache[(idx,total)]
    return dfs(0,0)
    # n = amount + 1
    # dp = [0] * n # dp is the number of combination for the amount
    # dp[0] = 1 

    # # to find all the combination for the amount we have to loop through each coin
    # for coin in coins:
    #     # then we have to check each amount from that coin to our target amount
    #     for a in range(coin, n):
    #         # add the values of the previous combinations for the coin of this amount
    #         dp[a] += dp[a - coin]
    # return dp[amount]

print(change(5, [1,2,5]))

'''
Target sum with combinations 
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
'''
def findTargetSumWays(nums: List[int], target: int) -> int:
    cache = {} #(index,total) -> number of ways
    def backtrack(i,total):
        # basecase if we reach at the last index
        if(i == len(nums)):
            return 1 if total == target else 0
        if (i,total) in cache:
            return cache[(i, total)]
        cache[(i,total)] = (backtrack(i+1,total+nums[i]) + backtrack(i+1,total-nums[i]))
        return cache[(i,total)]
    return backtrack(0,0)

'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
'''
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    cache = {} # (idx1,idx2)
    def backtracking(idx1,idx2):
        # if we reach the end of both the strings then we have the solution
        if idx1 == len(s1) and idx2 == len(s2):
            return True
        if (idx1,idx2) in cache:
            return cache[idx1,idx2]
        if idx1 < len(s1) and s1[idx1] == s3[idx1 + idx2] and backtracking(idx1+1,idx2):
            return True
        if idx2 < len(s2) and s2[idx2] == s3[idx1 + idx2] and backtracking(idx1,idx2+1):
            return True
        cache[(idx1,idx2)] = False
        return cache[(idx1,idx2)]
    return backtracking(0,0)
        
'''
Longest increasing path in a matrix
'''
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {} #(r,c) -> LIP
    def dfs(r,c,prevVal):
        if (r<0 or r >= ROWS or c <0 or c >= COLS or matrix[r][c] <= prevVal):
            return 0
        if (r,c) in dp:
            return dp[(r,c)]
        res = 1
        res = max(res, dfs(r+1,c,matrix[r][c])+1)
        res = max(res, dfs(r-1,c,matrix[r][c])+1)
        res = max(res, dfs(r,c+1,matrix[r][c])+1)
        res = max(res, dfs(r,c-1,matrix[r][c])+1)
        dp[(r,c)] = res
        return dp[(r,c)]
    for i in range(ROWS):
        for j in range(COLS):
            dfs(i,j,-1)
    return max(dp.values())

'''
Distinct subsequences
'''
def numDistinct(s: str, t: str) -> int:
    cache = {} # (i, j) -> numOfDistinctsubsequences
    def dfs(i,j): # i is the idx of s and j is the idx of t
        if j == len(t): # if we have empty string t then there is only one subsequence from s which is empty string
            return 1
        if i == len(s): # if we have empty input we cant make any sub sequence
            return 0
        if (i,j) in cache:
            return cache[(i,j)]
        
        if s[i] == t[j]:
            cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
        else:
            cache[(i,j)] = dfs(i+1,j)
        return cache[(i,j)]
    return dfs(0,0)

'''
Edit Distance
'''
def minDistance(word1: str, word2: str) -> int:
    cache = {} # (i,j) -> minOperations
    def dfs(i,j):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2)- j # when the i reaches the end returnt the remaining entry for the word 2
        if j == len(word2):
            return len(word1)- i # when the j reaches the end return the remaining entry for the word 1
        if (i,j) in cache:
            return cache[(i,j)]
        if word1[i] == word2[j]:
            cache[(i,j)] = dfs(i+1,j+1)
        else:
            cache[(i,j)] = 1 + min(dfs(i,j+1), dfs(i+1,j), dfs(i+1,j+1))# insert a char, remove a char, replace a char
        return cache[(i,j)]
    return dfs(0,0)



'''
Burst Balloons
'''
def maxCoins(nums: List[int]) -> int:
    cache = {} #(l,r) -> total where l is the left after added 1 and r is the last before added 1
    nums = [1] + nums + [1]
    def dfs(l,r):
        if l>r:
            return 0
        if (l,r) in cache:
            return cache[(l,r)]
        cache[(l,r)] = 0
        for i in range(l,r+1):
            coins = nums[l-1] * nums[i] * nums[r+1]
            coins += dfs(l,i-1) + dfs(i+1,r)
            cache[(l,r)] = max(cache[(l,r)], coins)
        return cache[(l,r)]
    return dfs(1,len(nums)-2)


'''
Pattern matching expression
'''
def isMatch(s: str, p: str) -> bool:
        cache = {} # (i,j) -> bool
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
        
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # if the next char is *
            if (j+1) < len(p) and p[j+1] == "*":
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i + 1, j))   # use *
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return cache[(i,j)]
        return dfs(0,0)
