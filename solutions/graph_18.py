"""Solution for graph_18: A* Search.

Shortest path on a 2D grid with 4-neighbour moves. The
expansion order is driven by a priority queue keyed on
``f = g + h``, where g is the cost-so-far and h is the
Manhattan-distance heuristic from the current cell to the
goal. With an admissible heuristic, A* finds an optimal
path in (typically) far fewer expansions than BFS.
Return the shortest path length in steps, or -1 if no path.
Source: https://www.geeksforgeeks.org/a-search-algorithm/

Inputs passed to solve():
    grid: 2D list-like. 0 = walkable, 1 = wall. Read with grid[row][column].
    start: (row, column) start position.
    goal: (row, column) goal position.
    size: width and height of the square grid.

Goal:
    the length of the shortest path from start to goal in steps, or -1.

Samples:
Sample 1 input:  grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], start = (0, 0), goal = (2, 2), size = 3
Sample 1 output: 4

Sample 2 input:  grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]], start = (0, 0), goal = (2, 2), size = 3
Sample 2 output: 4


"""

def solve(grid, start, goal, size):
    # Write your code here.
    return None
