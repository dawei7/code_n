def solve(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    row_counts = [0] * rows
    col_counts = [0] * cols
    
    # Pre-calculate the number of 1s in each row and column
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1
                
    total_triangles = 0
    
    # For each cell containing a 1, treat it as the right-angle vertex
    # The number of triangles is (ones_in_row - 1) * (ones_in_col - 1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                r_ones = row_counts[r]
                c_ones = col_counts[c]
                
                if r_ones > 1 and c_ones > 1:
                    total_triangles += (r_ones - 1) * (c_ones - 1)
                    
    return total_triangles
