class Solution:
    def capitalizeTitle(self, t: str) -> str:
        l=t.split()
        for i in range(len(l)):
            if len(l[i])<=2:
                l[i]=l[i].lower()
            else:
                l[i]=l[i].capitalize()
        return " ".join(l)