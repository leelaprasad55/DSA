class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split(" ")
        r=[""]*len(l)
        for i in l:
            n=int(i[-1])-1            
            r[n]=i[:-1]
        return " ".join(r)
        