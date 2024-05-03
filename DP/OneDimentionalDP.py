
from typing import List


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

'''
this is the problem where we find the solution of the smaller problem and then make our way upwards to the bigger problem,

there are four things to keep in mind when approaching this problem

1 - all the single characters are palindrome
2 - looping will happen diagonally, hence the most outer loop will run from 2 to length of the string, it determines the size of the substring being evaluated
3 - internal looping for i and is dynamic , it will loop from 0 to end index of string but the calculation will be n(total lenght of the string) - l (lenght of the substring) 
4 - j is the last index of the substring, which is a dynamic value , easy to calculate, = i (1st index of the substring) + l (length of the substring) - 1 [we decrease one as j is an index]

SUDO Code
- n is the length of the string
- dp is boolean matrix of n x n with false values as start with
- start, end are the indexes of the longest palindromic substrings
- loop for substring starting from 2 all the way to the length of the string + 1 as we want to include all possible lengths the substrings
    - loop for strating index i from 0 to n-l+1 so that it includes all the indexes
        - j will be the last index of the current substring i + l - 1
        - if the value of substring at i and j are same and its either length 2, or its innner string is a palindrome then put the value at i, j as True
'''
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

'''
count the number of palindromic substrings
we use the same method as above and keep the counter variable
let's see if we can solve this problem
'''

def count_palindromic_substrings(s:str)->int:
    n = len(s)
    count = n

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s [j]:
                if l == 2 or dp[i+1][j-1]:
                    count = count +1
                    dp[i][j] = True

    return count

'''
decoding a string into number of ways
using the bottom up approach to the problem solving
if the string is empty then there is only one way to decode it
if the string's first character is 0 then there is no way else there is only one way to decode it

then we have two possibilities for the rest of the characters
if the previous character and current character makes an int 0 < int < then there can only be same ways as the previous place
if the previous character and current character makes an int 10< int < 26 then the string is double digit and the ways to decode is two char before

at the end last value will be the answer

SUDO Code
n is the length of the string
dp will have the lenght of the string plus 1 to accomodate for the empty string
- base case each i represents the number of ways to decode the string of length i
- i = 0 have only one way to decode it
- i = 1 length of 1 string will have one way only if the char is not 0 else it has 0 ways
- loop for the range of dp's lenght
    - get the single digit of the string = s[i-1:i] we are deducting one more as the string is one index behind the dp
    - get the double digit of the string = s[i-2:i] 
    - check if the single digit is valid
        - yes then add the value of dp[i-1]
    - check is the double digit is valid
        - yes then add the value of dp[i-2]
return the last value of dp
'''

def decode_string_count(s:str)->int:
    n = len(s)
    dp = [0] * (n+1) # as we need to keep track of the empty string
    dp[0] = 1 # only one way to decode empty string
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, len(dp)):
        singleDigit = int(s[i-1:i])
        twoDigits = int(s[i-2:i]) # we decrease 2 as i is running one step ahead of the string

        # checkign for single digit
        if 0 <singleDigit<=9:
            dp[i] += dp[i-1]

        # checking for double digit
        if 10<= twoDigits<=26:
            dp[i] += dp[i-2]
    return dp[-1]


# def move_diagonally(n):
#     # n = 5
#     for l in range(2, n + 1):
#         for i in range(n-l+1):
#             j = i + l - 1
#             print(f"l: {l} i:{i} j:{j}")
'''
This problem requires
- creating array of length amount + 1 to accomodate for amount 0
- at every step of the array we are filling the default value of amount + 1
- at every iteration of the array we loop through the coins and check if the coin is less than or equal to the current amount, if yes then we put min of the value at that place or [amount - coin] +1

SUDO Code
- make the array of lenght amount + 1 with default value as amount + 1
- base case array[0] will be 0 no coins required for 0
- for i from 1 to end
    - iterate though each coin
        - if the coin is less than or equal to the value of amount
            - put the min value of (value at that index, value at index - coin + 1 as we want to add one more coin)
return the array[amount] if array[amount] != amount + 1 else return not possible solution
'''
def coin_change(coins:List[int],amount:int)->int:

    need = [amount + 1] * (amount + 1)
    
    # base case 0 no coins needed for amount 0
    need[0] = 0
    for i in range(1,len(need)):
        for c in coins:
            if c <= i:
                need[i] = min(need[i],need[i - c] +1)
    return need[amount] if need[amount] != amount+1 else -1


'''
MAX product of the subarray 

this problem can be solved using the dynamic programming bottom up approach
we maintain three things,
1 - maximum product so far
2 - current max product
3 - current min product
at each iteration we will find the maximum product by multiplying the current value with the current max and current min this will accomodate for any negative values
at the end we will update the maximum and minimum products 
return the result using the maximum product so far.

SUDO Code
maxsofar, currentmax,currentmin initialize with first element

loop from first element to the end of the array
    get the current array element
    keep temporary max of current eleemnt, currentmax * currentelement, currentmin * currentelement
    change the currentmin using the min function for above three values
    change the currentmax to temp max
    update the maxsofar using the current max
return the max sofar

'''

def maxProduct(nums:List[int])->int:
    n = len(nums)
    if n == 1:
        return nums[0]
    maxSoFar = nums[0]
    currentMax = nums[0]
    currentMin = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        tempMax = max(num, currentMax * num, currentMin * num)
        currentMin = min(num, currentMax * num, currentMin * num)
        currentMax = tempMax

        maxSoFar = max(maxSoFar, currentMax)
    return maxSoFar
print(maxProduct([2,3,-2,4]))

'''
Problem - Word Break
to solve this problem we will maintain a dp of lenght one greater than the lenght of the string to accomodate for the empty string

for each length of the substring we will check two things,
 1 - if the subtring's part from 0 to j is can be segmentable 
 2 - if the substring's part from j to i is in the word dictionary

 if both the conditions are met then we will consider that the substring can be segmented and put true to the dp array
 and we will return the last values as our answer

 SUDO Code
 convert the word dictionary into wordset for faster lookup
 create a dp with length of s plus 1 to accomodate for the empty string
 apply base case for string 0 to true
 loop as i from 1 to dp's length
    loop from 0 to i
        if the dp[j] is true and substring from j to i is in the word set then 
            make the current value true in dp
return the last value of dp as answer

'''

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    wordSet = set(wordDict)
    dp = [False] * (n+1) # to accomodate for the empty string
    dp[0] = True # as empty string can always be segmented to anything

    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True


    return dp[-1]
# print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

# move_diagonally(5)
# print(longest_palindrome("baa"))
# print(count_palindromic_substrings("abc"))
# print(decode_string_count("226"))
# print(coin_change([1,2,5],11))



            

        
        



# print(house_robing_top_down([2,7,9,3,1]))
# print(min_cost_climbing_stairs_bottom_up([10,15,20]))
# print(min_cost_climbing_stairs_top_down([10,15,20]))
# print(house_robing_bottom_up([2,7,9,3,1]))

# print(house_robber2_bottom_up([2,3,2]))


        


    

    

