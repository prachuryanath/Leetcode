class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        ans = 0
        for value in counts.values():
          ans += value//2 *2
          if ans % 2 == 0 and value % 2 == 1:
            ans += 1
        return ans            