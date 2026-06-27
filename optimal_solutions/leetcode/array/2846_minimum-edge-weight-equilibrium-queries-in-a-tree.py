import collections

def solve(n, edges, queries):
    adj = collections.defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    LOG = n.bit_length()
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n
    # counts[node][weight-1] stores frequency of weight on path from root to node
    counts = [[0] * 26 for _ in range(n)]

    def dfs(u, p, d, current_counts):
        depth[u] = d
        up[u][0] = p
        counts[u] = list(current_counts)
        for v, w in adj[u]:
            if v != p:
                current_counts[w - 1] += 1
                dfs(v, u, d + 1, current_counts)
                current_counts[w - 1] -= 1

    dfs(0, -1, 0, [0] * 26)

    for i in range(1, LOG):
        for u in range(n):
            if up[u][i - 1] != -1:
                up[u][i] = up[up[u][i - 1]][i - 1]

    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in range(LOG - 1, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
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
        path_len = depth[u] + depth[v] - 2 * depth[lca]
        
        max_freq = 0
        for i in range(26):
            freq = counts[u][i] + counts[v][i] - 2 * counts[lca][i]
            if freq > max_freq:
                max_freq = freq
        
        results.append(path_len - max_freq)
        
    return results
