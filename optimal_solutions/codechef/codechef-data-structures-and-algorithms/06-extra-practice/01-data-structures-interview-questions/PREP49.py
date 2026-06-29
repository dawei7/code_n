import sys
import math
from collections import deque
input = sys.stdin.readline

def is_valid(x, y, Nx, Ny):
    return 0 <= x <= Nx and 0 <= y <= Ny

def solve():
    t = int(input().strip())
    for _ in range(t):
        parts = input().split()
        while len(parts) < 2:
            parts += input().split()
        Nx, Ny = map(int, parts)
        M_R = input().split()
        while len(M_R) < 2:
            M_R += input().split()
        M, R = map(int, M_R)
        X_coords = list(map(int, input().split()))
        Y_coords = list(map(int, input().split()))
        R2 = R * R
        grid = [[False] * (Ny + 1) for _ in range(Nx + 1)]
        for i in range(Nx + 1):
            for j in range(Ny + 1):
                for k in range(M):
                    dx = i - X_coords[k]
                    dy = j - Y_coords[k]
                    if dx * dx + dy * dy <= R2:
                        grid[i][j] = True
                        break
        if grid[0][0] or grid[Nx][Ny]:
            print(0)
            continue
        q = deque()
        q.append((0, 0))
        visited = [[False] * (Ny + 1) for _ in range(Nx + 1)]
        visited[0][0] = True
        found = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while q:
            x, y = q.popleft()
            if x == Nx and y == Ny:
                found = True
                break
            for dx, dy in directions:
                nx, ny = (x + dx, y + dy)
                if is_valid(nx, ny, Nx, Ny) and (not visited[nx][ny]) and (not grid[nx][ny]):
                    visited[nx][ny] = True
                    q.append((nx, ny))
        print(1 if found else 0)


if __name__ == "__main__":
    solve()
