import heapq

def solve(grid, queries):
    m, n = len(grid), len(grid[0])
    
    # Store queries with original indices to return results in correct order
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    results = [0] * len(queries)
    
    # Min-heap stores (value, row, col)
    # We start from (0, 0)
    pq = [(grid[0][0], 0, 0)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    visited[0][0] = True
    
    count = 0
    
    for q_val, original_idx in sorted_queries:
        # Expand the frontier while the smallest value in heap is less than q_val
        while pq and pq[0][0] < q_val:
            val, r, c = heapq.heappop(pq)
            count += 1
            
            # Check 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))
        
        results[original_idx] = count
        
    return results
