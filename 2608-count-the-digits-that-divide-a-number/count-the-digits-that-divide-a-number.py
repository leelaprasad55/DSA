class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        a=str(num)
        for n in a:
            if n!="0" and num%int(n)==0:
                c+=1
        return c
        