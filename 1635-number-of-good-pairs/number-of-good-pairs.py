class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        d={}
        for n in nums:
            c+=d.get(n,0)
            d[n]=d.get(n,0)+1
        return c
        