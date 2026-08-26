class Solution:
    def maxDistance(self, c: List[int]) -> int:
        m=0
        for i in range(len(c)-1):
            for j in range(i+1,len(c)):
                if c[i]!=c[j]:
                    m=max(m,abs(i-j))
        return m
        