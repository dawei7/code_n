import sys
from collections import deque

def min_changes_for_color(grid, n, target):
    dist = [[10 ** 9] * n for _ in range(n)]
    dq = deque()
    start_cost = 0 if grid[0][0] == target else 1
    dist[0][0] = start_cost
    dq.append((0, 0))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < n and 0 <= ny < n:
                cost = 0 if grid[nx][ny] == target else 1
                if dist[x][y] + cost < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + cost
                    if cost == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
    return dist[n - 1][n - 1]

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    index = 0
    n = int(input_data[index])
    index += 1
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[index]))
            index += 1
        grid.append(row)
    ans = min(min_changes_for_color(grid, n, 0), min_changes_for_color(grid, n, 1))
    print(ans)


if __name__ == "__main__":
    solve()
