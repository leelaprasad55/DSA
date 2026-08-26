class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        d={}
        for j in nums1:
            d[j]=d.get(j,0)+1
        for j in nums2:
            d[j]=d.get(j,0)+1
        for j in nums3:
            d[j]=d.get(j,0)+1
        l=[]
        for k,v in d.items():
            if v>=2:
                l.append(k)
        return l