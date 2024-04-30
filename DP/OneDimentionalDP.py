class SearchProblem(object):
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 0
    def isEndState(self, state):
        return state == self.N
    def getSuccAndCost(self, state, costList):
        result = []

        if state + 1 <= self.N:
            result.append('One Step', (state + 1), costList[state+1])
        if state + 2 <= self.N:
            result.append('Two Step', (state + 2), costList[state+2])
        return result

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

# def min_cost_climbing_stairs(cost):
    

    

