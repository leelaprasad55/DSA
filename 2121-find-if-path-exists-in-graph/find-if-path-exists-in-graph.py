class Solution:
    def validPath(self, n: int, edges: List[List[int]], s: int, d: int) -> bool:
        if d==s:
            return True
        k=True
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        v=set()
        def dfs(n):
            if n==d:
                return True
            v.add(n)
            for i in g[n]:
                if i not in v:
                    if dfs(i):
                        return True
            return False
        return dfs(s)
