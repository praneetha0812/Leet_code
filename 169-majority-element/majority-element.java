class Solution {
    public int majorityElement(int[] nums) {
        HashMap <Integer, Integer> hmp = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int key= nums[i];
            hmp.put(key, hmp.getOrDefault(key,0)+1);
        }
        for(Map.Entry<Integer, Integer> it : hmp.entrySet()){
            if(it.getValue()> nums.length/2){
                return it.getKey();
            }
        }
    return -1; 
    }
    
}