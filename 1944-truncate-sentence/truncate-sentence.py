class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split(" ")
        a=" ".join(l[:k])
        return a