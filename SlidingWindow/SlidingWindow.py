from typing import List

'''
Best time to buy and sell stock

'''
arr = [1,2,3,4,5,6,7]
k = 2
for i in range(0,len(arr)-1-k,k):
    for j in range(i,i+k):
        print("sub array 1")
        
        print(arr[j])


    
