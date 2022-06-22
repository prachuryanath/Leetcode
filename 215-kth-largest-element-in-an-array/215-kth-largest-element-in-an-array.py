class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k-1):
          maxele = max(nums)
          nums.remove(maxele)
        return max(nums)