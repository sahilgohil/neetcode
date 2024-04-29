def climbing_stairs(N):
    cache = {}
    def recursion(n):
        if n == 0 or n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = recursion(n-1)+ recursion(n-2)
        return cache[n]
    return recursion(N)

# print(climbing_stairs(4))

def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * n
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return min(cost[0], cost[1])
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[n-1], dp[n-2])

    

print(min_cost_climbing_stairs([10, 15, 20]))