class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if low%2==0:
            if high%2==0:
                return int(diff/2)
            else:
                return int(diff//2 +1)
        else:
            if high%2==0:
                return int(diff//2 +1)
            else:
                return int(diff/2 + 1)