import sys
from functools import lru_cache

def solve(grid: list[list[int]]) -> int:
    MOD = 10**9 + 7
    m = len(grid)
    n = len(grid[0])

    # Directions for moving up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @lru_cache(None)
    def dfs(r: int, c: int) -> int:
        # A path consisting only of the current cell is 1 path
        count = 1

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check boundary conditions
            if 0 <= nr < m and 0 <= nc < n:
                # Check strictly increasing condition
                if grid[nr][nc] > grid[r][c]:
                    count = (count + dfs(nr, nc)) % MOD
        
        return count

    total_paths = 0
    # Iterate through each cell and sum up the paths starting from it
    for r in range(m):
        for c in range(n):
            total_paths = (total_paths + dfs(r, c)) % MOD
            
    return total_paths
