from collections import deque

def solve(n: int, queries: list[list[int]]) -> list[int]:
    # Initialize adjacency list with default linear edges i -> i+1
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[i].append(i + 1)
    
    def get_shortest_path():
        # Standard BFS to find shortest path from 0 to n-1
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            curr, dist = queue.popleft()
            if curr == n - 1:
                return dist
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1

    results = []
    for u, v in queries:
        adj[u].append(v)
        results.append(get_shortest_path())
        
    return results
