from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    
    ones_row = [0] * m
    ones_col = [0] * n
    
    # Precompute the number of ones in each row and column
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                ones_row[r] += 1
                ones_col[c] += 1
                
    # Construct the difference matrix
    diff = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            diff[r][c] = 2 * ones_row[r] + 2 * ones_col[c] - m - n
            
    return diff
