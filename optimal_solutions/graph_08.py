"""Optimal solution for graph_08: Kruskal's MST.

Greedy edge-by-edge union with DSU. Returns sorted MST edges or
[] if the graph is not connected.
"""


def solve(num_nodes, edges):
    parent = list(range(num_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
        return True

    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
