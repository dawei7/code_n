import sys
from collections import deque


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    directions = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        grid = []
        best = 0
        for _row in range(n):
            row = data[idx:idx + m]
            idx += m
            best = max(best, max(row))
            grid.append(row)

        visited = [[False] * m for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == best:
                    visited[i][j] = True
                    queue.append((i, j, 0))

        ans = 0
        while queue:
            x, y, d = queue.popleft()
            ans = max(ans, d)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
