import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    idx = 2
    edges = []
    for _ in range(m):
        u, v, w = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        edges.append((w, u, v))

    parent = list(range(n))
    size = [1] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    tree = [[] for _ in range(n)]
    for w, u, v in sorted(edges, reverse=True):
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        tree[u].append((v, w))
        tree[v].append((u, w))

    lines: list[str] = []
    for source in range(n):
        values = [0] * n
        stack = [(source, -1, 10**18)]
        while stack:
            node, par, best = stack.pop()
            values[node] = 0 if node == source else best
            for nxt, weight in tree[node]:
                if nxt != par:
                    stack.append((nxt, node, min(best, weight)))
        lines.append(" ".join(map(str, values)))

    sys.stdout.write("\n".join(lines))


if __name__ == "__main__":
    main()
