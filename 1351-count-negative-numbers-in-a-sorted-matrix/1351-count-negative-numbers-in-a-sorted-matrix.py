class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for num in grid:
          for number in num:
            if number < 0:
              count += 1
        return count