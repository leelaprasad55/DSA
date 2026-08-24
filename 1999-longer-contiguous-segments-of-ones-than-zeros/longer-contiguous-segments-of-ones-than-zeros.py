class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        c1=0
        c0=0
        m1=0
        m2=0
        for i in range(len(s)):
            if s[i]=='1':
                c1+=1
                c0=0
                m1=max(m1,c1)
            else:
                c0+=1
                c1=0
                m2=max(m2,c0)
        return m1>m2
                
                