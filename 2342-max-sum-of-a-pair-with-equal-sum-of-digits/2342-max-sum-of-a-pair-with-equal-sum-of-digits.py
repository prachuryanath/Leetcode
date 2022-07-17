class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
          s = str(num)
          key = 0
          for j in s:
            key += int(j)
          d[key].append(num)
        ans = -1
        for digit in d:
          s = sorted(d[digit])
          if len(s) >= 2:
            ans = max(ans, s[-1] + s[-2])
        return ans
