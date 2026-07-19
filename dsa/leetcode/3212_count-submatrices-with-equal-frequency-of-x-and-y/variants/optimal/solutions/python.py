from typing import List

def solve(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    # prefix_x[i][j] stores count of 'X' in grid[0...i-1][0...j-1]
    # prefix_y[i][j] stores count of 'Y' in grid[0...i-1][0...j-1]
    prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
    prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            # Calculate prefix sums using inclusion-exclusion principle
            val_x = 1 if grid[i][j] == 'X' else 0
            val_y = 1 if grid[i][j] == 'Y' else 0
            
            prefix_x[i+1][j+1] = (prefix_x[i][j+1] + prefix_x[i+1][j] - 
                                  prefix_x[i][j] + val_x)
            prefix_y[i+1][j+1] = (prefix_y[i][j+1] + prefix_y[i+1][j] - 
                                  prefix_y[i][j] + val_y)
            
            # Check condition: count of X == count of Y and count of X > 0
            if prefix_x[i+1][j+1] == prefix_y[i+1][j+1] and prefix_x[i+1][j+1] > 0:
                count += 1
                
    return count
