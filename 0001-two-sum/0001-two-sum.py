class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):  # Iterate over each number in the list
            for j in range(i + 1, len(nums)):  # Iterate over subsequent numbers
                if nums[i] + nums[j] == target:  # Check if the sum equals the target
                    return [i, j]  # If found, return the indices
        return []  # If no solution is found, return an empty list
