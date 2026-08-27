# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l,l1=[],[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        n=len(l)
        ans=0
        for i in range(n//2):
            ans=max(ans,l[i]+l[-i-1])
        return ans

        