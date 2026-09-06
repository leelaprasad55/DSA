class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=set(nums1)
        n2=set(nums2)
        a=list(n1.intersection(n2))
        if a:
            return min(a)
        return -1