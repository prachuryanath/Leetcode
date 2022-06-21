class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 1
        if n==3: return 2
        dp = [0]*(n+1)
        dp[1], dp[2], dp[3] = 1, 1, 2
        for i in range(4,n+1):
          dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]