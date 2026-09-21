class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        l=set()
        for li in bulbs:
            if li in l:
                l.remove(li)
            else:
                l.add(li)
        return sorted(l)
        