"""
Description
-----------
Find the shortest path from START to GOAL in a 2D grid.
0 = walkable, 1 = wall. Move in 4 directions (up/down/left/right).
The generated maze always has a route, but dense walls make guessing impossible.
Use Python row/column indexing: grid[row][column].
Rows go down the screen; columns go left to right.
Return the shortest path length in steps.
Requirement: O(n^2) where n = grid side length.
Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

Examples
--------
Example 1:
Input:  grid = [[0, 0, 0]], start = (0, 0), goal = (0, 2)
Output: 2

Example 2:
Input:  grid = [[0, 0]], start = (0, 0), goal = (0, 1)
Output: 1

Example 3:
Input:  grid = [[0, 1, 0], [0, 0, 0], [1, 1, 0]], start = (0, 0), goal = (0, 2)
Output: 4
"""

def solve(grid, start, goal, size):
    # Write your code here.
    return None
