public class RotateImage {
    /*
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise). 
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.

    ex) [1, 2, 3]      [7, 4, 1]
        [4, 5, 6]  ->  [8, 5, 2]
        [7, 8, 9]      [9, 6, 3]
    */
    public static void rotateImage(int[][] matrix) {
        transpose(matrix);
        reverseEachRow(matrix);
    }

    public static void transpose(int[][] matrix) {
        int N = matrix.length;
        for (int i = 0; i < N; i++) {
            for (int j = i; j < N; j++) {
                swapMatrixItems(matrix, i, j);
            }
        }
    }

    public static void reverseEachRow(int[][] matrix) {
        for (int[] row : matrix){
            int i = 0;
            int j = matrix.length - 1;
            while (i < j) {
                swapRowItems(row, i, j);
                ++i;
                --j;
            }
        }
    }

    public static void swapMatrixItems(int[][] matrix, int i, int j) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
    }

    public static void swapRowItems(int[] row, int i, int j) {
        int temp = row[i];
        row[i] = row[j];
        row[j] = temp;
    }
}