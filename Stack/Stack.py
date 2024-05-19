from typing import List
'''
Evaluate reverse polish notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.
'''
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for t in tokens:
        if t == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(add(a,b))
        elif t == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(subtract(a,b))
        elif t == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(multiply(a,b))
        elif t == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(divide(a,b))
        else:
            stack.append(int(t))
        
    return stack.pop()
def divide(a,b):
    return int(a/b)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
# print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(int(132//136))

'''
Generate Parenthesis


'''
def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []

    # add to the res if openN and closeN are n
    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
        
        # only add open if open is less than n
        if openN < n:
            stack.append("(")
            backtrack(openN+1,closeN)
            stack.pop()
        
        # only add closed if the closeN is less than openN
        if closeN < openN:
            stack.append(")")
            backtrack(openN,closeN+1)
            stack.pop()

    backtrack(0,0)
    return res

# print(generateParenthesis(3))

'''
Daily Temperature

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = [] #(index, value)
    res = [0] * len(temperatures)
    for i,t in enumerate(temperatures):
        while stack and t > stack[len(stack)-1][1]:
            top = stack.pop()
            res[top[0]] = i - top[0]
        stack.append((i,t))
    return res
# print(dailyTemperatures([73,74,75,71,69,72,76,73]))


'''
Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
'''
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, s] for p, s in zip(position,speed)]
    stack = []

    for p, s in sorted(pair)[::-1]: # sorted in reverse order:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the car behind has the high speed, -1 is behind -2
            stack.pop()

    return len(stack)


'''
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] #[index, height] 
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, (height * (i-index)))
            start = index
        stack.append([start,h])
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea