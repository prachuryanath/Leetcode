class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
        
        for num in c1:
            if num in c2: 
              ans.extend([num]*min(c1[num], c2[num]))
        return ans