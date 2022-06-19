class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      for i in range(1,len(nums)):
        ans = nums[i-1]
        nums[i] += ans
      return nums
        