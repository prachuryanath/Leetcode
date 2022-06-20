class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n):
            sum+= mat[i][i]
            mat[i][i] = 0
            sum+= mat[-i-1][i]
        return sum
