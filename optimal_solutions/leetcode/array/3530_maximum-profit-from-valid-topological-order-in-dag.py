def solve(n: int, edges: list[list[int]], values: list[int]) -> int:
    """
    In a Directed Acyclic Graph (DAG), a topological sort always exists.
    Since we want to maximize the profit of a valid topological order,
    and a topological order includes all nodes in the graph, the maximum
    profit is simply the sum of all node values, provided the graph is a DAG.
    If the problem implies selecting a subset, the logic would involve
    DP on subsets, but for a standard topological order of a DAG,
    all nodes must be included.
    """
    # Build adjacency list to verify DAG property if necessary
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    
    # Kahn's algorithm to verify if it is a DAG
    queue = [i for i in range(n) if in_degree[i] == 0]
    count = 0
    while queue:
        u = queue.pop(0)
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # If count != n, it's not a DAG (though problem constraints usually guarantee it)
    if count != n:
        return 0
        
    return sum(values)
