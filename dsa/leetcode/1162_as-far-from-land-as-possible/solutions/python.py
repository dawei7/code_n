from collections import deque


def solve(grid):
    n = len(grid)
    queue = deque()
    seen = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                queue.append((r, c, 0))
                seen[r][c] = True

    if not queue or len(queue) == n * n:
        return -1

    answer = 0
    while queue:
        r, c, distance = queue.popleft()
        answer = max(answer, distance)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                seen[nr][nc] = True
                queue.append((nr, nc, distance + 1))
    return answer
