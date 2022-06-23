class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        while x:
          dig = x%10
          ans = ans*10 + dig
          x = x// 10
        return 0 if pow(2,31) < ans else symbol * ans