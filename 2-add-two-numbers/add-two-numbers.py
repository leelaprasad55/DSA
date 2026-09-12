# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1 , l2):
        car=0
        res=ListNode(0)
        poi=res
        while l1 or l2 or car:
            f=l1.val if l1 else 0
            s=l2.val if l2 else 0
            sum=f+s+car
            num=sum%10
            car=sum//10
            poi.next=ListNode(num)
            poi=poi.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return res.next