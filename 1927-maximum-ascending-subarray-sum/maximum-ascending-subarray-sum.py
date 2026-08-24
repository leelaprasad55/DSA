class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        t=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                t+=nums[i]
            else:
                t=nums[i]
            m=max(m,t)
        return m
        