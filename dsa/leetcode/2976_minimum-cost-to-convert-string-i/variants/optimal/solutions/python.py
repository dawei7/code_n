def solve(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    # Initialize distance matrix with infinity
    # There are 26 lowercase English letters
    inf = float('inf')
    dist = [[inf] * 26 for _ in range(26)]
    
    # Distance to self is 0
    for i in range(26):
        dist[i][i] = 0
        
    # Populate initial transformation costs
    for u, v, c in zip(original, changed, cost):
        u_idx = ord(u) - ord('a')
        v_idx = ord(v) - ord('a')
        dist[u_idx][v_idx] = min(dist[u_idx][v_idx], c)
        
    # Floyd-Warshall algorithm to find all-pairs shortest paths
    for k in range(26):
        for i in range(26):
            if dist[i][k] != inf:
                for j in range(26):
                    if dist[k][j] != inf:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            
    total_cost = 0
    for s, t in zip(source, target):
        s_idx = ord(s) - ord('a')
        t_idx = ord(t) - ord('a')
        
        if dist[s_idx][t_idx] == inf:
            return -1
        
        total_cost += dist[s_idx][t_idx]
        
    return total_cost
