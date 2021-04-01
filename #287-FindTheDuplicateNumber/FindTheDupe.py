class FindTheDupe:
    """
    Given an array of integers nums containing n + 1 integers, 
    where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2
    """
    # Time: O(N) | Space: O(N)
    def find_duplicate_with_set(self, nums):
        seen = set()
        for num in nums:
            if num in seen: return num
            seen.add(num)
