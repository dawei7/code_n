import heapq

def solve(moveTime: list[list[int]]) -> int:
    rows = len(moveTime)
    cols = len(moveTime[0])
    
    # dist[r][c] stores the minimum time to reach cell (r, c)
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    
    # Priority Queue stores (current_time, r, c)
    pq = [(0, 0, 0)]
    
    while pq:
        curr_time, r, c = heapq.heappop(pq)
        
        if curr_time > dist[r][c]:
            continue
            
        if r == rows - 1 and c == cols - 1:
            return curr_time
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # The time to enter the next room is max(arrival_time, moveTime[nr][nc]) + 1
                # arrival_time is curr_time + 1
                arrival_time = curr_time + 1
                next_time = max(arrival_time, moveTime[nr][nc] + 1)
                
                if next_time < dist[nr][nc]:
                    dist[nr][nc] = next_time
                    heapq.heappush(pq, (next_time, nr, nc))
                    
    return -1
