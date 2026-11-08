class Solution:
    def countServers(self, g: list[list[int]]) -> int:
        n=len(g)
        m=len(g[0])
        r=[0]*n
        c=[0]*m
        for i in range(n):
            for j in range(m):
                if g[i][j]==1:
                    r[i]+=1
                    c[j]+=1

        cl=0
        for i in range(n):
            for j in range(m):
                if g[i][j]==1 and (r[i]>1 or c[j]>1):
                    cl+=1
        return cl
        