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
    