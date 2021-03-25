class ValidAnagram:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    """
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        N = len(s)
        s_count = [0] * 26
        t_count = [0] * 26
        key = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(N):
            s_count[key.index(s[i])] += 1
            t_count[key.index(t[i])] += 1 
        for i in range(26):
            if s_count[i] != t_count[i]: return False
        return True