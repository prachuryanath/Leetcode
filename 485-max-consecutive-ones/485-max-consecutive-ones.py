class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cstreak = mstreak = 0
        for i in range(len(nums)):
          if nums[i] == 1:
            cstreak +=1
          else:
            mstreak = max(cstreak,mstreak)
            cstreak = 0
        return max(cstreak,mstreak)