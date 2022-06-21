class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1, w = collections.Counter(s1), len(s1)

        for i in range(len(s2)):
          if s2[i] in count1:
            count1[s2[i]] -= 1
          if i>= w and s2[i-w] in count1:
            count1[s2[i-w]] += 1
          if all([count1[i]== 0 for i in count1]):
            return True
        return False