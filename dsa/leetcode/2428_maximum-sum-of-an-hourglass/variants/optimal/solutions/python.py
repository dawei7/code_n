from typing import List

def solve(grid: List[List[int]]) -> int:
    """
    Calculates the maximum sum of an hourglass in a 2D grid.
    An hourglass at (r, c) consists of:
    grid[r][c]   grid[r][c+1]   grid[r][c+2]
                 grid[r+1][c+1]
    grid[r+2][c] grid[r+2][c+1] grid[r+2][c+2]
    """
    rows = len(grid)
    cols = len(grid[0])
    max_sum = float('-inf')
    
    # Iterate through all possible top-left corners of a 3x3 hourglass
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Calculate the sum of the 7 elements in the hourglass
            current_sum = (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] +
                grid[r+1][c+1] +
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            )
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    return int(max_sum)
