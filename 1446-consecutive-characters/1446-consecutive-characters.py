class Solution:
    def maxPower(self, s: str) -> int:
        string = list(s)
        cstreak = mstreak = 1
        for i in range(len(string)-1):
          if string[i] == string[i+1]:
            cstreak +=1
          else:
            mstreak = max(cstreak,mstreak)
            cstreak = 1
        return max(cstreak,mstreak)