class Solution {
    public int removeElement(int[] nums, int val) {
        ArrayList <Integer> temp = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            if(nums[i] != val){
                temp.add(nums[i]);
            }
        }
        for(int i=0; i<temp.size(); i++){
            nums[i] = temp.get(i);
        }
        /*for(int i= temp.size(); i< nums.length; i++){
            nums[i]= val;
        }*/
        return temp.size();
    }
}