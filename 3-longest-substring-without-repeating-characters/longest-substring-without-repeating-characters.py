class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        j=0
        m=0
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[j])
                j+=1
            se.add(s[i])
            m=max(m,i-j+1)
        return m
            