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

    dp[0] = cost[0]
    dp[1] = cost[1]


    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    
    return min(dp[-1], dp[-2])


# house robber
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
def houseRobber(money:List[int])->int:
    n =  len(money)
    dp = [0] * n
    # base cases
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

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
        dp[start+1] = max(money[start], money[start+1])

        for i in range(start+2, end+1):
            dp[i] = max(money[i]+dp[i-2], dp[i-1])
        return dp
    dp_without1 = helper(1,n-1)
    dp_withoutlast = helper(0,n-2)
    return max(dp_without1[n-1], dp_withoutlast[n-2])

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
    # requires matrix dp
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    start,end = 0,0
    for l in range(2, n+1): # for substring of length starting from 2 to n
        for i in range(n-l+1): # starting index of the substring 0 to n-1
            j = l+i-1 # index of the last char in the substring
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i>end-start:
                        start,end = i,j
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
    n = len(s)+1
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n):
        single = int(s[i-1:i])
        double = int(s[i-2:i])

        if 0<single<=9:
            dp[i] += dp[i-1]
        if 10<=double<=26:
            dp[i] += dp[i-2]
    return dp[-1]


# print(decodeWays("223"))

# coin change
'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

def coinChange(coins:List[int], amount:int)->int:
    dp = [amount+1] * (amount+1)
    # base case
    dp[0] = 0
    for i in range (1, len(dp)):
        for c in coins:
            if c<= i:
                dp[i] = min(dp[i], dp[i-c] + 1) # here i need to find the min cost either current or the cost of previously made amount + using this coin
    return dp[amount] if dp[amount] != (amount+1) else -1

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
    max_so_far = nums[0]
    c_max = nums[0]
    c_min = nums[0]

    for i in range(1, len(nums)):
        temp_max = max(nums[i], nums[i] * c_max, nums[i]*c_min)
        c_min = min(nums[i], nums[i] * c_max, nums[i]*c_min)
        c_max = temp_max

        max_so_far = max(c_max,max_so_far)
    return max_so_far


# print(maxProduct([2,3,-2,4]))
# print(maxProduct([-2,0,-1]))

'''
this problem requires a wordset
create a dp of length of the string plus 1 with default value to be boolean
base case empty string will always be in word break = True
loop from 1 to end of dp
    then loop every substring till i
     check if the substring is already true and from j to i is in the word break then we put true
return the last value
'''
# wordbreak
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s) + 1
    dp = [False] * n
    dp[0] = True
    wordSet = set(wordDict)
    for i in range(1, n):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
    return dp[-1]   
 
# print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# print(wordBreak("leetcode", ["leet","code"]))

'''
we check if the current num is less than the 
'''
# longest increasing subsequence
def lengthOfLIS( nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]

# print(lengthOfLIS([10,9,2,5,3,7,101,18]))

# partition
def partition(nums:List[int])->bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target_sum = total//2
    n = len(nums) + 1
    dp = [[False] * (target_sum+1) for i in range(n)]
    for i in range(n):
        dp[i][0] = True # for sum 0 we can always partition
    
    for idx in range(1, n):
        for sm in range(1, target_sum+1):
            if nums[idx-1] <= sm:
                # two options either include the sum or not include the sum
                option1 = dp[idx-1][sm-nums[idx-1]] # include the current element to makeup for the sum
                option2 = dp[idx-1][sm] # do not inlcude the current element to makeup for the sum
                dp[idx][sm] = option1 or option2
            else:
                dp[idx][sm] = dp[idx-1][sm] # we just carry forward the previous answer

    return dp[-1][-1]


