def solve(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Build 2D prefix sum table
    # pref[i][j] stores sum of grid[0...i-1][0...j-1]
    pref = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            pref[r + 1][c + 1] = grid[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
            
    def get_sum(r1, c1, r2, c2):
        # Returns sum of rectangle from (r1, c1) to (r2, c2) inclusive
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
    
    # Iterate through all possible horizontal cuts (after row i)
    # and vertical cuts (after column j)
    # i ranges from 0 to rows-2, j ranges from 0 to cols-2
    for i in range(rows - 1):
        for j in range(cols - 1):
            sum1 = get_sum(0, 0, i, j)
            sum2 = get_sum(0, j + 1, i, cols - 1)
            sum3 = get_sum(i + 1, 0, rows - 1, j)
            sum4 = get_sum(i + 1, j + 1, rows - 1, cols - 1)
            
            if sum1 == sum2 == sum3 == sum4:
                return True
                
    return False
