import heapq
from collections import defaultdict

def solve(n: int, edges: list[list[int]], disappear: list[int]) -> list[int]:
    adj = defaultdict(list)
    for u, v, length in edges:
        adj[u].append((v, length))
        adj[v].append((u, length))
    
    # distances[i] stores the minimum time to reach node i
    distances = [-1] * n
    distances[0] = 0
    
    # Min-heap stores (current_time, node)
    pq = [(0, 0)]
    
    while pq:
        curr_time, u = heapq.heappop(pq)
        
        # If we found a longer path already, skip
        if curr_time > distances[u] and distances[u] != -1:
            continue
            
        for v, weight in adj[u]:
            new_time = curr_time + weight
            
            # Check if the node is still available and if this path is shorter
            if new_time < disappear[v]:
                if distances[v] == -1 or new_time < distances[v]:
                    distances[v] = new_time
                    heapq.heappush(pq, (new_time, v))
                    
    return distances
