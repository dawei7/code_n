"""Optimal solution for search_03: BFS on a 2D grid.

Find the shortest path from START to GOAL by exploring the grid
level by level with a TrackedQueue. O(n^2) for an n x n grid
since every cell is visited at most once.
"""


def solve(grid, start, goal, size):
    from code_n.tracked import TrackedQueue

    frontier = TrackedQueue()
    frontier.enqueue((start[0], start[1], 0))
    visited = set()
    while frontier:
        row, col, distance = frontier.dequeue()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == goal:
            return distance
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited:
                if grid[nr][nc] == 0:
                    frontier.enqueue((nr, nc, distance + 1))
    return -1
