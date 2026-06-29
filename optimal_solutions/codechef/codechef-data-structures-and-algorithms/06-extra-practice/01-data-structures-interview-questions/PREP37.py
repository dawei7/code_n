import sys
from collections import deque
input = sys.stdin.readline

def bfs(matrix, starts, n, m):
    reachable = [[False] * m for _ in range(n)]
    q = deque(starts)
    for i, j in starts:
        reachable[i][j] = True
    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = (i + di, j + dj)
            if 0 <= ni < n and 0 <= nj < m and (not reachable[ni][nj]):
                if matrix[ni][nj] >= matrix[i][j]:
                    reachable[ni][nj] = True
                    q.append((ni, nj))
    return reachable

def solve():
    t = int(input())
    for _ in range(t):
        line = input().strip()
        while line == '':
            line = input().strip()
        n, m = map(int, line.split())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        blue_starts = []
        for i in range(n):
            blue_starts.append((i, 0))
        for j in range(m):
            blue_starts.append((0, j))
        red_starts = []
        for i in range(n):
            red_starts.append((i, m - 1))
        for j in range(m):
            red_starts.append((n - 1, j))
        blue_reachable = bfs(matrix, blue_starts, n, m)
        red_reachable = bfs(matrix, red_starts, n, m)
        count = 0
        for i in range(n):
            for j in range(m):
                if blue_reachable[i][j] and red_reachable[i][j]:
                    count += 1
        sys.stdout.write(str(count) + '\n')


if __name__ == "__main__":
    solve()
