class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Create a dictionary to store the elements and their indices
        num_indices = {}

        # Traverse the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            # If the complement exists in the dictionary, return the indices
            if complement in num_indices:
                return [num_indices[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_indices[num] = i

        # If no solution is found
        return None