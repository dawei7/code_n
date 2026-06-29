import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = (data[0], data[1])
    parent = list(range(n))
    size = [1] * n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = (find(a), find(b))
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = (rb, ra)
        parent[rb] = ra
        size[ra] += size[rb]
    idx = 2
    for _ in range(m):
        union(data[idx] - 1, data[idx + 1] - 1)
        idx += 2
    costs = data[idx:idx + n]
    best: dict[int, int] = {}
    for i, cost in enumerate(costs):
        if cost < 0:
            continue
        root = find(i)
        if root not in best or cost < best[root]:
            best[root] = cost
    roots = {find(i) for i in range(n)}
    if len(roots) == 1:
        print(0)
        return
    if len(best) != len(roots):
        print(-1)
        return
    values = list(best.values())
    print(sum(values) + (len(values) - 2) * min(values))


if __name__ == "__main__":
    solve()
