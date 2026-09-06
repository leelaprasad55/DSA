class Solution:
    def isCircularSentence(self, s: str) -> bool:
        l=s.split(" ")
        if len(l)==1:
            return l[0][0]==l[0][-1]
        if l[0][0]!=l[-1][-1]:
            return False
        for i in range(len(l)-1):
            if l[i][-1]!=l[i+1][0]:
                return False
        return True
        