import java.util.HashMap;

public class SingleNumber {
    /*
    Given a non-empty array of integers nums, 
    every element appears twice except for one. 
    Find that single one.
    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
    */
    public int singleNumber(int[] nums) {
        int res = 0;
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int i: nums) counts.put(i, counts.getOrDefault(i, 0) + 1);
        for (int k: counts.keySet()) {
            if (counts.get(k) < 2) {
                res = k;
                break;
            }
        }
        return res;
    }
}
