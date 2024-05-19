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
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(int(132//136))