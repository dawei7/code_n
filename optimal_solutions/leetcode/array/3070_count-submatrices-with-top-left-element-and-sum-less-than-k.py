def solve(grid: list[list[int]], k: int) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a 2D prefix sum array
    # prefix_sum[i][j] will store the sum of the submatrix from (0,0) to (i,j)
    prefix_sum = [[0] * cols for _ in range(rows)]
    count = 0
    
    for r in range(rows):
        row_running_sum = 0
        for c in range(cols):
            row_running_sum += grid[r][c]
            
            # The sum of the submatrix (0,0) to (r,c) is:
            # current row's running sum + the prefix sum of the row above
            if r == 0:
                prefix_sum[r][c] = row_running_sum
            else:
                prefix_sum[r][c] = row_running_sum + prefix_sum[r-1][c]
            
            if prefix_sum[r][c] < k:
                count += 1
            else:
                # Since all elements are non-negative, if the sum at (r,c) 
                # is >= k, any submatrix extending further will also be >= k.
                # However, we must continue to fill the prefix_sum table 
                # for future calculations.
                pass
                
    return count
