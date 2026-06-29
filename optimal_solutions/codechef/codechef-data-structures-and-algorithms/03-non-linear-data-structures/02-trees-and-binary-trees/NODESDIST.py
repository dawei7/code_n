import sys
from collections import defaultdict, deque
import math
N = 100001
LG = 17
adj = defaultdict(list)
level = [0] * N
ancestors = [[-1] * LG for _ in range(N)]
n = 0

def dfs(node, parent, lvl):
    level[node] = lvl
    ancestors[node][0] = parent
    for child in adj[node]:
        if child != parent:
            dfs(child, node, lvl + 1)

def preprocess():
    for j in range(1, LG):
        for node in range(1, n + 1):
            ancestor = ancestors[node][j - 1]
            if ancestor == -1:
                ancestors[node][j] = -1
            else:
                ancestors[node][j] = ancestors[ancestor][j - 1]

def lca(u, v):
    if level[u] < level[v]:
        u, v = (v, u)
    diff = level[u] - level[v]
    for j in range(LG):
        if diff >> j & 1:
            u = ancestors[u][j]
    if u == v:
        return u
    for j in range(LG - 1, -1, -1):
        if ancestors[u][j] != -1 and ancestors[u][j] != ancestors[v][j]:
            u = ancestors[u][j]
            v = ancestors[v][j]
    return ancestors[u][0]

def get_distance(u, v):
    lca_of_uv = lca(u, v)
    return level[u] + level[v] - 2 * level[lca_of_uv]

def solve():
    input = sys.stdin.read
    data = input().split()
    global n
    index = 0
    n = int(data[index])
    index += 1
    u = int(data[index])
    index += 1
    v = int(data[index])
    index += 1
    for _ in range(n - 1):
        ui = int(data[index])
        index += 1
        vi = int(data[index])
        index += 1
        adj[ui].append(vi)
        adj[vi].append(ui)
    dfs(1, -1, 0)
    preprocess()
    print(get_distance(u, v))


if __name__ == "__main__":
    solve()
