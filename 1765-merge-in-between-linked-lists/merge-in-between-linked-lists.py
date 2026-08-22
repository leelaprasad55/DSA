# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        t1=list1
        t2=list1
        while t1 and a>0:
            a-=1
            t1=t1.next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        t1=list1
        for _ in range(a-1):
            t1=t1.next  
        t2=list1
        for _ in range(b):
            t2=t2.next
        ab=t2.next  
        t1.next=list2 
        t=list2
        while t.next:
            t=t.next  
        t.next=ab  
        return list1
        