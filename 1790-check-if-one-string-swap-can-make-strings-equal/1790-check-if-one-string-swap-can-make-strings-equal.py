class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
          return False
        else:
          count = 0
          s1 = list(s1)
          s2 = list(s2)
          for i in range(len(s1)):
            if s1[i] != s2[i]:
              count += 1
          if (count ==2 or count==0) and sorted(s1)==sorted(s2):
            return True
          else:
            return False