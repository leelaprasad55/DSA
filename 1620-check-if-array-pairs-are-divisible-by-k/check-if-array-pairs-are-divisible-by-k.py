class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        d=[0]*k
        for nu in arr:
            r=(nu%k+k)%k
            d[r]+=1
        if d[0]%2!=0:
            return False
        for i in range(1,k//2+1):
            if d[i]!=d[k-i]:
                return False
        return True 