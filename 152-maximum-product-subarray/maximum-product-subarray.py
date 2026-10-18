class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ma=nums[0]
        mi=nums[0]
        k=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                mi,ma=ma,mi
            ma=max(x,ma*x)
            mi=min(x,mi*x)
            k=max(k,ma)
        return k