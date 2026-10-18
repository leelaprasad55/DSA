class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        k=0
        while l<=r:
            m=(l+r)//2
            if m*m<=x:
                k=m
                l=m+1
            else:
                r=m-1
        return k