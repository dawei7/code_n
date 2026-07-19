def solve(grid: list[list[int]], threshold: int) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])
    
    # sum_grid stores the sum of averages for each cell
    # count_grid stores how many valid 3x3 regions cover each cell
    sum_grid = [[0] * n for _ in range(m)]
    count_grid = [[0] * n for _ in range(m)]
    
    def is_valid(r, c):
        # Check horizontal adjacency
        for i in range(r, r + 3):
            for j in range(c, c + 2):
                if abs(grid[i][j] - grid[i][j + 1]) > threshold:
                    return False
        # Check vertical adjacency
        for i in range(r, r + 2):
            for j in range(c, c + 3):
                if abs(grid[i][j] - grid[i + 1][j]) > threshold:
                    return False
        return True

    # Iterate through all possible 3x3 top-left corners
    for i in range(m - 2):
        for j in range(n - 2):
            if is_valid(i, j):
                # Calculate average
                total = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        total += grid[r][c]
                avg = total // 9
                
                # Update auxiliary grids
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        sum_grid[r][c] += avg
                        count_grid[r][c] += 1
                        
    # Construct final result
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if count_grid[i][j] > 0:
                result[i][j] = sum_grid[i][j] // count_grid[i][j]
            else:
                result[i][j] = grid[i][j]
                
    return result
