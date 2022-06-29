class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c))+1):
          target = c - a**2
          l, r = 0, sqrt(c)
          while l<=r:
            mid = (l+r)//2
            if mid**2 == target:
              return True
            elif mid**2 > target:
              r = mid-1
            else:
              l = mid+1
        return False