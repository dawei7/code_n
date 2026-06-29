import sys
from functools import cmp_to_key

def solve_case(n: int, weights: list[int], edges: list[tuple[int, int]]) -> int:
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
    zeros = [0] * n
    ones = [0] * n
    inv = [0] * n

    def compare(a: int, b: int) -> int:
        left = ones[a] * zeros[b]
        right = ones[b] * zeros[a]
        return (left > right) - (left < right)
    for node in reversed(order):
        children = [child for child in graph[node] if parent[child] == node]
        children.sort(key=cmp_to_key(compare))
        total_ones = 1 if weights[node] == 1 else 0
        total_zeros = 1 if weights[node] == 0 else 0
        current_inv = 0
        if weights[node] == 1:
            current_inv = sum((zeros[child] for child in children))
        prefix_ones = 0
        for child in children:
            current_inv += inv[child] + prefix_ones * zeros[child]
            prefix_ones += ones[child]
            total_ones += ones[child]
            total_zeros += zeros[child]
        ones[node] = total_ones
        zeros[node] = total_zeros
        inv[node] = current_inv
    return inv[0]

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
        weights = data[idx:idx + n]
        idx += n
        edges = []
        for _ in range(n - 1):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(str(solve_case(n, weights, edges)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
