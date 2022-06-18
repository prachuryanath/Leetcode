class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numdone = []
        for i in range(len(numbers)):
          if not numbers[i] in numdone:
            numdone.append(numbers[i])
            l, r = i+1, len(numbers)-1
            Key = target - numbers[i]
            while l<=r:
              mid = (l+r)//2
              if Key == numbers[mid]:
                return([i+1,mid+1])
              elif Key > numbers[mid]:
                l = mid+1
              elif Key < numbers[mid]:
                r = mid-1