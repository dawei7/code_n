import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    print("\n".join(" ".join(map(str, adj[node])) for node in range(1, n + 1)))


if __name__ == "__main__":
    solve()
