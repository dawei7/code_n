def solve(board: list[list[int]]) -> int:
    m = len(board)
    n = len(board[0])
    
    # Precompute top 3 values for each row
    row_tops = []
    for r in range(m):
        # Get top 3 values with their column indices
        row_vals = sorted([(board[r][c], c) for c in range(n)], reverse=True)
        row_tops.append(row_vals[:3])
        
    max_sum = -float('inf')
    
    # Iterate over all pairs of rows (r1, r2)
    for r1 in range(m):
        for r2 in range(r1 + 1, m):
            # Try all combinations of top 3 from r1 and r2
            for val1, c1 in row_tops[r1]:
                for val2, c2 in row_tops[r2]:
                    if c1 == c2:
                        continue
                    
                    # Find the best r3 that doesn't conflict with c1 and c2
                    for r3 in range(m):
                        if r3 == r1 or r3 == r2:
                            continue
                        
                        for val3, c3 in row_tops[r3]:
                            if c3 != c1 and c3 != c2:
                                current_sum = val1 + val2 + val3
                                if current_sum > max_sum:
                                    max_sum = current_sum
                                # Since row_tops is sorted, we can break early
                                break
    return max_sum
