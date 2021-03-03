class Permutations:
    """
    Given an array nums of distinct integers, 
    return all the possible permutations. 
    You can return the answer in any order.
    """
    def permute(self, nums):
        n = len(nums)
        result = []
        self.heaps_algo(nums, n, result)
        return result
    
    def heaps_algo(self, arr, n, result):
        
        if n == 1:
            result.append(arr[::])
            return
        
        for i in range(n):
            self.heaps_algo(arr, n - 1, result)
            if n & 1:
                arr[0], arr[n-1] = arr[n-1], arr[0]
            else:
                arr[i], arr[n-1] = arr[n-1], arr[i]