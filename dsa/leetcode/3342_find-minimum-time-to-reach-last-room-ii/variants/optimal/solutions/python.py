import heapq

def solve(moveTime: list[list[int]]) -> int:
    rows = len(moveTime)
    cols = len(moveTime[0])
    
    # dist[r][c][parity] stores the min time to reach (r, c) 
    # where parity is (steps_taken % 2)
    # parity 0: next move adds 1, parity 1: next move adds 2
    dist = {}
    
    # Priority Queue stores (current_time, r, c, parity)
    pq = [(0, 0, 0, 0)]
    dist[(0, 0, 0)] = 0
    
    while pq:
        curr_time, r, c, parity = heapq.heappop(pq)
        
        if curr_time > dist.get((r, c, parity), float('inf')):
            continue
            
        if r == rows - 1 and c == cols - 1:
            return curr_time
            
        # Determine the time increment based on parity
        # parity 0 -> next move adds 1, parity 1 -> next move adds 2
        increment = 1 if parity == 0 else 2
        next_parity = 1 - parity
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # The time to enter the next cell is max(moveTime[nr][nc], curr_time) + increment
                arrival_time = max(moveTime[nr][nc], curr_time) + increment
                
                if arrival_time < dist.get((nr, nc, next_parity), float('inf')):
                    dist[(nr, nc, next_parity)] = arrival_time
                    heapq.heappush(pq, (arrival_time, nr, nc, next_parity))
                    
    return -1
