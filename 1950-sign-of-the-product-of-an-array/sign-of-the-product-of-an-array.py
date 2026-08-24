class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=1
        for n in nums:
            if n>0:
                c*=1
            elif n<0:
                c*=-1
            else:
                c*=0
        return c
        