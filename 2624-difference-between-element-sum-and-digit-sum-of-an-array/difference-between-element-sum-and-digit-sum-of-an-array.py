class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=sum(nums)
        b=0
        for n in nums:
            while n>0:
                b+=n%10
                n//=10
        return abs(a-b)