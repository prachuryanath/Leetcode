class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.append(0)
        hc.append(h)
        vc.append(0)
        vc.append(w)
        
        hc.sort()
        vc.sort()
        
        l, r = 0, 0
        
        for i in range(1,len(hc)):
          l = max(l, hc[i] - hc[i-1])
        for j in range(1,len(vc)):
          r = max(r, vc[j] - vc[j-1])
        
        return (l*r)%1000000007
        