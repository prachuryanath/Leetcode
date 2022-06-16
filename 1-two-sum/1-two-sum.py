class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            rem = target - n
            if rem in nums and i!=nums.index(rem):
                return i, nums.index(rem)