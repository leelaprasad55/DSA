class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}        
        for i in nums:
            d[i]=d.get(i,0)+1
        c=0
        for k,v in d.items():
            if v>1:
                c+=1
        return c!=0