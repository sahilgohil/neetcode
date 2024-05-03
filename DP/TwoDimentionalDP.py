# Unique Paths
'''
given m x n matrix find the number of unique paths to reach the destination end
SUDO Code

crearte dp with m x n and assign default value of 1 as there is always one way to reach that cell either from above or from the left
loop through each cell (start from 1 row and 1 column as the base cases are satisfied)
the unique ways at each cell are the ways from the above row and left column's sum
return the last cell

'''

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