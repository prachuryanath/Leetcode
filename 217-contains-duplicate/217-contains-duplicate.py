class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numt = set(nums)
        if len(numt) != len(nums):
            return True
        else:
            return False
                