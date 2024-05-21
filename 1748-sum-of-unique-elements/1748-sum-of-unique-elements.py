class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
                if i in count:
                    count[i] +=1
                else:
                    count[i] = 1
        sum = 0
        for i, frequency in count.items():
            if frequency == 1:
                sum = sum + i
        return sum
          