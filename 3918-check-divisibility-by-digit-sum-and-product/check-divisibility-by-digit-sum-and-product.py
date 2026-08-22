class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        t=n
        while t>0:
            r=t%10
            s+=r
            p*=r
            t//=10
        c=s+p
        return True if n%c==0 else False