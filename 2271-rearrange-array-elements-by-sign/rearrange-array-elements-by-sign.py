class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]<0:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l=[]
        for i in range(len(l1)):
            l.append(l2[i])
            l.append(l1[i])
        return l