class GroupAnagrams:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    # O(N * KlogK) Time where K == max length of a string | O(N) Space
    def group_anagrams(self, strs):
        count = 0
        output = []
        anagrams = {}
        for i in range(len(strs)):
            current = self.get_sorted_st(strs[i])
            if current in anagrams:
                output[anagrams[current]].append(strs[i])
            else:
                output.append([strs[i]])
                anagrams[current] = count
                count += 1
        return output

    def get_sorted_st(self, st):
        st = list(st)
        st.sort()
        st = ''.join(st)
        return st