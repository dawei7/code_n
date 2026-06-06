"""Optimal solution for search_03: BFS on a 2D grid.

Find the shortest path from START to GOAL by exploring the grid
level by level with a FIFO queue. O(n^2) for an n x n grid
since every cell is visited at most once.

The engine no longer ships a TrackedQueue - the player
brings their own (collections.deque is the obvious choice;
a plain list with pop(0) is O(n) per pop and would push
the total to O(n^3), which still passes the O(n^2) budget
because the engine doesn't count plain-list ops).
"""


def solve(grid, start, goal, size):
    from collections import deque

    frontier = deque()
    frontier.append((start[0], start[1], 0))
    visited = set()
    while frontier:
        row, col, distance = frontier.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    frontier.append((nr, nc, distance + 1))
    return -1
