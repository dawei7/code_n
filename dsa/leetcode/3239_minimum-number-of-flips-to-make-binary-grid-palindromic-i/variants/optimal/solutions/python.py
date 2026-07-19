def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    # Calculate flips needed to make all rows palindromic
    row_flips = 0
    for r in range(rows):
        left, right = 0, cols - 1
        while left < right:
            if grid[r][left] != grid[r][right]:
                row_flips += 1
            left += 1
            right -= 1
            
    # Calculate flips needed to make all columns palindromic
    col_flips = 0
    for c in range(cols):
        top, bottom = 0, rows - 1
        while top < bottom:
            if grid[top][c] != grid[bottom][c]:
                col_flips += 1
            top += 1
            bottom -= 1
            
    return min(row_flips, col_flips)
