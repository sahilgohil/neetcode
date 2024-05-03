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
print(minCostClimbingStairs([10,15,20]))
# house robber
# house robber 2
# longest palindromic substring
# count the palindromic substrings
# decode ways
# coin change
