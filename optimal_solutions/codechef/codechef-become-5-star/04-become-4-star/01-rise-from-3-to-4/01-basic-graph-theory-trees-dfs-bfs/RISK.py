import sys
from collections import deque

def second_player_score(grid: list[str]) -> int:
    n = len(grid)
    m = len(grid[0])
    seen = [[False] * m for _ in range(n)]
    sizes: list[int] = []
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for r in range(n):
        for c in range(m):
            if grid[r][c] != '1' or seen[r][c]:
                continue
            seen[r][c] = True
            queue = deque([(r, c)])
            size = 0
            while queue:
                x, y = queue.popleft()
                size += 1
                for dx, dy in directions:
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < n and 0 <= ny < m and (not seen[nx][ny]) and (grid[nx][ny] == '1'):
                        seen[nx][ny] = True
                        queue.append((nx, ny))
            sizes.append(size)
    sizes.sort(reverse=True)
    return sum(sizes[1::2])

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        m = int(tokens[idx + 1])
        idx += 2
        grid = [tokens[idx + i].decode() for i in range(n)]
        idx += n
        out.append(str(second_player_score(grid)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
