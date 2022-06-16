class Solution:
    def countElements(self, nums: List[int]) -> int:
        mint,maxt = min(nums), max(nums)
        return sum(1 for x in nums if mint<x<maxt)
