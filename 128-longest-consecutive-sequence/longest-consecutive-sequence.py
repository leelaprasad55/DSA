class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sn=set(nums)
        m=0
        for n1 in sn:
            if n1-1 not in sn:
                c=1
                n=n1
                while n+1 in sn:
                    n+=1
                    c+=1 
                m=max(m,c)
        return m