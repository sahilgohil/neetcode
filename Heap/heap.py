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