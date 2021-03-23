#include <iostream>
using namespace std;

/*
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise). 
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

ex) [1, 2, 3]      [7, 4, 1]
    [4, 5, 6]  ->  [8, 5, 2]
    [7, 8, 9]      [9, 6, 3]
*/

class RotateImage
{
    public:

    void rotate_image(int **matrix, int N)
    {
        transpose(matrix, N);
        reverse_each_row(matrix, N);
    }

    private:

    /* This swaps every diagonal item in matrix. Google 'transpose matrix'. */
    void transpose(int **matrix, int N)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = i; j < N; j++)
            {
                swap_matrix_items(matrix, i, j);
            }
        }
    }

    /* This reverses each row of a matrix */
    void reverse_each_row(int **matrix, int N)
    {
        for (int r = 0; r < N; r++)
        {
            int i = 0;
            int j = N - 1;
            while (i < j)
            {
                swap_row_items(matrix[r], i, j);
                ++i;
                --j;
            }
        }
    }

    /* This swaps items in a given matrix */
    void swap_matrix_items(int **matrix, int i, int j)
    {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
    }

    /* This swaps items in a given row of a matrix */
    void swap_row_items(int *row, int i, int j)
    {
        int temp = row[i];
        row[i] = row[j];
        row[j] = temp;
    }
};

void print_matrix_rows(int **matrix, int N)
{
    for (int i = 0; i < N; i++)
    {
        cout<<"[";
        for (int j = 0; j < N; j++)
        {
            if (j == N - 1)
            {
                cout<<matrix[i][j]<<"]";
                break;
            }
            cout<<matrix[i][j]<<", ";
        }
        cout<<endl;
    }
    cout<<endl;
}

int main()
{
    int **test = new int*[3];
    test[0] = new int[3];
    test[1] = new int[3];
    test[2] = new int[3];

    int num = 1;
  	for (int i = 0; i < 3; i++)
    {
      for (int j = 0; j < 3; j++)
      {
        test[i][j] = num;
        num++;
      }
    }

    cout<<"Before:"<<endl;
    print_matrix_rows(test, 3);

    RotateImage *solver = new RotateImage();
    solver->rotate_image(test, 3);

    cout<<"After:"<<endl;
    print_matrix_rows(test, 3);

    delete solver;
    delete []test;
}