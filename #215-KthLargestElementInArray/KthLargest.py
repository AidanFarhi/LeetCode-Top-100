import heapq

class KthLargest:
    """
    Given an integer array nums and an integer k, 
    return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, 
    not the kth distinct element.
    """
    def find_kth_largest(self, nums, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]