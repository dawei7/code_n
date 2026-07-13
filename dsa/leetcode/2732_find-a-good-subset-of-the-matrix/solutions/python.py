from typing import List

def solve(grid: List[List[int]]) -> List[int]:
    # Map each unique row pattern (as a bitmask) to its first occurrence index
    pattern_to_idx = {}
    for r_idx, row in enumerate(grid):
        mask = 0
        for val in row:
            mask = (mask << 1) | val
        if mask not in pattern_to_idx:
            pattern_to_idx[mask] = r_idx
            
    # Case 1: A row with all 0s exists
    if 0 in pattern_to_idx:
        return [pattern_to_idx[0]]
        
    # Case 2: Find two rows with bitwise AND equal to 0
    masks = list(pattern_to_idx.keys())
    n_masks = len(masks)
    for i in range(n_masks):
        for j in range(i + 1, n_masks):
            if (masks[i] & masks[j]) == 0:
                return sorted([pattern_to_idx[masks[i]], pattern_to_idx[masks[j]]])
                
    return []
