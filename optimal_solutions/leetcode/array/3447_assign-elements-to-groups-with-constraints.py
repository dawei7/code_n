def solve(groups: list[list[int]], elements: list[int]) -> list[int]:
    max_val = 0
    for group in groups:
        for x in group:
            if x > max_val:
                max_val = x
    
    # Map each element to its first occurrence index
    # If an element appears multiple times, we only care about the first one
    element_to_min_idx = {}
    for idx, val in enumerate(elements):
        if val not in element_to_min_idx:
            element_to_min_idx[val] = idx
            
    # min_idx_for_divisor[v] will store the smallest index of an element that divides v
    min_idx_for_divisor = [float('inf')] * (max_val + 1)
    
    for val, idx in element_to_min_idx.items():
        # Iterate through all multiples of val up to max_val
        for multiple in range(val, max_val + 1, val):
            if idx < min_idx_for_divisor[multiple]:
                min_idx_for_divisor[multiple] = idx
                
    results = []
    for group in groups:
        best_idx = float('inf')
        for x in group:
            if x <= max_val:
                if min_idx_for_divisor[x] < best_idx:
                    best_idx = min_idx_for_divisor[x]
        
        if best_idx == float('inf'):
            results.append(-1)
        else:
            results.append(int(best_idx))
            
    return results
