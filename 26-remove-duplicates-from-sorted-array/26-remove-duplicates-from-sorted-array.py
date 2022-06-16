class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        result = 1
        for i in range(length-1):
            if nums[i] != nums[i+1]:
                nums[result] = nums[i+1] 
                result +=1
        return result

