class NumBits:
    """
    Write a function that takes an unsigned integer and returns the number of '1' bits it has 
    (also known as the Hamming weight).
    Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
    Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
    """
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            # Each time, we are comparing the last bit (far right) to 1       
            #                                        v
            # ex) 1 = 00000000000000000000000000000001
            #     n = 00000000000000000000000000001011
            #                                        ^
            res += (n & 1)
            # Then, shift n to the right using >>         ->->
            # ex) Before: n = 00000000000000000000000000001011 
            #     After:  n = 00000000000000000000000000000101
            n = n >> 1
        return res