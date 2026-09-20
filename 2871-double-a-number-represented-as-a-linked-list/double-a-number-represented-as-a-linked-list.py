# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        c=0
        for i in range(len(l)-1,-1,-1):
            v=l[i]*2+c
            l[i]=v%10
            c=v//10
        if c:
            l.insert(0,c)
        d=ListNode(0)
        t=d
        for v in l:
            t.next=ListNode(int(v))
            t=t.next
        return d.next
        