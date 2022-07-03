class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        l, r = m-1, 0
        while l>=0 and r<n:
          if mat[l][r] == target:
            return True
          elif mat[l][r] < target:
            r += 1
          else:
            l -= 1
        return False
            