import heapq

class KthSmallest:
    """
    Given an n x n matrix where each of the rows and columns are sorted in ascending order, 
    return the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.
    Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
    """
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n == 1:
            return matrix[0][k-1]
        hp = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(hp, matrix[i][j])
        return heapq.nsmallest(k, hp)[-1]