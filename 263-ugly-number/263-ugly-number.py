class Solution:
    def isUgly(self, n: int) -> bool:
        if n>0:
          for i in range(2,6):
            while n%i ==0:
              n = n/i
        return n==1