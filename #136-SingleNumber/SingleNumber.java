import java.util.HashMap;

public class SingleNumber {
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
