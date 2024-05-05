# May 3 2024
'''
165. Compare version numbers
we will solve this problem by splitting the string by .
the result list will contain the string format of numbers
we will compare each numbers
if v1num > v2 number return 1
if v2num > v1 number return -1
if the length of the strings are not equal then consider the remaining numbers as 0 for comparision
at the end if we cannot find any answer then return 0
'''
from typing import List


def compareVersion( version1: str, version2: str) -> int:
    v1 = version1.split('.')
    v2 = version2.split('.')

    for i in range(max(len(v1), len(v2))):
        v1Num = int(v1[i]) if i < len(v1) else 0
        v2Num = int(v2[i]) if i < len(v2) else 0

        if v1Num > v2Num:
            return 1
        if v2Num > v1Num:
            return -1
    return 0

# May 2 2024
'''
2441. Largest Positive Integer That Exists With Its Negative
we create a set of the list
then we will sort the array and from left to right we will try finding the solution
if we encounter any negative value we break the loop and return -1


'''
def findMaxK(nums: List[int]) -> int:
    numSet = set()
    largest = -1

    for n in nums:
        if -n in numSet:
            largest = max(largest, abs(n))
        else:
            numSet.add(n)
    return largest

# print(findMaxK([-1,2,-3,3]))


# May 1 2024
'''
2000. Reverse Prefix of Word
to solve this problem we will first get the first index of the character c
now we will use that index to make a substring from 0 to i
then reverse loop it and make a new string
join that new string with i+1 index of the string if the first occurence was not the last index 
if it was then return the reversed string as it is
'''
def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word
    idx = word.index(ch)
    subString = word[:idx+1]
    reversedString = ""
    for i in range(len(subString)-1, -1,-1):
        reversedString += subString[i]
    if idx + 1 == len(word):
        return reversedString
    return reversedString+word[idx+1:]
print(reversePrefix("abccd",'c'))

# May 4 2024
'''

'''