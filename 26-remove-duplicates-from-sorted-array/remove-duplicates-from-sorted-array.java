class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0;
        int j;
        int n= nums.length;
        for(j=1; j<=n-1; j++){
           if(nums[i] !=nums[j]){
             
              i++;
              nums[i] =nums[j];
           }
        }return i+1;
    }

}