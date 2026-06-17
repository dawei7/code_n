"""Solution for backtrack_05: Rat in a Maze.

Find a path from (0, 0) to (n-1, n-1) in a 0/1 maze
(1 = open, 0 = blocked). Move 4-neighbour (right, down,
left, up). Backtracking DFS with a visited set. The setup
carves a guaranteed path, so the answer is always non-empty.
Source: https://www.geeksforgeeks.org/rat-in-a-maze-problem-when-movement-in-all-possible-directions-is-allowed/

Inputs passed to solve():
    maze: n x n maze; 1 = open, 0 = blocked.
    n: maze dimension (capped at 4 in the setup).

Goal:
    a path as a list of (row, col) tuples, or [] if no path.

Samples:
Sample 1 input:  maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]], n = 4
Sample 1 output: [(0,0), (1,0), (1,1), (2,1), (3,1), (3,2), (3,3)] (or similar)


"""

def solve(maze, n):
    # Write your code here.
    return None
