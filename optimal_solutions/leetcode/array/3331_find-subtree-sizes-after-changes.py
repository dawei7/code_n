import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(parent, s):
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        adj[parent[i]].append(i)
    
    new_parent = list(parent)
    # Track the most recent ancestor for each character 'a'-'z'
    last_seen = [-1] * 26
    
    def find_new_parents(u, p_map):
        char_idx = ord(s[u]) - ord('a')
        old_p = p_map[char_idx]
        
        if old_p != -1:
            new_parent[u] = old_p
            
        # Save state to backtrack
        prev_val = p_map[char_idx]
        p_map[char_idx] = u
        
        for v in adj[u]:
            find_new_parents(v, p_map)
            
        # Restore state
        p_map[char_idx] = prev_val

    find_new_parents(0, last_seen)
    
    # Build new adjacency list based on updated parents
    new_adj = [[] for _ in range(n)]
    for i in range(1, n):
        new_adj[new_parent[i]].append(i)
        
    subtree_sizes = [0] * n
    
    def compute_sizes(u):
        size = 1
        for v in new_adj[u]:
            size += compute_sizes(v)
        subtree_sizes[u] = size
        return size
        
    compute_sizes(0)
    return subtree_sizes
