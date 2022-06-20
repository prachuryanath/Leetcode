class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
          return []
        nums.sort()
        count = set()
        for i,v in enumerate(nums[:-2]):
          if i>=1 and v == nums[i-1]:
            continue
          d = {}
          for x in nums[i+1:]:
            if x not in d:
              d[-v-x] = 1
            else:
              count.add((v,-v-x,x))
        return map(list,count)
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
