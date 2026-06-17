"""Solution for dp_10: Unique Paths.

Count the number of distinct paths from the top-left
(0, 0) to the bottom-right (m-1, n-1) of an m x n grid,
moving only right or down. Cells with value 1 are
obstacles (cannot enter); 0 = free. The setup uses an
obstacle-free grid.
Requirement: O(m * n).
Source: https://www.geeksforgeeks.org/count-all-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

Inputs passed to solve():
    grid: 2D list-like; 0 = free, 1 = obstacle.
    m: number of rows.
    n: number of columns.

Goal:
    the number of distinct paths from (0,0) to (m-1, n-1).

Samples:
Sample 1 input:  grid = [[0,0,0],[0,0,0]], m = 2, n = 3
Sample 1 output: 3 (R-R-D, R-D-R, D-R-R)

Sample 2 input:  grid = [[0,1],[0,0]], m = 2, n = 2
Sample 2 output: 1 (only D then R)


"""

def solve(grid, m, n):
    # Write your code here.
    return None
