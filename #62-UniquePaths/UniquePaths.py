class UniquePaths:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?
    Example 1:
    Input: m = 3, n = 7
    Output: 28
    Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        seen = [[0]*n for _ in range(m)]
        return self.paths(0, 0, m-1, n-1, seen)
    
    def paths(self, i, j, m, n, seen):
        # Base case
        if i == m and j == n:
            return 1
        elif seen[i][j] > 0:
            return seen[i][j]
        else:
            if i < m:
                seen[i][j] += self.paths(i+1, j, m, n, seen)
            if j < n:
                seen[i][j] += self.paths(i, j+1, m, n, seen)
                
        return seen[i][j]