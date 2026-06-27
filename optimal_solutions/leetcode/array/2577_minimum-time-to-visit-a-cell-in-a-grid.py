import heapq

def solve(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # If the first step is impossible, return -1
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1
    
    # Priority Queue stores (time, row, col)
    pq = [(0, 0, 0)]
    visited = set([(0, 0)])
    
    while pq:
        time, r, c = heapq.heappop(pq)
        
        if r == m - 1 and c == n - 1:
            return time
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                wait = 0
                # If the next cell's requirement is greater than current time + 1
                if grid[nr][nc] > time + 1:
                    diff = grid[nr][nc] - (time + 1)
                    # If diff is odd, we can arrive exactly at grid[nr][nc]
                    # If diff is even, we arrive at grid[nr][nc] + 1
                    wait = diff if diff % 2 == 0 else diff + 1
                
                new_time = time + 1 + wait
                visited.add((nr, nc))
                heapq.heappush(pq, (new_time, nr, nc))
                
    return -1
