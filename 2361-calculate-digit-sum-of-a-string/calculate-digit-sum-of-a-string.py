class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            t=""
            for i in range(0,len(s),k):
                ck=s[i:i+k]
                cks=sum(int(num) for num in ck)
                t+=str(cks)
            s=t
        return s
