class Solution:
    def trap(self, h: list[int]) -> int:
        st=[]
        t=0
        for i in range(len(h)):
            while st and h[st[-1]]<h[i]:
                p=h[st.pop()]
                if not st:
                    break
                dis=i-st[-1]-1
                k=min(h[st[-1]],h[i])
                k-=p
                t+=dis*k
            st.append(i)
        return t