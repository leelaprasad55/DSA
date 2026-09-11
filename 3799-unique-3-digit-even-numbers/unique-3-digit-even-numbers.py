from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        k=set()
        for i,j,k1 in permutations(digits,3):
            if i!=0 and k1%2==0:
                k.add((i,j,k1))
        return len(k)