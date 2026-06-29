import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    all_out = []
    for _ in range(t):
        n, k, root = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        special = [0] * (n + 1)
        for node in data[idx:idx + k]:
            special[node] = 1
        idx += k
        graph = [[] for _ in range(n + 1)]
        for _edge in range(n - 1):
            u, v = (data[idx], data[idx + 1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        parent = [0] * (n + 1)
        depth = [0] * (n + 1)
        order = [root]
        parent[root] = -1
        for node in order:
            for nxt in graph[node]:
                if nxt == parent[node]:
                    continue
                parent[nxt] = node
                depth[nxt] = depth[node] + 1
                order.append(nxt)
        has = special[:]
        spnode = [0] * (n + 1)
        for node in reversed(order):
            if special[node]:
                spnode[node] = node
            for nxt in graph[node]:
                if parent[nxt] == node and has[nxt]:
                    has[node] = 1
                    if not spnode[node]:
                        spnode[node] = spnode[nxt]
        closest = [0] * (n + 1)
        closest[root] = root if has[root] else 0
        for node in order:
            if node != root:
                closest[node] = node if has[node] else closest[parent[node]]
        values = []
        witnesses = []
        for node in range(1, n + 1):
            c = closest[node]
            values.append(str(2 * depth[c] - depth[node]))
            witnesses.append(str(spnode[c]))
        all_out.append(' '.join(values))
        all_out.append(' '.join(witnesses))
    sys.stdout.write('\n'.join(all_out))


if __name__ == "__main__":
    solve()
