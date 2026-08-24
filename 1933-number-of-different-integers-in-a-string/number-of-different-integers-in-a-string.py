class Solution:
    def numDifferentIntegers(self, w: str) -> int:
        l=[]
        s=set()
        for i in range(len(w)):
            if w[i].isdigit():
                l.append(w[i])
            else:
                if l:
                    s.add(int("".join(l)))
                    l=[]
        if l:
            s.add(int("".join(l)))
        return len(s)

        