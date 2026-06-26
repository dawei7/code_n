from typing import List

def solve(grid: List[List[int]]) -> int:
    """
    Calculates the sum of the maximums of removed elements by sorting each row
    and iterating through the columns.
    """
    # Sort each row in-place to easily access elements from largest to smallest
    for row in grid:
        row.sort()
    
    total_sum = 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # After sorting, the largest elements are at the end of each row.
    # We iterate through each column index (representing one operation step).
    for col in range(num_cols):
        max_val = 0
        for row in range(num_rows):
            # Update the max_val for the current operation step
            if grid[row][col] > max_val:
                max_val = grid[row][col]
        total_sum += max_val
        
    return total_sum
