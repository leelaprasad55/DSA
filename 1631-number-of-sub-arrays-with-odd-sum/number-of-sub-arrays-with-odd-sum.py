class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        e,o,p=1,0,0
        for i in arr:
            p^=(i&1)
            if p:
                o+=1
            else:
                e+=1
        return (o*e)%(10**9+7)
        