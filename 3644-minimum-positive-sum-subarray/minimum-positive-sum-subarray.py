class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mn=float('inf')
        n=len(nums)
        a=[0]*(n+1)
        for i in range(n):
            a[i+1]=a[i]+nums[i]
        for e in range(l,n+1):
            smin=max(0,e-r)
            smax=e-l
            for s in range(smin,smax+1):
                s=a[e]-a[s]
                if s>0:
                    mn=min(mn,s)
        return mn if mn!=float('inf') else -1