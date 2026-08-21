class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n=len(arr)
        arr.sort()
        if n==2:
            return True
        for i in range(n-2):
            if arr[i+1]-arr[i]!=arr[i+2]-arr[i+1]:
                return False
        return True
        