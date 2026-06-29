import sys
from collections import defaultdict, deque

def dfs(node, parent, depth, dist, adj):
    dist[node] = depth
    for v in adj[node]:
        if v != parent:
            dfs(v, node, depth + 1, dist, adj)

def solve():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    edges = list(map(int, data[1:]))
    adj = defaultdict(list)
    dist = [-1] * (n + 1)
    for i in range(0, len(edges), 2):
        x = edges[i]
        y = edges[i + 1]
        adj[x].append(y)
        adj[y].append(x)
    dfs(1, -1, 0, dist, adj)
    start_node = 1
    max_dist = -1
    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            start_node = i
    dist = [-1] * (n + 1)
    dfs(start_node, -1, 0, dist, adj)
    max_dist = max(dist[1:])
    print(max_dist)


if __name__ == "__main__":
    solve()
