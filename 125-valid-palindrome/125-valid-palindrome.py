class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum())
        s = s.lower()
        for i in range(len(s)-1):
          if s[i] != s[len(s)- 1 - i]:
            return False
        return True
            