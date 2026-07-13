def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    
    found = False
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                found = True
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
                
    if not found:
        return 0
        
    return (max_r - min_r + 1) * (max_c - min_c + 1)
