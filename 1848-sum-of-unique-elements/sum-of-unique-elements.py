class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        f=Counter(nums)
        return sum(x for x in nums if f[x]==1)