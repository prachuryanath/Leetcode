class Solution:
    def repeatedCharacter(self, s: str) -> str:
        S = set()

        for x in s:
            if x in S:
                return x
            else:
                S.add(x)
