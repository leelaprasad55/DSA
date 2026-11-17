class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        l={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def bt(ix,s):
            if ix==len(digits):
                r.append(s[:])
                return 
            for le in l[digits[ix]]:
                bt(ix+1,s+le)
        
        r=[]
        bt(0,"")
        return r