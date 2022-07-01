class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
      return sum([self.binarySearch(arr) for arr in grid])
      
    def binarySearch(self,arr):
      l, r = 0, len(arr)-1
      while l<=r:
        mid = (l+r)//2
        if arr[mid] < 0:
          r = mid-1
        else:
          l = mid+1
      return len(arr) - l
