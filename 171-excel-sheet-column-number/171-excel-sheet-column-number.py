class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        for i, c in enumerate(reversed(columnTitle.upper())):
            val += (26**i) * (ord(c) - 64)
            
        return val
