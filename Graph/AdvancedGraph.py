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