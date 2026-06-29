import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        indegree = [0] * (n + 1)
        for _ in range(m):
            _u, v = (data[idx], data[idx + 1])
            idx += 2
            indegree[v] += 1
        out.append('YES' if all((indegree[i] > 0 for i in range(1, n + 1))) else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
