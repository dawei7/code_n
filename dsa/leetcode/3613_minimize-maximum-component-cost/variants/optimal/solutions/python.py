def solve(n: int, edges: list[list[int]], k: int) -> int:
    if k == n:
        return 0

    parent = list(range(n))
    size = [1] * n

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    components = n
    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            continue

        if size[root_u] < size[root_v]:
            root_u, root_v = root_v, root_u
        parent[root_v] = root_u
        size[root_u] += size[root_v]
        components -= 1

        if components == k:
            return weight

    return 0
