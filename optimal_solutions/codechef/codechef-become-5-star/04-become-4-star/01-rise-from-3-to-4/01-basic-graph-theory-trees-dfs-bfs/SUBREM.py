import sys

def solve_case(n: int, penalty: int, values: list[int], edges: list[tuple[int, int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    order = [0]
    for node in order:
        for nxt in graph[node]:
            if nxt != parent[node]:
                parent[nxt] = node
                order.append(nxt)
    dp = values[:]
    for node in reversed(order):
        total = values[node]
        for nxt in graph[node]:
            if parent[nxt] == node:
                total += dp[nxt]
        dp[node] = max(total, -penalty)
    return dp[0]

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, penalty = (data[idx], data[idx + 1])
        idx += 2
        values = data[idx:idx + n]
        idx += n
        edges = []
        for _ in range(n - 1):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(str(solve_case(n, penalty, values, edges)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
