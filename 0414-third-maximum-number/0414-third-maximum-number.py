class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second= third = float('-inf')
        for i in nums:
            if i in (first, second, third):
                continue
            if i > first:
                first, second, third = i, first, second
            elif i > second:
                second, third = i, second
            elif i > third:
                third = i
        return third if third != float('-inf') else first
                
        