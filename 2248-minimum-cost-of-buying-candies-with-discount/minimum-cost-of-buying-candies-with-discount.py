class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        s=sorted(cost,reverse=True)
        a=[0]
        a.extend(s)
        c=0
        for n in range(len(a)):
            if n%3==0:
                continue
            else:
                c+=a[n]
        return c