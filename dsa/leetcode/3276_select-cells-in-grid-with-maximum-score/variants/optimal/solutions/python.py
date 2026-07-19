from collections import defaultdict

def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    
    # Map each value to the list of rows it appears in
    val_to_rows = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            val_to_rows[grid[r][c]].append(r)
            
    # Sort unique values to process them in order
    unique_vals = sorted(val_to_rows.keys(), reverse=True)
    
    # dp[mask] = max sum using rows represented by mask
    # mask is a bitmask of length 'rows'
    dp = {0: 0}
    
    for val in unique_vals:
        new_dp = dp.copy()
        possible_rows = set(val_to_rows[val])
        
        for mask, current_sum in dp.items():
            for r in possible_rows:
                # If row r is not yet used in the mask
                if not (mask & (1 << r)):
                    new_mask = mask | (1 << r)
                    new_dp[new_mask] = max(new_dp.get(new_mask, 0), current_sum + val)
        dp = new_dp
        
    return max(dp.values())
