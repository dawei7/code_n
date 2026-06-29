import sys


def articulation_count(n: int, edges: list[tuple[int, int]]) -> int:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    tin = [-1] * n
    low = [0] * n
    timer = 0
    cut = [False] * n
    sys.setrecursionlimit(max(1_000_000, 3 * n + 10))

    def dfs(node: int, parent: int) -> None:
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        children = 0
        for nxt in graph[node]:
            if nxt == parent:
                continue
            if tin[nxt] != -1:
                low[node] = min(low[node], tin[nxt])
            else:
                dfs(nxt, node)
                low[node] = min(low[node], low[nxt])
                if parent != -1 and low[nxt] >= tin[node]:
                    cut[node] = True
                children += 1
        if parent == -1 and children > 1:
            cut[node] = True

    dfs(0, -1)
    return sum(cut)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, m, cost = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        edges = []
        for _ in range(m):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        out.append(str(articulation_count(n, edges) * cost))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
