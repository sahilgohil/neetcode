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