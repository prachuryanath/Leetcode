class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right+1):
          for char in str(num):
            if int(char) == 0 or num % int(char) != 0:
              break
          else:
            ans.append(num)
        return ans