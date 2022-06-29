class Solution:
    def judgeSquareSum(self, c: int) -> bool:
      a, b = 0, int(sqrt(c))
      while a<=b:
        total = a**2 + b**2
        if c == total:
          return True
        elif total < c:
            a += 1
        else:
            b -= 1
      return False