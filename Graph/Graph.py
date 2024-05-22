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

'''

Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

def solve(board: List[List[str]]) -> None:

    rows,cols = len(board), len(board[0])

    def dfs(r,c):
        if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
            return
        board[r][c] = "T"
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]):
                dfs(r,c)
    # first run the dfs on the borders and capture the o regions into T
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
    # make all the remaining o into x

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "T":
                board[r][c] = "O"


'''
Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # create a map for each course as key and its prerequisits as values
    preMap = {i:[] for i in range(numCourses)}
    # loop through the prerequisits and put values
    for cors,pre in prerequisites:
        preMap[cors].append(pre)
    
    # create a dfs function that loops and checks for any loops
    visit = set() # set of all the visited courses

    def dfs(cors):
        if cors in visit:
            return False
        if preMap[cors] == []:
            return True
        
        visit.add(cors)
        for pre in preMap[cors]:
            if not dfs(pre): # if any of the pre requsits are visited already then return false
                return False
        visit.remove(cors)
        preMap[cors] = []
        return True
    
    for cors in range(numCourses):
        if not dfs(cors):
            return False
        
    return True


'''
Course Schedule 2

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    res = []
    # create a map for each course as key and its prerequisits as values
    preMap = {i:[] for i in range(numCourses)}
    # loop through the prerequisits and put values
    for cors,pre in prerequisites:
        preMap[cors].append(pre)
    
    # create a dfs function that loops and checks for any loops
    visit = set() # set of all the visited courses
    cycle = set()

    def dfs(cors):
        if cors in cycle:
            return False
        if cors in visit:
            return True
        
        cycle.add(cors)
        for pre in preMap[cors]:
            if not dfs(pre): # if any of the pre requsits are visited already then return false
                return False
        cycle.remove(cors)
        visit.add(cors)
        res.append(cors)
        return True
    
    for cors in range(numCourses):
        if not dfs(cors):
            return []
    return res
# print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))

'''
Graph valid tree
'''
def validTree(n: int, edges: List[List[int]]) -> bool:
    if not n:
        return True
    adjList = {i:[] for i in range(n)}
    for n1, n2 in edges:
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    visit = set()
    def dfs(curr, prev):
        if curr in visit:
            return False
        visit.add(curr)
        for nei in adjList[curr]:
            if nei == prev:
                continue
            if not dfs(nei,curr):
                return False
        return True
    
    return dfs(0,-1) and n == len(visit)

'''
Number of Connected components

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.
'''
def countComponents(n: int, edges: List[List[int]]) -> int:
    visit = set()
    adjList = {i:[] for i in range(n)}
    for n1,n2 in edges:
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    
    def dfs(node):
        if node in visit:
            return
        visit.add(node)
        for nei in adjList[node]:
           if nei not in visit:
               dfs(nei)
    components = 0
    for i in range(n):
        if i not in visit:
            components += 1
            dfs(i)
    return components

'''

Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''
def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    
    # using the union find algorithm
    # requires a rank and parent 
    par = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) +1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p
    def union(n1,n2):
        p1,p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True
    
    for n1,n2 in edges:
        if not union(n1,n2):
            return [n1,n2]
    return []
