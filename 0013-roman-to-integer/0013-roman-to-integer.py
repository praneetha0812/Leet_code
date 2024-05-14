class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        prev_value = 0
        #sum of digits of roman number, 
        result = 0
       
        for char in reversed(s):
            # Get the value of the current Roman numeral
            value = roman_values[char]
            
            # If the value is less than the previous value, subtract it
            if value < prev_value:
                result -= value
            # Otherwise, add it to the result
            else:
                result += value
            
            # Update the previous value for the next iteration
            prev_value = value
        
        return result