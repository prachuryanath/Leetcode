class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
          if num<0:
            count +=1
        if 0 in nums:
          return 0
        elif count%2!=0:
          return -1
        else:
          return 1