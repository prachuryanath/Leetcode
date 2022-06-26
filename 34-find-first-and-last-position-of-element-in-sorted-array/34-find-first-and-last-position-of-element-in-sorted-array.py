class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchFindPos(nums: List[int], target: int, find_start: bool=True):
            l, r, res = 0, len(nums)-1, -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    res = mid
                    if find_start:
                        r = mid-1
                    else:
                        l = mid+1
                if nums[mid] < target:
                    l = mid + 1
                if nums[mid] > target:
                    r = mid - 1
            return res
        
        start = binarySearchFindPos(nums, target)
        end = binarySearchFindPos(nums, target, False)
        return [start, end]
        