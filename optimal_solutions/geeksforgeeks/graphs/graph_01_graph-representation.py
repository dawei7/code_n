"""Optimal solution for graph_01: Graph Representation.

Build an adjacency list from a list of edges. The graph is
undirected, so each edge (u, v) adds v to u's list and u to v's.
The input may contain duplicate edges; using a per-node set
deduplicates them in O(1) each. O(n) where n is the number of
edges.
"""


def solve(num_nodes, edges):
    graph = {i: set() for i in range(num_nodes)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return {node: sorted(neighbors) for node, neighbors in graph.items()}
