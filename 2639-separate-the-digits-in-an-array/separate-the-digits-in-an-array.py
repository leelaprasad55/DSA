class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for n in nums:
            l.extend(map(int,str(n)))
        return l