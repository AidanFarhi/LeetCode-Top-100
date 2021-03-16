class Subsets:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    Ex)
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    """
    def sub_sets(self, arr):
        subs = [None] * len(arr)  # Maintain an array of subsets
        res = []                  # Result array 
        self.sub_sets_helper(arr, subs, res, 0)  # Make initial call here
        return res
    
    # Recursive funtion that does all the work
    def sub_sets_helper(self, arr, subs, res, i):
        if i == len(arr):  # Base case
            res.append(self.get_subset(subs))   # Add current subset to result 
        else:
            subs[i] = None   # First handle case where item is not chosen
            self.sub_sets_helper(arr, subs, res, i + 1)
            subs[i] = arr[i] # Then handle case where item IS chosen
            self.sub_sets_helper(arr, subs, res, i + 1)

    def get_subset(self, arr):
        res = []
        for item in arr:
            if item is not None:
                res.append(item)
        return res


if __name__ == '__main__':
    test = [1, 2, 3]
    Solver = Subsets()
    result = Solver.sub_sets(test)
    print(result)
