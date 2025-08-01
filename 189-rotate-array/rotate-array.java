class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k%n;
        reverse(nums, 0, n-k-1);
        reverse(nums,n-k, n-1);
        reverse(nums, 0, n-1);
    }

    public static void reverse(int[] nums, int l, int r){

        while(l<r){
        int temp = nums[l];
        nums[l]= nums[r];
        nums[r] = temp;
        l++; r--;
        } 
    }
    
    
}