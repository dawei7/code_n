def solve(properties: list[list[int]], k: int) -> int:
    n = len(properties)
    sets = [set(row) for row in properties]
    parent = list(range(n))

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(a: int, b: int) -> None:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    for i in range(n):
        for j in range(i + 1, n):
            if len(sets[i] & sets[j]) >= k:
                union(i, j)

    return len({find(i) for i in range(n)})
