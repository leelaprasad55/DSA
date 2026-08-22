class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        for l in accounts:
            a.append(sum(l))
        return max(a)