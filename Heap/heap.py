from typing import List
import heapq
import collections
'''
Kth largest element in a stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minH = []
        for n in nums:
            heapq.heappush(self.minH,n)

    def add(self, val: int) -> int:
        heapq.heappush(self.minH,val)
        while(len(self.minH) > self.k):
            heapq.heappop(self.minH)
        return self.minH[0]
    
'''
Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
'''
def lastStoneWeight(stones: List[int]) -> int:
    maxH = []
    for stone in stones:
        heapq.heappush(maxH, -stone)
    while len(maxH) >1:
        y = -heapq.heappop(maxH)
        x = -heapq.heappop(maxH)
        if x == y:
            continue
        else:
            heapq.heappush(maxH,-(y-x))

    return -heapq.heappop(maxH) if len(maxH) > 0 else 0

'''
K closest point to the origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

create a min heap where heap is (dis, index of the points)
put them in the minHeap
while k > 1: pop the elements
get the point's index and return the points
'''
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    minH = []
    i = 0
    for x,y in points:
        dis = (x*x) + (y*y)
        heapq.heappush(minH,(dis,i))
        i+=1
    res = []

    while k>0:
        idx = heapq.heappop(minH)[1]
        res.append(points[idx])
        k-=1
    return res
# print(kClosest([[1,3],[-2,2]],1))


'''
Kth largest element in the array

'''
def findKthLargest(nums: List[int], k: int) -> int:
    minH = []
    for n in nums:
        heapq.heappush(minH,n)
    while(len(minH) > k):
        heapq.heappop(minH)
    return minH[0]


'''
Task Scheduler


'''
def leastInterval(self, tasks: List[str], n: int) -> int:
    '''
    first make the hashmap with key as (taskchar, its priority)
    every loop we check if the char exist in the hashmap then we take its value
    and and add n to it and push the new char in the heap

    '''
    count = collections.Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)
    q = collections.deque()
    time = 0
    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt,time+n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time