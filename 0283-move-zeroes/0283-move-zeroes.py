class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        prev = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                hold = nums[prev]
                nums[prev] =nums[i]
                nums[i]=hold
                prev +=1

                