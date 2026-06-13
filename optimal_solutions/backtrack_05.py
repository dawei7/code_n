"""Optimal solution for backtrack_05: Rat in a Maze.

Find a path from (0, 0) to (n-1, n-1) in a 0/1 maze. 1 = open.
Move 4-neighbour. Backtracking DFS.
"""


def solve(maze, n):
    if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []

    def helper(r, c):
        if r == n - 1 and c == n - 1:
            path.append((r, c))
            return True
        if r < 0 or c < 0 or r >= n or c >= n:
            return False
        if visited[r][c] or maze[r][c] == 0:
            return False
        visited[r][c] = True
        path.append((r, c))
        if helper(r + 1, c) or helper(r, c + 1):
            return True
        path.pop()
        return False

    if helper(0, 0):
        return path
    return []
