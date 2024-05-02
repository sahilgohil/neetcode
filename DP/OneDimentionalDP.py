
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
    def recursion(idx):
        if idx<0:
            return 0
        if idx == 1:
            return houses[1]
        if idx in cache:
            return cache[idx]
        cache[idx] = max(houses[idx] + recursion(idx-2), recursion(idx-1) )

        return cache[idx]
    recursion(len(houses)-1)
    return cache[len(houses)-1]

"""
Read the above problem and imagine that the houses are located in the circular pattern
hence, you cant rob the first and last house at the same time
make 2 dp one with first house removed 
another with last house removed.
take the max of both that will be the answer
"""
"""
Bottom-Up Approach
nums is given which is the maximum money that each house has
make a var n has value of the length of houses
create a helper function that takes the starting and ending index and returns the dp array
    make dp with values to 0
    make dp of start to houses to start
    make dp of start+1 to houses to start, start+1 max
    loop thoush start+2 to end +1
    use the same logic as the previous question
    return the dp
use the helper function to get the dp without the first house
use the helper functuon to get the dp without the last house
return the maximum of the two dp

Top-Down approach is not possible for this problem (more complex than the bottom up (tabulation))
"""

def house_robber2_bottom_up(nums):
    '''
        this problem requires the bottom-up or tabulaation approach to dp

        need a helper function (n is the number of houses)
        first leave the first house and fill the dp from 1 to n-1 
        then leave the last house and fill the dp from 0 to n-2
        after getting both tables we will get the maximum of the both the tables last values n-1 and n-2
        that will be our answer
    '''
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    def helper(start, end):
            dp = [0] * n
            dp[start]  = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])

            for i in range(start +2, end+1):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp
    dp_first_leave = helper(1,n-1)
    dp_leave_last = helper(0,n-2)
    return max(dp_first_leave[n-1], dp_leave_last[n-2])


def longest_palindrome(s:str)-> str:
    n = len(s) # length of the string
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True # all single characters are the palindrome
    start, end = 0,0
    for l in range(2, n+1): # lenght of substring 2,3,4 ...
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i > end - start:
                        start, end = i ,j
                    
    return s[start:end+1]


def move_diagonally(n):
    # n = 5
    for l in range(2, n + 1):
        for i in range(n-l+1):
            j = i + l - 1
            print(f"l: {l} i:{i} j:{j}")

# move_diagonally(5)
print(longest_palindrome("baa"))



            

        
        



# print(house_robing_top_down([2,7,9,3,1]))
# print(min_cost_climbing_stairs_bottom_up([10,15,20]))
# print(min_cost_climbing_stairs_top_down([10,15,20]))
# print(house_robing_bottom_up([2,7,9,3,1]))

# print(house_robber2_bottom_up([2,3,2]))


        


    

    

