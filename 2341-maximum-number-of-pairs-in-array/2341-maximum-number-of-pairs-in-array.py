class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s = collections.Counter(nums)
        ans = [0]*2
        for v in s.values():
            ans[0] += (v//2)
            ans[1] += (v%2)
        return ans
