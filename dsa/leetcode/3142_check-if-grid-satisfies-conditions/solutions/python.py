def solve(grid: list[list[int]]) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            # Check vertical condition: cell must equal the one below it
            if r + 1 < rows:
                if grid[r][c] != grid[r + 1][c]:
                    return False
            
            # Check horizontal condition: cell must not equal the one to the right
            if c + 1 < cols:
                if grid[r][c] == grid[r][c + 1]:
                    return False
                    
    return True
