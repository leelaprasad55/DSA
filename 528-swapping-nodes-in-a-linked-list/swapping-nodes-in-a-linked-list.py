# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t=head
        l=[]
        while t:
            l.append(t.val)
            t=t.next
        n=len(l)
        if n<=1:
            return head
        a=l[k-1]
        b=l[-k]
        c=1
        n1=n-k+1
        t=head
        while t:
            if c==k:
                t.val=b
            elif c==n1:
                t.val=a
            t=t.next
            c+=1
        return head
        