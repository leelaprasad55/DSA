class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        a=""
        for i in words:
            a+=i
            if len(a)>len(s):
                return False
            if a==s:
                return True
        return False