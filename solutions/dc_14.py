"""Solution for dc_14: Staircase Search in Sorted 2D Matrix.


            Given an n x m matrix where each row and each
            column is sorted in ascending order, return True
            iff `target` is present. Staircase algorithm: start
            at the top-right corner. If cell > target, move
            left; if cell < target, move down. Each step
            eliminates a row or a column, so O(n + m) total.
            Source: https://www.geeksforgeeks.org/dsa/search-in-a-row-wise-and-column-wise-sorted-2d-array-using-divide-and-conquer-algorithm/
            

Inputs passed to solve():
    matrix: n x m matrix, rows and columns sorted ascending (small in tests).
    n: row count.
    m: column count.
    target: the value to look for.

Goal:
    True iff target appears in matrix.

Samples:
Sample 1 input:  matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 5
Sample 1 output: True

Sample 2 input:  matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], n=3, m=4, target = 100
Sample 2 output: False


"""

def solve(matrix, n, m, target):
    # Write your code here.
    return None
