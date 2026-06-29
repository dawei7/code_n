import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = (data[0], data[1])
    matrix = [[0] * n for _ in range(n)]
    idx = 2
    for _ in range(m):
        u, v = (data[idx] - 1, data[idx + 1] - 1)
        idx += 2
        matrix[u][v] = 1
        matrix[v][u] = 1
    print('\n'.join((' '.join(map(str, row)) for row in matrix)))


if __name__ == "__main__":
    solve()
