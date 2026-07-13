import heapq
from collections import deque

def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return 0
    
    # Multi-source BFS to calculate distance to nearest thief
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
                
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
                
    # Dijkstra-like approach to find the path with max-min safeness
    # Max-heap stores (-safeness, r, c)
    pq = [(-dist[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while pq:
        d, r, c = heapq.heappop(pq)
        d = -d
        
        if r == n - 1 and c == n - 1:
            return d
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                # The safeness of the path is the min of current path and next cell
                new_dist = min(d, dist[nr][nc])
                heapq.heappush(pq, (-new_dist, nr, nc))
                
    return 0
