class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if not nums:
        return 0
      nums.sort()
      lstreak = cstreak = 1
      for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
          if nums[i] == nums[i-1]+1:
            cstreak +=1
          else:
            lstreak = max(lstreak, cstreak)
            cstreak = 1
      return max(lstreak,cstreak)