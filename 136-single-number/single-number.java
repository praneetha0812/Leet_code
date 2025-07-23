import java.util.HashMap;

class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int num : nums) {
            hash.put(num, hash.getOrDefault(num, 0) + 1);
        }

        for (int key : hash.keySet()) {
            if (hash.get(key) == 1) {
                return key;
            }
        }

        // Just in case, although by problem constraints, this shouldn't happen
        return -1;
    }
}
