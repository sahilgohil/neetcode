
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

"""
maintain a cache
get the total length of the costs
    create a new function recursion that takes the index i
        if i is in the cache return the cache value
        if i is less than 0 then return 0

        calculate the cost for current step with cost for current step plus cost of previous step
        calculate the cost for current step with cost for current step plus cost of previous two step
        take the minimum for the above two
        store it in the cache
        return the cache value
    call the recursion function for one step and two step and return the minimum of the two
"""
def min_cost_climbing_stairs_top_down(costs):
    cache = {}
    def recursion(idx):
        if idx in cache:
            return cache[idx]
        if idx < 0:
            return 0
        cost_one_step = costs[idx] + recursion(idx -1)
        cost_two_step = costs[idx] + recursion(idx -2)
        cache[idx] = min(cost_one_step, cost_two_step)
        return cache[idx]
    return min(recursion(len(costs)-1), recursion(len(costs)-2))        

"""
Bottom-Up Approach
create an array of size len(costs)
put the base cases in the array as
    cost to reach step 0 is the same and
    cost to reach step 1 is the same
loop for the rest of the steps
    for each step the cost will be the minimum cost of previous one and two steps in addition to the current step cost
    return the minimum of the last two steps
"""

def min_cost_climbing_stairs_bottom_up(costs):
    dp = [0] * len(costs)
    n = len(costs)
    dp[0] = costs[0]
    dp[1] = costs[1]
    for i in range(2, len(costs)):
        dp[i] = costs[i] + min(dp[i-1],dp[i-2])
    return min(dp[n-1],dp[n-2])

'''
House robbing problem
Constraint is : can not rob two houses in a row
'''

"""
Bottom-Up Approach
nums is given which is the maximum money that each house has
create an array of size len(nums)
put the base cases in the array as
profitloot from house 0 is same
profitloot from house 1 is profit from one house before plus current and previous's max
return the max will be the last index's value
"""

def house_robing_bottom_up(houses):
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0],houses[1])
    for i in range(2,len(houses)):
        dp[i] = max(dp[i-1], houses[i] + dp[i-2])
    return dp[len(houses)-1]

"""
Top-Down approach
keep a cache
run the recursive funtion that takes index as an argument
    if the i is less than 0 return 0
    if i is in the cache then return the cache value
    the value we calculate at i is max of (current house money + last to last house money, last house money)
    store it in the cache at i
    return the value in cache at i
run the recursive function and return the value at the last index in cache
"""

def house_robing_top_down(houses):
    cache = {}
    def recursion()

# print(min_cost_climbing_stairs_bottom_up([10,15,20]))
# print(min_cost_climbing_stairs_top_down([10,15,20]))
print(house_robing_bottom_up([2,7,9,3,1]))

        


    

    

