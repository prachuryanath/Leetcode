class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      if not nums2:
        return None

      mapping = {}
      result = []
      stack = []
      stack.append(nums2[0])

      for i in range(1, len(nums2)):
        while stack and nums2[i] > stack[-1]:     
          mapping[stack[-1]] = nums2[i]          
          stack.pop()
        stack.append(nums2[i])    
        print(stack)
        
      return [mapping.get(n, -1) for n in nums1]
