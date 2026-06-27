def solve(n: int, queries: list[list[int]]) -> int:
    visited_rows = set()
    visited_cols = set()
    total_sum = 0
    
    # Process queries in reverse order
    for type_i, index_i, val_i in reversed(queries):
        if type_i == 0:  # Row query
            if index_i not in visited_rows:
                visited_rows.add(index_i)
                total_sum += val_i * (n - len(visited_cols))
        else:  # Column query
            if index_i not in visited_cols:
                visited_cols.add(index_i)
                total_sum += val_i * (n - len(visited_rows))
        
        # Early exit if all rows or all columns are fully covered
        if len(visited_rows) == n or len(visited_cols) == n:
            break
            
    return total_sum
