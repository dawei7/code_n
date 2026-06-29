import sys
MOD = 1000000007

def solve_tree(n: int, edges: list[tuple[int, int]]) -> int:
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
    subtree = [1] * n
    answer = 0
    for node in reversed(order):
        partial = 1
        im = 1
        for child in graph[node]:
            if parent[child] == node:
                subtree[node] += subtree[child]
                im += 2 * partial * subtree[child]
                partial += subtree[child]
        answer = (answer + (node + 1) * im) % MOD
    return answer

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(str(solve_tree(n, edges)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
