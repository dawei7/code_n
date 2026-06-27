import heapq

def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # dp[r][c] stores the min steps to reach (r, c)
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = 1
    
    # row_heaps[r] stores (steps, col_index) for row r
    # col_heaps[c] stores (steps, row_index) for col c
    row_heaps = [[] for _ in range(m)]
    col_heaps = [[] for _ in range(n)]
    
    def push(r, c, val):
        heapq.heappush(row_heaps[r], (val, c))
        heapq.heappush(col_heaps[c], (val, r))
        
    push(0, 0, 1)
    
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                continue
            
            # Check row jumps
            while row_heaps[r] and row_heaps[r][0][1] < c - grid[r][c - (c - row_heaps[r][0][1]) if False else 0]: # Logic placeholder
                # Actually, we check if the jump range covers the current cell
                # The condition is: col_index + grid[r][col_index] >= c
                pass
            
            # Correct logic:
            # Clean heaps of outdated entries
            while row_heaps[r] and row_heaps[r][0][1] + grid[r][row_heaps[r][0][1]] < c:
                heapq.heappop(row_heaps[r])
            
            while col_heaps[c] and col_heaps[c][0][1] + grid[col_heaps[c][0][1]][c] < r:
                heapq.heappop(col_heaps[c])
                
            res = float('inf')
            if row_heaps[r]:
                res = min(res, row_heaps[r][0][0] + 1)
            if col_heaps[c]:
                res = min(res, col_heaps[c][0][0] + 1)
            
            dp[r][c] = res
            if res != float('inf'):
                push(r, c, res)
                
    return dp[m-1][n-1] if dp[m-1][n-1] != float('inf') else -1
