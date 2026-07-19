from collections import defaultdict
from typing import List

def solve(mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    val_to_coords = defaultdict(list)
    for r in range(m):
        for c in range(n):
            val_to_coords[mat[r][c]].append((r, c))
            
    row_max = [0] * m
    col_max = [0] * n
    
    for val in sorted(val_to_coords.keys()):
        coords = val_to_coords[val]
        # Store the new dp values for this batch
        updates = []
        for r, c in coords:
            dp_val = max(row_max[r], col_max[c]) + 1
            updates.append((r, c, dp_val))
        
        # Apply updates to row_max and col_max
        for r, c, dp_val in updates:
            row_max[r] = max(row_max[r], dp_val)
            col_max[c] = max(col_max[c], dp_val)
            
    return max(max(row_max), max(col_max))
