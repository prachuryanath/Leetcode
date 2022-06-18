class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(value for value in nums1 if value in nums2)