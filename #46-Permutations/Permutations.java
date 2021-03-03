import java.util.ArrayList;

public class Permutations {
    /*
    Given an array nums of distinct integers, 
    return all the possible permutations. 
    You can return the answer in any order.
    */
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        heapsAlgo(nums, n, res);
        return res;
    }
    
    public void heapsAlgo(int[] nums, int n, List<List<Integer>> res) {
        if (n == 1) {
            res.add(listToArr(nums));
            return;
        }
        
        for (int i = 0; i < n; i++) {
            heapsAlgo(nums, n - 1, res);
            if (n % 2 == 0) {
                swap(nums, 0, n - 1);
            } else {
                swap(nums, i, n - 1);
            }
        }
    }
    
    public List<Integer> listToArr(int[] arr) {
        List<Integer> l = new ArrayList<>();
        for (int i: arr) l.add(i);
        return l;
    }
    
    public void swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
}