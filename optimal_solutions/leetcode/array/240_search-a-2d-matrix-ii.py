from typing import List

def solve(matrix: List[List[int]], target: int) -> bool:
    """
    Searches for a target in a 2D matrix sorted by rows and columns.
    Uses the staircase search algorithm starting from the top-right corner.
    """
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start at the top-right corner
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif current > target:
            # Target must be in a column to the left
            col -= 1
        else:
            # Target must be in a row below
            row += 1
            
    return False
