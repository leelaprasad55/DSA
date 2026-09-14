class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n=str(n)
        c=0
        for i in range(len(n)):
            if i%2==0:
                c+=int(n[i])
            else:
                c-=int(n[i])
        return c