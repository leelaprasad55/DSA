class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        k=image[sr][sc]
        if k==color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=len(image) or c>=len(image[0]) :
                return 
            if image[r][c]!=k:
                return
            image[r][c]=color
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        dfs(sr,sc)    
        return image    