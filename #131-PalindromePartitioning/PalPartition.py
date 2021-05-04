class PalindromePartition:
    """
    Given a string s, partition s such that every substring of the partition is a palindrome. 
    Return all possible palindrome partitioning of s.
    A palindrome string is a string that reads the same backward as forward.
    Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
    Example 2:
    Input: s = "a"
    Output: [["a"]]
    """
    
    def partition(self, s):
        res = []
        current = []
        N = len(s)
        
        def helper(k):
            if k == N:
                res.append(current.copy())
            else:
                for i in range(k, N):
                    if self.isPal(s[k:i+1]):
                        current.append(s[k:i+1])
                        helper(i+1)
                        current.pop()
        
        helper(0)
        return res
        
    def isPal(self, string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True