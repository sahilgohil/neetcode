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
    n = amount + 1
    dp = [0] * n # dp is the number of combination for the amount
    dp[0] = 1 

    # to find all the combination for the amount we have to loop through each coin
    for coin in coins:
        # then we have to check each amount from that coin to our target amount
        for a in range(coin, n):
            # add the values of the previous combinations for the coin of this amount
            dp[a] += dp[a - coin]
    return dp[amount]

print(change(5, [1,2,5]))