from typing import List
import collections
import heapq
'''
Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
'''
def findItinerary(tickets: List[List[str]]) -> List[str]:
    adjList = collections.defaultdict(list)
    # create a dictionary of empty lists

    for src, dest in tickets:
        heapq.heappush(adjList[src],dest) # make it a min heap by pushing values in the top
    
    
    stack = ["JFK"] # create a stack for iteration and push the first value JFK
    res = [] # keep track ofn the result

    # run while the stack is non empty
    while stack:
        # take the last value of the stack
        src = stack[-1]
        # check if it is in the dict and it has values in the list
        if src in adjList and adjList[src]:
            # append the value from the src's 
            stack.append(heapq.heappop(adjList[src]))
        else:
            # if there are no destinations left then push the result and take the src out of stack
            res.append(stack.pop())

    # return the reverse of the result
    return res[::-1]

'''

Min Cost to connect all points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''

# solution requires prim's algorithm for min heap

def minCostConnectPoints(points: List[List[int]]) -> int:
    # create a map
    adjList = {i:[] for i in range(points)}

    # assign the manhatten distance to each node and make neighbours
    N = len(points)
    
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            cost = abs(x1-x2) + abs(y1-y2)
            # it is undirected graph
            adjList[i].append([cost,j])
            adjList[j].append([cost,i])

    # Prim's Algo
    res = 0
    minH = [[0,0]] # starting at node 0 with distance cost 0 [cost, node]
    visit = set()
    
    while len(visit) < N:
        cost, i = heapq.heappop(minH)
        if i in visit:
            continue
        visit.add(i)
        res += cost
        for neiCost, nei in adjList[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost,nei])

    return res


'''
Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adjList = collections.defaultdict(list)
    for u,v,w in times:
        adjList[u].append((v,w)) #(dest, weight)
    t = 0
    minH = [[0,0]] # cost,node
    visit = set()

    while minH:
        cost, node = heapq.heappop(minH)
        if node in visit:
            continue
        visit.add(node)
        t+=cost
        for nei, weight in adjList[node]:
            heapq.heappush([cost+weight,nei])
    return t

'''
Swim in rising water

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''
def swimInWater(grid: List[List[int]]) -> int:
    rows,cols = len(grid), len(grid[0])

    t=0
    visit = set()
    minH = [[grid[0][0],0,0]] # [cost,row,col]

    while minH:
        cost, r, c = heapq.heappop(minH)
        if (r,c) in visit or r not in range(rows) or c not in range(cols):
            continue
        visit.add((r,c))
        t = max(t,cost)
        if r == rows -1 and c == cols-1:
            return t
        if r+1 in range(rows) and (r+1,c) not in visit:
            heapq.heappush(minH,[grid[r+1][c],r+1,c])
        if r-1 in range(rows) and (r-1,c) not in visit:
            heapq.heappush(minH,[grid[r-1][c],r-1,c])
        if c+1 in range(cols) and (r,c+1) not in visit:
            heapq.heappush(minH,[grid[r][c+1],r,c+1])
        if c-1 in range(cols) and (r,c-1) not in visit:
            heapq.heappush(minH,[grid[r][c-1],r,c-1])

    return 0

# print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))

'''
Alien Dictionary

There is a foreign language language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.

SUDO CODE:
   # create a adjList with key:value(set) for each char in all words

   # compare two words char by char
   # get the min length from both words
   # if length of the word 1 is greater and prefix of both words are same then return empty string as no solution exist""
   # loop through the prefix,
   # if the char are different then add them in the adj list and break

   # create a visit map where true value = in current path, false value = not in current path
   # create a res list
'''
def foreignDictionary(words: List[str]) -> str:
    adjList = {c:set() for w in words for c in w}
    incoming_edges = {c:0 for c in adjList}

    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        minL = min(len(w1),len(w2))
        if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
            return ""
        
        for j in range(minL):
            if w1[j] != w2[j]:
                adjList[w1[j]].add(w2[j])
                incoming_edges[w2[j]] += 1
                break
    q = collections.deque()
    for k, v in incoming_edges.items():
        if v == 0:
            q.append(k)
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nei in adjList[c]:
            incoming_edges[nei] -= 1
            if incoming_edges[nei] == 0:
                q.append(nei)
    
    if len(res) == len(adjList):
        return "".join(res)
    return ""

'''
Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    if dst >=n:
        return -1
    adjList = collections.defaultdict(list)
    # make the adjlist
    for s, d, c in flights:
        adjList[s].append([d,c]) #(dest, cost)
    
    # require a min head
    minH = [[0,src,k]] # cost and node
    visit = set()

    while minH:
        cost, node, step = heapq.heappop(minH)

        if node == dst:
            res = min(res,cost)

        if (node,step) in visit or step <0:
            continue
        visit.add(node,step)
        for nei, c in adjList[node]:
            if (nei,step-1) not in visit:
                heapq.heappush(minH,[c+cost, nei,step-1])
               
    return -1

# print(findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0,2,2))