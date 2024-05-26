from typing import List
import heapq
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