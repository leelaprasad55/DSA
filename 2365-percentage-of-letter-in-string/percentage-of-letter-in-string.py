class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d={}
        l=len(s)
        for c in s:
            d[c]=d.get(c,0)+1
        c=d.get(letter,0)
        return c*100//l
        