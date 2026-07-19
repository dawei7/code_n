import collections

def solve(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    # Map all unique substrings to IDs
    trie = {}
    def get_id(s, create=False):
        node = trie
        for char in s:
            if char not in node:
                if not create: return -1
                node[char] = {}
            node = node[char]
        if '#' not in node:
            if not create: return -1
            node['#'] = len(ids)
            ids.append(s)
        return node['#']

    ids = []
    for s in original: get_id(s, True)
    for s in changed: get_id(s, True)
    
    n_nodes = len(ids)
    dist = [[float('inf')] * n_nodes for _ in range(n_nodes)]
    for i in range(n_nodes): dist[i][i] = 0
    
    for o, c, w in zip(original, changed, cost):
        u, v = get_id(o), get_id(c)
        dist[u][v] = min(dist[u][v], w)
        
    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n_nodes):
        for i in range(n_nodes):
            if dist[i][k] == float('inf'): continue
            for j in range(n_nodes):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    n = len(source)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # DP with Trie lookups
    for i in range(n):
        if dp[i] == float('inf'): continue
        
        # Option 1: Characters match, no cost
        if source[i] == target[i]:
            dp[i+1] = min(dp[i+1], dp[i])
            
        # Option 2: Try all possible transformations starting at i
        curr_s, curr_t = trie, trie
        for j in range(i, n):
            if source[j] not in curr_s or target[j] not in curr_t:
                break
            curr_s = curr_s[source[j]]
            curr_t = curr_t[target[j]]
            
            if '#' in curr_s and '#' in curr_t:
                u, v = curr_s['#'], curr_t['#']
                if dist[u][v] != float('inf'):
                    dp[j+1] = min(dp[j+1], dp[i] + dist[u][v])
                    
    return dp[n] if dp[n] != float('inf') else -1
