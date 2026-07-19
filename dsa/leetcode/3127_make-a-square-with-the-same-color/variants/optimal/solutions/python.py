def solve(grid: list[list[str]]) -> bool:
    """
    Checks if any 2x2 subgrid can be made monochromatic by changing at most one cell.
    A 2x2 square can be made monochromatic if it contains at least 3 cells of the same color.
    """
    # There are four possible 2x2 squares in a 3x3 grid.
    # Their top-left corners are at (0,0), (0,1), (1,0), and (1,1).
    for i in range(2):
        for j in range(2):
            # Collect the four cells in the current 2x2 square
            cells = [
                grid[i][j], 
                grid[i+1][j], 
                grid[i][j+1], 
                grid[i+1][j+1]
            ]
            
            # Count occurrences of 'B' and 'W'
            black_count = cells.count('B')
            white_count = cells.count('W')
            
            # If either color appears 3 or 4 times, we can form a monochromatic square
            if black_count >= 3 or white_count >= 3:
                return True
                
    return False
