def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    # The output matrix will have dimensions (n-2) x (n-2)
    res_size = n - 2
    res = [[0] * res_size for _ in range(res_size)]
    
    for i in range(res_size):
        for j in range(res_size):
            # Find the maximum in the 3x3 subgrid starting at (i, j)
            max_val = 0
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if grid[r][c] > max_val:
                        max_val = grid[r][c]
            res[i][j] = max_val
            
    return res
