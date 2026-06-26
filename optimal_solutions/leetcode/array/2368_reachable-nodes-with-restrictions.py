from collections import deque, defaultdict

def solve(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Convert restricted list to a set for O(1) lookup
    restricted_set = set(restricted)
    
    # BFS traversal starting from node 0
    count = 0
    queue = deque([0])
    visited = {0}
    
    while queue:
        curr = queue.popleft()
        count += 1
        
        for neighbor in adj[curr]:
            if neighbor not in visited and neighbor not in restricted_set:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return count
