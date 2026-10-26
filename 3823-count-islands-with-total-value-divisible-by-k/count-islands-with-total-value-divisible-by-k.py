class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        c=0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 0
            s=grid[i][j]
            grid[i][j]=0
            s+=dfs(i,j-1)
            s+=dfs(i,j+1)
            s+=dfs(i-1,j)
            s+=dfs(i+1,j)
            return s
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    if dfs(i,j)%k==0:
                        c+=1
        return c
        
        