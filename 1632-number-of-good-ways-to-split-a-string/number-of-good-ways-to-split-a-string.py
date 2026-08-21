class Solution:
    def numSplits(self, s: str) -> int:
        d1={}
        d2=Counter(s)
        c=0
        for i in s:
            d1[i]=d1.get(i,0)+1
            d2[i]-=1
            if d2[i]==0:
                d2.pop(i)
            if len(d1)==len(d2):
                c+=1
        return c
        