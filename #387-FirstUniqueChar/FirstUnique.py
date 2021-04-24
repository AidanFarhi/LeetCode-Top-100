class FirstUnique:
    """
    Given a string s, return the first non-repeating character in it and return its index. 
    If it does not exist, return -1.
    Example 1:
    Input: s = "leetcode"
    Output: 0
    """
    def firstUniqChar(self, s: str) -> int:
        """
        Take advantage of the fact that ascii codes
        for lower case chars are in the range 97-122
        """
        counts = [0] * 26
        # Get a count of all chars
        for ch in s:
            # ord() gets us the ascii code, and -97 will
            # allow us to use 0-25 indexing for the counts array.
            # ex) ord(a) == 97 ... ord(z) == 122
            #     97 - 97 = 0  ... 122 - 97 = 25
            counts[ord(ch)-97] += 1
        # Now go through the string and check if the char count == 1
        for i, ch in enumerate(s):
            if counts[ord(ch)-97] == 1:
                return i
        # If none are found
        return -1
