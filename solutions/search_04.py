"""Solution for search_04: DFS Grid.

Count all reachable cells from the top-left corner.
0 = walkable, 1 = wall. Move in 4 directions.
Use Python row/column indexing: grid[row][column].
Rows go down the screen; columns go left to right.
Return the total number of reachable cells (including start).
Requirement: O(n^2) where n = grid side length.
Source: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

Inputs passed to solve():
    grid: 2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].
    start: (row, column) start position.
    size: width and height of the square grid.

Goal:
    the number of walkable cells reachable from start (including start).

Samples:
Sample 1 input:  grid = [[0, 0], [0, 0]], start = (0, 0)
Sample 1 output: 4

Sample 2 input:  grid = [[0, 1], [1, 0]], start = (0, 0)
Sample 2 output: 1

Sample 3 input:  grid = [[0, 0, 1]], start = (0, 0)
Sample 3 output: 2

"""

def solve(grid, start, size):
    # Write your code here.
    return None
