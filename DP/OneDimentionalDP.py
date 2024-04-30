
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

def min_cost_climbing_stairs(costs):
    cache = {}
    n = len(costs)
    def recursion(i):
        if i in cache:
            return cache[i]
        if i<0:
            return 0;
        
        one_step_cost = costs[i] + recursion(i-1)
        two_step_cost = costs[i] + recursion(i-2)
        cache[i] = min(one_step_cost, two_step_cost)
        return cache[i]
    return min(recursion(n-1), recursion(n-2))

print(min_cost_climbing_stairs([10,15,20]))


        


    

    

