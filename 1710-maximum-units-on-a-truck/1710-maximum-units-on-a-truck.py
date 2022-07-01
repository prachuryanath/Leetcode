class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse=True)
        count = 0
        for box in boxTypes:
          if truckSize < 0:
            break
          count += min(truckSize,box[0]) * box[1]
          truckSize -= box[0]
        return count