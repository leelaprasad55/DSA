class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        s11=""
        s12=""
        s21=""
        s22=""
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
                if c==1:
                    s11=s1[i]
                    s21=s2[i]
                if c==2:
                    s12=s1[i]
                    s22=s2[i]
            if c>2:
                return False
        if c==0:
            return True
        return s11==s22 and s12==s21