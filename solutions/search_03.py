"""Solution for search_03: BFS Grid.

Find the shortest path from START to GOAL in a 2D grid.
0 = walkable, 1 = wall. Move in 4 directions (up/down/left/right).
The generated maze always has a route, but dense walls make guessing impossible.
Use Python row/column indexing: grid[row][column].
Rows go down the screen; columns go left to right.
Return the shortest path length in steps.
Requirement: O(n^2) where n = grid side length.
Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

Inputs passed to solve():
    grid: 2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].
    start: (row, column) start position.
    goal: (row, column) goal position.
    size: width and height of the square grid.

Goal:
    the length of the shortest path from start to goal in steps. The challenge always has a path.

Samples:
Sample 1 input:  grid = [[0, 0, 0]], start = (0, 0), goal = (0, 2)
Sample 1 output: 2

Sample 2 input:  grid = [[0, 0]], start = (0, 0), goal = (0, 1)
Sample 2 output: 1

Sample 3 input:  grid = [[0, 1, 0], [0, 0, 0], [1, 1, 0]], start = (0, 0), goal = (0, 2)
Sample 3 output: 4

"""

def solve(grid, start, goal, size):
    # Write your code here.
    return None
