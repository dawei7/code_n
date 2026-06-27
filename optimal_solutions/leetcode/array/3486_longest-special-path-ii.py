import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(edges, values):
    n = len(values)
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # last_pos[val] stores the depth of the most recent node with value 'val'
    # prefix_dist[depth] stores the distance from root to node at 'depth'
    # node_val_at_depth[depth] stores the value of the node at 'depth'
    last_pos = {}
    prefix_dist = [0] * (n + 1)
    node_val_at_depth = [0] * (n + 1)
    
    max_len = 0
    count = 0
    
    def dfs(u, p, depth, current_dist, start_depth):
        nonlocal max_len, count
        
        val = values[u]
        prev_depth = last_pos.get(val, -1)
        
        # Update the start_depth of the current valid path
        new_start_depth = start_depth
        if prev_depth >= start_depth:
            new_start_depth = prev_depth + 1
            
        # Calculate path length from the valid start
        path_len = current_dist - prefix_dist[new_start_depth]
        
        if path_len > max_len:
            max_len = path_len
            count = 1
        elif path_len == max_len:
            count += 1
            
        # Recurse
        last_pos[val] = depth
        node_val_at_depth[depth] = val
        
        for v, w in adj[u]:
            if v != p:
                prefix_dist[depth + 1] = current_dist + w
                dfs(v, u, depth + 1, current_dist + w, new_start_depth)
        
        # Backtrack
        if prev_depth == -1:
            del last_pos[val]
        else:
            last_pos[val] = prev_depth

    dfs(0, -1, 0, 0, 0)
    return [max_len, count]
