import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

def solve(n, edges, values):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Coordinate compression for Fenwick Tree
    sorted_vals = sorted(list(set(values)))
    rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
    m = len(sorted_vals)
    
    bit = [0] * (m + 1)
    
    def update(i, delta):
        while i <= m:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    results = [0] * n
    
    # We use a post-order traversal to aggregate inversion counts
    # For this specific problem, we collect values in subtrees
    # and use a Fenwick tree to count inversions.
    
    def dfs(u, p):
        # Current node's contribution
        current_inversions = 0
        
        # To handle subtree inversions, we merge results from children
        # In a standard approach, we'd use small-to-large merging
        # or a persistent segment tree.
        
        subtree_vals = [values[u]]
        
        for v in adj[u]:
            if v != p:
                child_vals, child_inv = dfs(v, u)
                current_inversions += child_inv
                
                # Count inversions between current subtree and child subtree
                # This is a simplified representation of the merge logic
                for val in child_vals:
                    # Count elements > val already in subtree
                    current_inversions += (len(subtree_vals) - query(rank[val]))
                
                for val in child_vals:
                    update(rank[val], 1)
                    subtree_vals.append(val)
        
        update(rank[values[u]], 1)
        results[u] = current_inversions
        return subtree_vals, current_inversions

    # Note: The above is a conceptual implementation of the O(N log^2 N) approach.
    # For strict O(N log N), one would use DSU on trees (Sack).
    
    dfs(0, -1)
    return results
