# climbing stairs
from typing import List


def cs(n:int) -> int:
    cache = {}
    def recursion(idx) -> int:
        if idx == 0 or idx == 1:
            return 1
        if idx in cache:
            return cache[idx]
        cache[idx] = recursion(idx - 1) + recursion (idx - 2)
        return cache[idx]
    return recursion(n)
    
# min cost climbing stairs
'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
def minCostClimbingStairs( cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * n
    # base case
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1],dp[-2])
# print(minCostClimbingStairs([10,15,20]))
# house robber
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
def houseRobber(money:List[int])->int:
    n = len(money)
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0],money[1])

    for i in range(2, n):
        dp[i] = max(money[i] + dp[i-2], dp[i-1])
    return dp[-1]
# print(houseRobber([1,2,3,1]))

# house robber 2
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

here we have to find the maximum money twice,
 first without house 1
 second without house last
 this way we will save from looting house 1 and last at the same time
 and then the answer will the max of both the results

'''
def houseRobber2(money:List[int])->int:
    n = len(money)
    def helper(start, end):
        dp = [0] * n
        dp[start] = money[start]
        dp[start + 1] = max(money[start], money[start + 1])
        for i in range(start + 2, n ):
            dp[i] = max(dp[i-2] + money[i], dp[i-1])
        return dp
    money_without_first = helper(1,n-1)
    money_without_last = helper(0,n-2)
    return max(money_without_first[n-1], money_without_last[n-2])
# print(houseRobber2([2,3,2]))

# longest palindromic substring
'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 classic dp problem,
 all single will be palindrome
 all 2 char is palindrome if both char are same
 threee or more are palindrome if char at both ends are same and the substring is palindrome
 that is it
 keep track of the longest string's starting and ending index
 that is the result
'''
def longestPalindrome(s:str)->str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    start, end = 0,0
    for l in range(2, n+1):
        for i in range(n-l +1):
            j = i+l-1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j]= True
                    if j-i > end - start:
                        start, end = i, j

    return s[start:end+1]
# print(longestPalindrome("babad"))

# count the palindromic substrings
'''
this question is the same as the previous one we only need to count it and return the value

'''
def palindromeCount(s:str)->int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    count = n
    for l in range(2, n+1):
        for i in range(n-l +1):
            j = i+l-1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j]= True
                    count = count +1

    return count
# print(palindromeCount("abc"))

# decode ways
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

to solve this problem we will use the dp bottom up approach
we will have two base cases,
1 - if the string is empty then there is only one way to decode it
2 - if the string's first char is not 0 then one way else 0 ways
then for each char we have to find out if the char is non zero and the two digit forms a valid number and add both together
'''

def decodeWays(s:str)->int:
    n = len(s)
    dp = [0] * (n+1) # as we have additional case for string beign empty
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, len(dp)):
        singleDigit = int(s[i-1:i])
        doubleDigit = int(s[i-2:i])

        if 0< singleDigit <=9:
            dp[i] += dp[i-1] # the ways to decode are same as previous
        if 10 <= doubleDigit <= 26:
            dp[i] += dp[i-2] # the ways to decode are same as one before previous

    return dp[-1]
# print(decodeWays("223"))

# coin change
'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

def coinChange(coins:List[int], amount:int)->int:
    need = [amount + 1] * (amount + 1)
    need[0] = 0 # 0 coins are required for 0 amount
    for a in range(1, len(need)):
        for c in coins:
            if c<= a:
                need[a] = min(need[a], need[a-c] + 1)
    
    return need[amount] if need[amount] != amount +1 else -1
# print(coinChange([1,2,5], 11))


# maxproduct
'''
first keep the var maxProductSofar
then currentMax at the index
then currentMin at the index
initialize all the above three with value of the first element
loop from i to end
'''
def maxProduct(nums:List[int])->int:
    max_product_so_far = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    for i in range(1, len(nums)):
        tempMax = max(nums[i], current_max * nums[i], current_min * nums[i])
        current_min = min(nums[i], current_max * nums[i], current_min * nums[i])
        current_max = tempMax

        max_product_so_far = max(max_product_so_far, current_max)
    return max_product_so_far
print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

# wordbreak
# longest increasing subsequence
# partition

