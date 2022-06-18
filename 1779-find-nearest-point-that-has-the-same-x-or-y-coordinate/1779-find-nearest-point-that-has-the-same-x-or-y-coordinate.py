class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
      min_dist, ans = float('inf'), -1
      for i, (a,b) in enumerate(points):
        if a == x or b==y:
          dist = abs(x-a) + abs(y-b)
          if dist < min_dist:
            ans, min_dist = i, dist
      return ans