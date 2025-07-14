class Solution {
    public int removeDuplicates(int[] nums) {
        LinkedHashSet <Integer> set = new LinkedHashSet<>();
        for(int i=0; i<nums.length; i++){
            set.add(nums[i]);
        }
        System.out.println(set);
        int k= set.size();
        int j =0;
        for(int x: set){
            nums[j] = x;
            j++;
        } return k;
    }
}