from typing import List

def solve(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Precompute the maximum value for each column
    col_maxes = []
    for c in range(cols):
        current_max = -1
        for r in range(rows):
            if matrix[r][c] > current_max:
                current_max = matrix[r][c]
        col_maxes.append(current_max)
    
    # Create a result matrix or modify in place
    # Here we modify in place for efficiency
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == -1:
                matrix[r][c] = col_maxes[c]
                
    return matrix
