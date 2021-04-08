class Solution:
    
    def roman_to_int_MY_VERSION(self, s: str) -> int:
        val_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i = 0
        N = len(s)
        res = 0
        while i < N:
            ch = s[i]
            # Check if we are at the end of the string
            if i < N-1 or (i == 0 and N == 2):
                # Handle 3 cases
                if ch == "I":
                    if s[i+1] == "V":
                        res += 4
                        i += 2
                    elif s[i+1] == "X":
                        res += 9
                        i += 2
                    else:
                        res += 1
                        i += 1
                elif ch == "X":
                    if s[i+1] == "L":
                        res += 40
                        i += 2
                    elif s[i+1] == "C":
                        res += 90
                        i += 2
                    else:
                        res += 10
                        i += 1
                elif ch == "C":
                    if s[i+1] == "D":
                        res += 400
                        i += 2
                    elif s[i+1] == "M":
                        res += 900
                        i += 2
                    else:
                        res += 100
                        i += 1
                else:
                    res += val_map[ch]
                    i += 1
            else:
                res += val_map[ch]
                i += 1
        return res

    def roman_to_int_LEETCODE_VERSION(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total