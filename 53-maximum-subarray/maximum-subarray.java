class Solution {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int sum = 0;
        int start = 0;
        int ansStart = 0, ansEnd = 0;

        for (int i = 0; i < nums.length; i++) {
            if (sum == 0) {
                start = i;
            }

            sum += nums[i];

            if (sum > max) {
                max = sum;
                ansStart = start;
                ansEnd = i;
            }

            if (sum < 0) {
                sum = 0;
            }
        }

      
        System.out.println("Subarray: " + Arrays.toString(Arrays.copyOfRange(nums, ansStart, ansEnd + 1)));

        return max;
    }
}
