class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        win_sum = sum(cardPoints[:k])
        ans = win_sum
        for i in range(1,k+1):
            win_sum = win_sum - cardPoints[k-i] + cardPoints[-i]
            ans = max(ans, win_sum)
        return ans        