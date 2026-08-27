class Solution:
    def countEven(self, num: int) -> int:
        c=sum(map(int,str(num)))
        return num//2 if c%2==0 else (num-1)//2
        