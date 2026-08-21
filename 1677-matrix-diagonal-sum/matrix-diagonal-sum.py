class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        r=0
        for i in range(n):
            r+=mat[i][i]+mat[i][n-i-1]
        if n%2==1:
            r-=mat[n//2][n//2]
        return r