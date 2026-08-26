# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        t=head
        c=0
        while t:
            c+=1
            t=t.next
        n=c//2
        a=0
        t=head
        while t:
            if n==a+1:
                t.next=t.next.next
                break
            else:
                t=t.next
            a+=1
        return head

        