"""Optimal solution for backtrack_06: Knight's Tour.

For a board of size n, find any sequence of knight moves that
visits every cell exactly once. Backtracking with Warnsdorff's
heuristic: at each step, prefer the move with the fewest
onward neighbours.
"""


def solve(n):
    if n <= 1:
        return [(0, 0)] if n == 1 else []
    if n < 5:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def degree(r, c):
        count = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                count += 1
        return count

    def helper(r, c, step):
        visited[r][c] = True
        path.append((r, c))
        if step == n * n:
            return True
        candidates = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                candidates.append((degree(nr, nc), nr, nc))
        candidates.sort()
        for _, nr, nc in candidates:
            if helper(nr, nc, step + 1):
                return True
        visited[r][c] = False
        path.pop()
        return False

    if helper(0, 0, 1):
        return path
    return []
