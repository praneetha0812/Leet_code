class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
         # list to store the output
        output = []

        # Iterate through the list
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    # Add the indices of the two elements to the output list
                    output.append(i)
                    output.append(j)
                    return output  # Return the output as soon as a valid pair is found

        # empty list, when no output is found
        return output