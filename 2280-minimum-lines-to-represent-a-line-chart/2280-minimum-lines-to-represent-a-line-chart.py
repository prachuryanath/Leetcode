class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        cntr = n-1
        stockPrices.sort()
        for i in range(1,n-1):
          a, b, c = stockPrices[i-1], stockPrices[i], stockPrices[i+1]
          slope0 = (b[0] - a[0])*(c[1] - b[1])
          slope1 = (c[0] - b[0])*(b[1] - a[1])
          if slope0 == slope1:
            cntr -= 1
        return cntr