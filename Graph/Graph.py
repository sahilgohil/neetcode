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

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    oldToNew = {} #oldNode -> newNode

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node)
