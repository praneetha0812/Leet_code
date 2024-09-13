class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # intiating left and right pointers
        left = 0
        right = len(s)-1
        #checking the condition
        while left < right:
             #swappinf left and right elements 
                hold = s[left]
                s[left]= s[right]
                s[right]= hold
                
                #incrementing left pointer so that it can cover the rest elements in array
                left += 1
               #decrementing right pointer so that it can cover the rest elements in array
                right -= 1