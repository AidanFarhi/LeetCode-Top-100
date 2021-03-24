class MajorityElement:
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    """
    def majorityElement(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        counts = {}
        target = len(nums) // 2
        res = self.get_counts(nums, counts, target)
        return res

    def get_counts(self, nums, counts, target):
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
                if counts[num] > target:
                    return num
