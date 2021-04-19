class PascalsTriangle:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    """
    def generate(self, numRows):
        if numRows == 1: return [[1]]
        output = [[1]]
        self.helper(output, [1], 1, numRows)
        return output
    
    def helper(self, output, parents, level, numRows):
        if level == numRows: 
            return
        else:
            next_gen = parents[::]
            next_gen.append(1)
            for i in range(level):
                if i != 0 and i < level:
                    next_gen[i] = parents[i-1] + parents[i]
            output.append(next_gen[::])
            self.helper(output, next_gen, level+1, numRows)