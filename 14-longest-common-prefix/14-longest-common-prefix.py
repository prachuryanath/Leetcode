class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = min(strs)
        s2 = max(strs)

        for key, value in enumerate(s1):
            if value != s2[key]:
                return s1[:key] #stop until hit the split index
        return s1
