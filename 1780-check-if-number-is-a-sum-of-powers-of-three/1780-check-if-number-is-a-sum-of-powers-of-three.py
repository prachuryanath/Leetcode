class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
      def find_ternary(num):
        quotient = num/3   
        remainder = num%3
        if quotient == 0:  
            return ""
        else:
            return find_ternary(int(quotient)) + str(int(remainder))

      num = int(find_ternary(n))
      while num > 0:
          digit = num % 10
          if digit == 2:
            return False
          num = num // 10
      return True
      
