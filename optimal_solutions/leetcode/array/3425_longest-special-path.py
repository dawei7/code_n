import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(edges, values):
    n = len(values)
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    max_len = 0
    count = 0
    
    # Maps value -> (prefix_sum, depth)
    val_map = {}
    
    def dfs(u, p, current_dist, depth, path_nodes):
        nonlocal max_len, count
        
        val = values[u]
        
        # Check if value exists in current path
        prev_dist, prev_depth = val_map.get(val, (-1, -1))
        
        # The valid start of the path is after the last occurrence of this value
        start_depth = prev_depth + 1
        
        # Calculate path length
        # We need the prefix sum at start_depth. 
        # path_nodes stores (prefix_sum, depth)
        start_dist = path_nodes[start_depth][0]
        dist = current_dist - start_dist
        
        if dist > max_len:
            max_len = dist
            count = 1
        elif dist == max_len:
            count += 1
            
        # Update state
        old_val_info = val_map.get(val)
        val_map[val] = (current_dist, depth)
        path_nodes.append((current_dist, depth))
        
        for v, w in adj[u]:
            if v != p:
                dfs(v, u, current_dist + w, depth + 1, path_nodes)
        
        # Backtrack
        path_nodes.pop()
        if old_val_info:
            val_map[val] = old_val_info
        else:
            del val_map[val]

    # path_nodes stores (prefix_sum, depth)
    dfs(0, -1, 0, 0, [(0, -1)])
    
    return [max_len, count]
