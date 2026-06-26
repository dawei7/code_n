"""
Description
-----------
Shortest path on a 2D grid with 4-neighbour moves. The
expansion order is driven by a priority queue keyed on
f = g + h, where g is the cost-so-far and h is the
Manhattan-distance heuristic from the current cell to the
goal. With an admissible heuristic, A* finds an optimal
path in (typically) far fewer expansions than BFS.
Return the shortest path length in steps, or -1 if no path.
Source: https://www.geeksforgeeks.org/a-search-algorithm/

Examples
--------
Example 1:
Input:  grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], start = (0, 0), goal = (2, 2), size = 3
Output: 4

Example 2:
Input:  grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]], start = (0, 0), goal = (2, 2), size = 3
Output: 4
"""

def solve(grid, start, goal, size):
    # Write your code here.
    return None
