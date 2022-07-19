class Solution:
    def getRow(self, ind: int) -> List[int]:
        res = [[1]*(i+1) for i in range(ind+1)]
        for i in range(2, ind+1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[ind]
