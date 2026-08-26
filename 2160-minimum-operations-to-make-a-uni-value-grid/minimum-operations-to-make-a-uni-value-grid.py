class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l=[]
        for li in grid:
            l.extend(li)
        r=l[0]%x
        for n in l:
            if n%x!=r:
                return -1
        l.sort()
        m=l[len(l)//2]
        op=0
        for n in l:
            op+=abs(n-m)//x
        return op