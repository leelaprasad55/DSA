class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m=-1
        for i in nums:
            if -i in nums:
                m=max(m,i)
        return m