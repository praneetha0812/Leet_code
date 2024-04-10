class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending with 0 are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # Reverse the number
        reversed_x = 0
        original_x = x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        # Check if the original number is the same as the reversed number
        return original_x == reversed_x

       