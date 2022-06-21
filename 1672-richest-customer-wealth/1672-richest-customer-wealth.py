class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        msum = 0
        for account in accounts:
          csum = sum(account)
          msum = max(csum, msum)
        return msum