def solve(grid: list[list[int]]) -> bool:
    n = len(grid)
    # Map each step value to its (row, col) coordinate
    pos = [None] * (n * n)
    for r in range(n):
        for c in range(n):
            pos[grid[r][c]] = (r, c)
    
    # A valid tour must start at (0, 0)
    if grid[0][0] != 0:
        return False
    
    # Validate each consecutive move
    for i in range(n * n - 1):
        r1, c1 = pos[i]
        r2, c2 = pos[i + 1]
        
        dr = abs(r1 - r2)
        dc = abs(c1 - c2)
        
        # A knight move is valid if the absolute differences are {1, 2}
        # This is equivalent to checking if the product is 2 and sum is 3
        if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
            return False
            
    return True
