import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        p=1
        l=0
        mx=2
        for r,v in enumerate(nums):
            while math.gcd(p,v)>1:
                p//=nums[l]
                l+=1
            p*=v
            mx=max(mx,r-l+1)
        return mx       