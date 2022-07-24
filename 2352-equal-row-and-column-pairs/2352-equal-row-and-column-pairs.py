class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n =len(grid)
        trans = [[grid[j][i] for j in range(n)] for i in range(n)]
        count = 0
        for row in grid:
          for column in trans:
            if row == column:
              count += 1
        return count