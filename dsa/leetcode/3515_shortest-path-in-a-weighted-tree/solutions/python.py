import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(n, edges, queries):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    LOG = n.bit_length()
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n
    dist = [0] * n
    
    def dfs(u, p, d, w):
        depth[u] = d
        dist[u] = w
        up[u][0] = p
        for v, weight in adj[u]:
            if v != p:
                dfs(v, u, d + 1, w + weight)
                
    dfs(0, -1, 0, 0)
    
    for i in range(1, LOG):
        for u in range(n):
            if up[u][i-1] != -1:
                up[u][i] = up[up[u][i-1]][i-1]
                
    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if (diff >> i) & 1:
                u = up[u][i]
        
        if u == v:
            return u
        
        for i in range(LOG - 1, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        
        return up[u][0]
    
    results = []
    for u, v in queries:
        lca = get_lca(u, v)
        d = dist[u] + dist[v] - 2 * dist[lca]
        results.append(d)
        
    return results
