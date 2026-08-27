# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        t=d
        t1=head
        s=0
        while t1:
            if t1.val==0:
                if s>0:
                    t.next=ListNode(s)
                    t=t.next
                    s=0
            else:
                s+=t1.val
            t1=t1.next
        return d.next
        