import collections

def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    
    # Use collections.Counter to store frequencies of unique rows
    # Tuples are used as keys because lists are not hashable.
    row_counts = collections.Counter()
    for r_idx in range(n):
        row_counts[tuple(grid[r_idx])] += 1
        
    # Use collections.Counter to store frequencies of unique columns
    col_counts = collections.Counter()
    for c_idx in range(n):
        current_col = []
        for r_idx in range(n):
            current_col.append(grid[r_idx][c_idx])
        col_counts[tuple(current_col)] += 1
        
    # Calculate the number of equal pairs
    equal_pairs = 0
    # Iterate through each unique row type and its frequency
    for row_tuple, row_freq in row_counts.items():
        # If this row_tuple also exists as a column, multiply their frequencies.
        # If row_tuple is not in col_counts, col_counts[row_tuple] will return 0,
        # correctly adding nothing to equal_pairs for that specific row type.
        equal_pairs += row_freq * col_counts[row_tuple]
        
    return equal_pairs
