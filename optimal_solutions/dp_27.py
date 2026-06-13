"""Optimal solution for dp_27: Floyd-Warshall Path Reconstruction.

Standard Floyd-Warshall with a next[][] matrix to
reconstruct the path. Return [] if dest is unreachable.
"""


def solve(n, edges, src, dest):
    if src == dest:
        return [src]
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    nxt = [[-1] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k] if nxt[i][k] != -1 else k
    if dist[src][dest] == INF:
        return []
    path = [src]
    cur = src
    while cur != dest:
        cur = nxt[cur][dest]
        if cur == -1:
            return []
        path.append(cur)
    return path
