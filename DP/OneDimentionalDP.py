class SearchProblem(object):
    def __init__(self, N):
        self.N = N
    
    def startState(self):
        return 1
    def isEndState(self, state):
        return state == self.N
    def getSuccessors(self, state):
        result = []
        if state + 1 <= self.N:
            result.append(state + 1)
        if state + 2 <= self.N:
            result.append(state + 2)
        return result
        

def climbingStairs(problem):
    cache = {}
    def futureCost(state):
        if problem.isEndState(state):
            return 1
        if state in cache:
            return cache[state]
        result = sum(futureCost(nextState) for nextState in problem.getSuccessors(state))
        cache[state] = result


