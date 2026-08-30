class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        for x in range(len(num)-2):
            if num[x]==num[x+1]==num[x+2]:
                ans=max(ans, num[x:x+3])
        return ans