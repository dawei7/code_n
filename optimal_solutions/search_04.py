"""Optimal solution for search_04: DFS on a 2D grid.

Explore reachable cells depth-first using a TrackedStack. O(n^2)
for an n x n grid.
"""


def solve(grid, start, size):
    from code_n.tracked import TrackedStack

    visited = set()
    stack = TrackedStack()
    stack.push(start)
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.push((nr, nc))
    return len(visited)
