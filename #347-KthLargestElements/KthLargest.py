from collections import Counter
import heapq

class KthLargest:

    def kth_largest(self, nums, k):

        if k == len(nums):
            return nums
        
        counts = Counter(nums)
        
        return heapq.nlargest(k, counts.keys(), key=counts.get)