def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    flips = 0
    ones_count = 0
    diff_pairs = 0
    
    # Process 4-cell groups
    for r in range(m // 2):
        for c in range(n // 2):
            cells = [
                grid[r][c], grid[r][n - 1 - c],
                grid[m - 1 - r][c], grid[m - 1 - r][n - 1 - c]
            ]
            s = sum(cells)
            flips += min(s, 4 - s)
            ones_count += (s if s <= 2 else 4 - s)
            
    # Process middle row if m is odd
    if m % 2 == 1:
        r = m // 2
        for c in range(n // 2):
            if grid[r][c] != grid[r][n - 1 - c]:
                flips += 1
                diff_pairs += 1
            else:
                if grid[r][c] == 1:
                    ones_count += 2
                    
    # Process middle column if n is odd
    if n % 2 == 1:
        c = n // 2
        for r in range(m // 2):
            if grid[r][c] != grid[m - 1 - r][c]:
                flips += 1
                diff_pairs += 1
            else:
                if grid[r][c] == 1:
                    ones_count += 2
                    
    # Process center cell if both are odd
    if m % 2 == 1 and n % 2 == 1:
        if grid[m // 2][n // 2] == 1:
            flips += 1
            
    # Adjust for parity of ones_count
    if ones_count % 4 != 0:
        if diff_pairs > 0:
            flips += 0
        else:
            flips += 2
            
    return flips
