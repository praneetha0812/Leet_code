class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> mp = new HashMap<>();
        int[] ans = new int[2];
        ans[0]= ans[1]=Integer.MIN_VALUE;
        for(int i=0; i<nums.length; i++){
            int a= nums[i];
            int more = target -a;
            if(mp.containsKey(more)){
                ans[0] = mp.get(more);
                ans[1] = i;
            }
            mp.put(nums[i], i);
        }
        return ans;
        
    }

}