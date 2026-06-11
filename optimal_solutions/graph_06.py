"""Optimal solution for graph_06: Floyd-Warshall.

All-pairs shortest distances via the triple-loop DP.
"""


def solve(num_nodes, edges):
    INF = float("inf")
    dist = [[INF] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    return [[d if d != INF else -1 for d in row] for row in dist]
