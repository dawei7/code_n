from collections import deque, defaultdict

def solve(n, edges):
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1
    
    # Kahn's algorithm to find nodes not in cycles
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    is_tree_node = [False] * n
    
    tree_node_count = 0
    while queue:
        u = queue.popleft()
        is_tree_node[u] = True
        tree_node_count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Nodes remaining with in_degree > 0 are part of cycles
    cyclic_node_count = n - tree_node_count
    
    return [cyclic_node_count, tree_node_count]
