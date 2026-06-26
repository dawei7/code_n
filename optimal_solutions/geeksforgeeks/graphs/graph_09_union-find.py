"""Optimal solution for graph_09: Union-Find (DSU).

Path compression + union by rank. Process a list of union/find
ops and return the find results in order.
"""


def solve(n, ops):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1

    results = []
    for op in ops:
        if op[0] == "union":
            union(op[1], op[2])
        elif op[0] == "find":
            results.append(find(op[1]) == find(op[2]))
    return results
