class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = [idx for idx, x in enumerate(nums) if x==target]
        return ans        