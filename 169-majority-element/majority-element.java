class Solution {
    public int majorityElement(int[] nums) {
        int n= nums.length;
        int el =0;
        int count =0;
        for(int i=0; i<n; i++){
            if(count==0){
                count =1;
                el = nums[i];
            }
            else if(el == nums[i]) count ++;
            else count--;
        }
        int coun2= 0;
        for(int i=0; i<n; i++){
            if(nums[i] == el) coun2++;
        }
        if(coun2> n/2) return el;
        else return -1;
        
    }
}