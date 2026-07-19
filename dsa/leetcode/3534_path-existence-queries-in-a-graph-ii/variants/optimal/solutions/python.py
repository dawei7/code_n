from collections import defaultdict

def solve(n, edges, queries):
    """
    Solves the path existence query problem by tracking reachable bitwise AND values.
    Since the AND operation is non-increasing, we can maintain a set of possible
    AND values for each node.
    """
    # adj[u] stores list of (v, weight)
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
    
    # reachable[u] stores a set of all possible bitwise AND values 
    # achievable from node u to any other node.
    # Given the constraints and the nature of bitwise AND, 
    # the number of distinct AND values is limited (at most 31 per node).
    reachable = [set() for _ in range(n)]
    
    # We use a worklist approach to propagate reachable AND values
    # For each node, we track the set of AND values of paths starting from it.
    # To optimize, we process nodes in reverse topological order or via BFS.
    # Since it's a general graph, we use a fixed-point iteration.
    
    # Initialize: a node can reach itself with an AND value of "all ones" (identity)
    # However, the problem implies paths of length >= 1.
    # We initialize based on outgoing edges.
    for u in range(n):
        for v, w in adj[u]:
            reachable[u].add(w)
            # Propagate existing reachable values from v
            for val in reachable[v]:
                reachable[u].add(w & val)
    
    # Iterative update until convergence
    changed = True
    while changed:
        changed = False
        for u in range(n):
            for v, w in adj[u]:
                old_len = len(reachable[u])
                reachable[u].add(w)
                for val in reachable[v]:
                    reachable[u].add(w & val)
                if len(reachable[u]) > old_len:
                    changed = True
                    
    results = []
    for start, end, target in queries:
        if start == end:
            # Depending on problem definition, path of length 0 might be allowed.
            # Assuming path must contain at least one edge based on typical constraints.
            results.append(False)
        else:
            results.append(target in reachable[start])
            
    return results
