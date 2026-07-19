from collections import deque

def solve(grid: list[list[int]], health: int) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    
    # If the starting cell is hazardous, we lose 1 health immediately
    start_cost = grid[0][0]
    if start_cost >= health:
        return False
        
    # dist[r][c] stores the minimum health cost to reach (r, c)
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = start_cost
    
    # 0-1 BFS using a deque
    queue = deque([(0, 0)])
    
    while queue:
        r, c = queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return dist[r][c] < health
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                weight = grid[nr][nc]
                if dist[r][c] + weight < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + weight
                    # If weight is 0, add to front; if 1, add to back
                    if weight == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))
                        
    return dist[rows - 1][cols - 1] < health
