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
    seen = [False] * (n + 1)
    order = []
    sys.setrecursionlimit(1_000_000)

    def dfs(node):
        seen[node] = True
        order.append(node)
        for nxt in adj[node]:
            if not seen[nxt]:
                dfs(nxt)

    dfs(1)
    print("DFS traversal: " + " ".join(map(str, order)))


if __name__ == "__main__":
    solve()
