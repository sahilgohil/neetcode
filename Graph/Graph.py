from typing import List
import collections

'''
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = collections.deque()
        queue.append((r,c))
        visited.add((r,c))
        while queue:
            row, col = queue.popleft()
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            for d in dir:
                nextRow = row + d[0]
                nextCol = col + d[1]
                if nextRow in range(rows) and nextCol in range(cols) and grid[nextRow][nextCol] == "1" and (nextRow,nextCol) not in visited:
                    queue.append((nextRow,nextCol))
                    visited.add((nextRow,nextCol))
                # check if the next row is in the range
                # check if the next row is a land
                # add the next row to the queue
                # add the cell to the visited

    # loop though each cell for islands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    
    return islands

'''
Max Area Of Island
'''
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    maxArea = 0
    visited = set()

    rows, cols = len(grid), len(grid[0])
 
    def dfs(i,j):
        if i not in range(rows) or j not in range(cols) or grid[i][j] == 0 or (i,j) in visited:
            return 0
        visited.add((i,j))
        
        return (1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j + 1) + dfs(i,j - 1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
            
                ca = dfs(r,c)
                maxArea = max(maxArea, ca)
    return maxArea


'''
Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''

# def cloneGraph(node: Optional['Node']) -> Optional['Node']:
#     oldToNew = {} #oldNode -> newNode

#     def dfs(node):
#         if node in oldToNew:
#             return oldToNew[node]
#         copy = Node(node.val)
#         oldToNew[node] = copy
#         for nei in node.neighbors:
#             copy.neighbors.append(dfs(nei))
#         return copy
#     return dfs(node)

'''
Walls and Gates (leetcode premium)

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
'''
def walls_and_gates(grid: List[List[int]]) -> List[List[int]]: # type: ignore
    
    rows,cols = len(grid), len(grid[0])
    q = collections.deque()
    # append all the cells which are gates
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                visit.add((r,c))
                q.append([r,c])
    # initialize the distance
    def addCell(r,c):
        if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visit:
            return
        visit.add((r,c))
        q.append([r,c])

    dist = 0
    # run the bfs
    while q:

        for i in range(len(q)):
            r,c = q.popleft()
            grid[r][c] = dist
            addCell(r+1,c)
            addCell(r-1,c)
            addCell(r,c+1)
            addCell(r,c-1)
        dist+=1

'''
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

def orangesRotting(grid: List[List[int]]) -> int:
    # we put the rotten oranges in
    # then do bfs to make the surrounding ornages rotten
    # if at the end any of the oranges left then return -1
    rows,cols = len(grid), len(grid[0])
    freahOranges = 0
    q = collections.deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                freahOranges += 1
            elif grid[r][c] == 2:
                q.append([r,c])
    # bfs unitl no more fresh left or until q is not empty
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0
    while q and freahOranges >0:
        for i in range(len(q)):
            pr,pc = q.popleft()
            for d in dir:
                r = d[0]+pr
                c = d[1]+pc
                if r < 0 or r == rows or c < 0  or c == cols or grid[r][c] != 1:
                    continue
                else:
                    grid[r][c] = 2
                    q.append([r,c])
                    freahOranges -= 1 
        time+=1

    return time if freahOranges == 0 else -1
# print(orangesRotting([[1,2]]))

'''

Pacific Atlantic waterflow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    res = []

    rows,cols = len(heights), len(heights[0])

    pac, atl = set(), set()

    def dfs(r,c,visit,preHeight):
        if r not in range(rows) or c not in range(cols) or (r,c) in visit or heights[r][c] < preHeight:
            return
        visit.add((r,c))
        dfs(r+1,c,visit,heights[r][c])
        dfs(r-1,c,visit,heights[r][c])
        dfs(r,c+1,visit,heights[r][c])
        dfs(r,c-1,visit,heights[r][c])

    for c in range(cols):
        dfs(0,c,pac,heights[0][c])
        dfs(rows-1,c,atl,heights[rows-1][c])

    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols-1,atl,heights[r][cols-1])

    for r in range(rows):
        for c in range(cols):
            if (r,c) in pac and (r,c) in atl:
                res.append([r,c])

    return res