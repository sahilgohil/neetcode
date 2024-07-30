# '''
# Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.
 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 
# Input: grid = [
#   ['1','1','1','1','0'],
#   ['1','1','0','1','0'],
#   ['1','1','0','0','0'],
#   ['0','0','0','0','0']
# ]

# Output: 1



# '''

# def findIslands(grid):

#     rows = len(grid)
#     cols = len(grid[0])

#     visit = set()


#     def dfs(r,c, dr, dc):

#         if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visit or grid[r][c] == "0":
#             return
        
#         # visited
#         visit.add((r,c))
#         shape.add((dr,dc))
#         dfs(r+1,c)
#         dfs(r-1,c)
#         dfs(r,c+1)
#         dfs(r,c-1)
    
#     islands = 0

#     '''
#     Input: grid = [
#   ['1','1','1','1','0'],
#   ['1','1','0','1','0'],
#   ['1','1','0','0','0'],
#   ['0','0','0','0','0']
# ]'''
#     res = set()

#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == "1" and (r,c) not in visit:

#                 shape = set()
#                 dfs(r,c, dr, dc)
#                 res.add(frozenset(shape))
    
#     return len(res)

# '''
# nput: grid = [   ['1','1','0','0','0'],   ['1','1','0','0','0'],   ['0','0','1','0','0'],   ['0','0','0','1','1'] ] 
# Output: 3 
 
# Input: grid = [['1','0','1','1','0','1','1']] 
# Output: 3 
 
# Input: grid = [['1'],['0'],['1'],['0'],['1'],['1']] Output: 3
# '''

# print(findIslands([
#   ['1','1','1','1','0'],
#   ['1','1','0','1','0'],
#   ['1','1','0','0','0'],
#   ['0','0','0','0','0']
# ]))

# print(findIslands([   ['1','1','0','0','0'],   ['1','1','0','0','0'],   ['0','0','1','0','0'],   ['0','0','0','1','1'] ]))

# print(findIslands([['1','0','1','1','0','1','1']]))

# print(findIslands([['1'],['0'],['1'],['0'],['1'],['1']]))



