def solve():
    import sys
    sys.setrecursionlimit(10 ** 6)
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = [list(data[index + i]) for i in range(n)]
        index += n
        visited = [[False] * n for _ in range(n)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 'O' and (not visited[i][j]):
                    stack = [(i, j)]
                    component = []
                    boundary_touch = False
                    while stack:
                        x, y = stack.pop()
                        if visited[x][y]:
                            continue
                        visited[x][y] = True
                        component.append((x, y))
                        if x == 0 or x == n - 1 or y == 0 or (y == n - 1):
                            boundary_touch = True
                        for dx, dy in dirs:
                            nx, ny = (x + dx, y + dy)
                            if 0 <= nx < n and 0 <= ny < n:
                                if matrix[nx][ny] == 'O' and (not visited[nx][ny]):
                                    stack.append((nx, ny))
                    if not boundary_touch:
                        for x, y in component:
                            matrix[x][y] = 'X'
        for row in matrix:
            output_lines.append(''.join(row))
    sys.stdout.write('\n'.join(output_lines))


if __name__ == "__main__":
    solve()
