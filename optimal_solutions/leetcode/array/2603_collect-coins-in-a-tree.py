from collections import deque

def solve(coins: list[int], edges: list[list[int]]) -> int:
    n = len(coins)
    if n <= 1:
        return 0
    
    adj = [set() for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        degree[u] += 1
        degree[v] += 1
        
    # First pass: remove all leaf nodes that do not have coins
    queue = deque()
    for i in range(n):
        if degree[i] == 1 and coins[i] == 0:
            queue.append(i)
            
    removed_count = 0
    while queue:
        u = queue.popleft()
        removed_count += 1
        for v in adj[u]:
            adj[v].remove(u)
            degree[v] -= 1
            if degree[v] == 1 and coins[v] == 0:
                queue.append(v)
                
    # Second and third pass: remove nodes at distance 1 and 2 from coins
    # This effectively prunes the tree to the minimal subtree containing all coins
    for _ in range(2):
        leaves = [i for i in range(n) if degree[i] == 1]
        for u in leaves:
            removed_count += 1
            for v in adj[u]:
                adj[v].remove(u)
                degree[v] -= 1
                
    remaining_edges = (n - removed_count - 1)
    return max(0, remaining_edges * 2)
