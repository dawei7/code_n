"""Optimal solution for search_04: DFS on a 2D grid.

Explore reachable cells depth-first using a LIFO stack.
O(n^2) for an n x n grid.

The engine no longer ships a TrackedStack - the player
brings their own (a plain list with .append() / .pop()
gives the standard LIFO semantics; a plain list is fine
here because the engine doesn't count plain-list ops
and the budget is enforced by the grid reads / writes).
"""


def solve(grid, start, size):
    visited = set()
    stack = [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return len(visited)
