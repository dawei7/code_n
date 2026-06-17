"""Solution for heap_06: Kth Smallest in Sorted Matrix.

A matrix where every row and every column is sorted
(row-major with sorted columns). Return the kth smallest
element. Min-heap of (value, row, col) starting at [0][0];
pop k times, pushing each cell's right + down neighbours.
O(k log k) per insertion.
Source: https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/

Inputs passed to solve():
    matrix: n x n matrix (rows and columns sorted).
    n: matrix dimension.
    k: 1-indexed kth smallest.

Goal:
    the kth smallest element in the matrix.

Samples:
Sample 1 input:  matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], n = 3, k = 8
Sample 1 output: 13


"""

def solve(matrix, n, k):
    # Write your code here.
    return None
