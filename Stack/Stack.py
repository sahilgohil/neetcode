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
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
