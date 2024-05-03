# Unique Paths
'''
given m x n matrix find the number of unique paths to reach the destination end
SUDO Code

crearte dp with m x n and assign default value of 1 as there is always one way to reach that cell either from above or from the left
loop through each cell
the unique ways at each cell are the ways from the above row and left column's sum
return the last cell

'''