class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        frequency.sort(reverse=True)
        
        res = 0
        max_freq = len(s)
        
        for freq in frequency:
          if freq > max_freq:
            res += freq - max_freq
            freq = max_freq
          max_freq = max(0,freq-1)
        return res