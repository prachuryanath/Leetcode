from math import *
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            tmp = int(n / 5)
            count += tmp
            n = tmp
        return count
