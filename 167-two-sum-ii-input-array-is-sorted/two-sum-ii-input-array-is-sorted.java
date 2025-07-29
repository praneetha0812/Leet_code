class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                // Return 1-based indices
                return new int[] { left + 1, right + 1 };
            } else if (sum < target) {
                left++;  // Increase the sum
            } else {
                right--; // Decrease the sum
            }
        }

        return new int[] {};  // Per constraints, this won't be reached
    }
}
