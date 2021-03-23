class RotateImage:
    """
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise). 
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.

    ex) [1, 2, 3]      [7, 4, 1]
        [4, 5, 6]  ->  [8, 5, 2]
        [7, 8, 9]      [9, 6, 3]
    """
    def rotate(self, matrix):
        self.transpose(matrix)
        self.reverse_each_row(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    def reverse_each_row(self, matrix):
        for row in matrix:
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
