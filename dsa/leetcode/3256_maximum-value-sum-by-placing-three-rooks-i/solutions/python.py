def solve(board: list[list[int]]) -> int:
    m = len(board)
    n = len(board[0])
    
    # Pre-process: For each row, keep only the top 3 values and their column indices
    # This reduces the search space significantly.
    top_rows = []
    for r in range(m):
        row_data = []
        for c in range(n):
            row_data.append((board[r][c], c))
        # Sort descending by value and take top 3
        row_data.sort(key=lambda x: x[0], reverse=True)
        top_rows.append(row_data[:3])
    
    max_sum = -float('inf')
    
    # Iterate through all combinations of 3 rows
    for r1 in range(m):
        for r2 in range(r1 + 1, m):
            for r3 in range(r2 + 1, m):
                # For each row, we have up to 3 candidates
                for val1, c1 in top_rows[r1]:
                    for val2, c2 in top_rows[r2]:
                        if c2 == c1:
                            continue
                        for val3, c3 in top_rows[r3]:
                            if c3 == c1 or c3 == c2:
                                continue
                            
                            current_sum = val1 + val2 + val3
                            if current_sum > max_sum:
                                max_sum = current_sum
                                
    return max_sum
