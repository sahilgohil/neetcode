from typing import List, Optional
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
Reverse the linked list

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
   
    if not head:
        return None
    newhead = head
    if head.next:
        newhead = reverseList(head.next)
        head.next.next = head
    head.next = None


    return newhead

'''
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    while list1:
        curr.next = list1
        curr = curr.next
        list1 = list1.next
    while list2:
        curr.next = list2
        curr = curr.next
        list2 = list2.next
    return dummy.next


'''
Merge K sorted lists
'''

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    newSortedList = None
    while len(lists) >1:
        list1 = lists.pop()
        newSortedList = mergeTwoLists(newSortedList,list1)
    if len(lists) == 1:
        list1 = lists.pop()
        newSortedList = mergeTwoLists(newSortedList,list1)
    return newSortedList


'''
Reorder the List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def reorderList(head: ListNode) -> None:
    if not head:
        return
    s, f = head, head.next
    while f and f.next:
        s = s.next
        f = f.next.next
    
    second = s.next
    s.next = None
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    # prev is second half and head is the first half
    while head and prev:
        htmp = head.next
        ptmp = prev.next
        head.next = prev
        prev.next = htmp
        head = htmp
        prev = ptmp


'''
Remove the Nth node from the end of the list

Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return head
    size = 0
    curr = head
    while curr:
        size += 1
        curr = curr.next
    if size == n:
        return head.next
    remove = size-n
    count = 1
    curr = head
    while True:
        if remove == count:
            curr.next = curr.next.next
            break
        curr = curr.next
        count += 1
    return head


'''
Copy random list pointer
make a deep copy of the linked list
'''
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    copyMap = {} # (old:new)
    '''
    each node has its own value
    -> create new node with its value if it does not already exist
    -> create the next node with its value if it does not already exist
    -> create the random node with the value given if it does not exist
    '''
    def dfs(node):
        if not node:
            return node
        if node in copyMap:
            return copyMap[node]
        newNode = Node(node.val)
        copyMap[node] = newNode
        newNode.next = dfs(node.next)
        newNode.random = dfs(node.random)
        return newNode
    return dfs(head)

'''
Add two numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = ListNode(-1)
    res = dummy
    while l1 and l2:
        currSum = l1.val + l2.val + carry
        newNode = ListNode(currSum % 10)
        carry = currSum // 10
        res.next = newNode
        res = res.next
        l1 = l1.next
        l2 = l2.next
    while l1:
        currSum = l1.val + carry
        newNode = ListNode(currSum % 10)
        carry = currSum // 10
        res.next = newNode
        res = res.next
        l1 = l1.next
    while l2:
        currSum = l2.val + carry
        newNode = ListNode(currSum % 10)
        carry = currSum // 10
        res.next = newNode
        res = res.next
        l2 = l2.next
    if carry > 0:
        newNode = ListNode(carry)
        res.next = newNode
    return dummy.next

'''
Find If Linked List has a cycle
'''
def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    s,f = head,head.next
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True
        
    return False

'''
find duplicate number using the constant extra space
'''
def findDuplicate(nums: List[int]) -> int:
    s = 0
    f = 0
    while True:
        s = nums[s]
        f = nums[nums[f]]
        if s == f:
            break
    s2 =0
    while True:
        s = nums[s]
        s2 = nums[s2]
        if s == s2:
            return s
'''
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''    

class DoubleNode:
        def __init__(self, key, value):
           self.k = key
           self.v = value
           self.next = None
           self.prev = None
class LRUCache:
            
    def __init__(self, capacity: int):
       self.cap = capacity
       self.cache = {}
       self.left = DoubleNode(-1,-1)
       self.right = DoubleNode(-1,-1)
       self.left.next = self.right
       self.right.prev = self.left

    def insert(self,node):
        rightPrev = self.right.prev
        node.next = self.right
        node.prev = rightPrev
        rightPrev.next = node
        self.right.prev = node
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].v
        return -1
        
    def put(self, key: int, value: int) -> None:
        # remove from the list
        if key in self.cache:
            self.remove(self.cache[key])
        # create new node
        self.cache[key] = DoubleNode(key,value)
        self.insert(self.cache[key])
        
        # now check if the capacity is reached or not
        if len(self.cache) > self.cap:
            removalNode = self.left.next
            self.remove(removalNode)
            del self.cache[removalNode.k]
            
            

'''
Reverse nodes in k-group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]: