class MajorityElement:
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    """

    # This solution is: Time O(N) | Space O(N)
    def majority_element_with_hashmap(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        counts = {}
        target = len(nums) // 2
        res = self.get_counts(nums, counts, target)
        return res

    def get_counts(self, nums, counts, target):
        for num in nums:
            if num not in counts: counts[num] = 1
            else:
                counts[num] += 1
                if counts[num] > target: return num

    # This solution is: Time O(N) | Space O(1)
    def majority_element_boyer_moore(self, nums):
        if len(nums) == 1: return nums[0]
        candidate = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate: counter += 1
            elif nums[i] != candidate and counter > 0: counter -= 1
            else:
                candidate = nums[i]
                counter = 1
        
