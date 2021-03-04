class SingleNumber:
    """
    Given a non-empty array of integers nums, 
    every element appears twice except for one. 
    Find that single one.
    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
    """
    def singleNumber(self, nums):
        
        counts = {}
        
        for num in nums:
            n = str(num)
            if counts.get(n) is None:
                counts[n] = 1
            else:
                counts[n] += 1
                
        for key, val in counts.items():
            if val < 2:
                return int(key)