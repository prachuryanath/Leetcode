class Solution:
    def minPartitions(self, n: str) -> int:
      digit = [char for char in n]
      return max(digit)