class ReverseString:
    """
    Write a function that reverses a string. 
    The input string is given as an array of characters s.
    Do not allocate extra space for another array, 
    you must do this by modifying the input array in-place with O(1) extra memory.
    You may assume all the characters consist of printable ascii characters.
    """
    def reverseString(self, s):
        i = 0           # pointer to front of arr
        j = len(s) - 1  # pointer to end of arr
        while i < j:    # end the algorithm when pointers cross
            s[i], s[j] = s[j], s[i]  # pythonic swap of elements
            i += 1                   # move i > in arr
            j -= 1                   # move j < in arr