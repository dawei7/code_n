def solve(grid: list[list[int]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    def dfs(r, c):
        if r == m - 1 and c == n - 1:
            return True
        
        grid[r][c] = 0
        
        # Try moving down or right
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < m and nc < n and grid[nr][nc] == 1:
                if dfs(nr, nc):
                    return True
        return False

    # First pass: check if a path exists and remove it
    # We don't want to remove the start (0,0) or end (m-1, n-1)
    # So we temporarily set them back to 1 if they were flipped
    has_path1 = dfs(0, 0)
    
    if not has_path1:
        return True
    
    grid[0][0] = 1
    grid[m - 1][n - 1] = 1
    
    # Second pass: check if another path exists
    has_path2 = dfs(0, 0)
    
    return not has_path2
