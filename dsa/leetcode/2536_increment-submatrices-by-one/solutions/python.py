def solve(n: int, queries: list[list[int]]) -> list[list[int]]:
    # Initialize a difference array with size (n+1) x (n+1)
    # to handle boundary conditions easily.
    diff = [[0] * (n + 1) for _ in range(n + 1)]
    
    for r1, c1, r2, c2 in queries:
        diff[r1][c1] += 1
        if r2 + 1 < n:
            diff[r2 + 1][c1] -= 1
        if c2 + 1 < n:
            diff[r1][c2 + 1] -= 1
        if r2 + 1 < n and c2 + 1 < n:
            diff[r2 + 1][c2 + 1] += 1
            
    # Compute the 2D prefix sum to get the actual values
    res = [[0] * n for _ in range(n)]
    
    # First, compute prefix sums along rows
    for r in range(n):
        current_row_sum = 0
        for c in range(n):
            current_row_sum += diff[r][c]
            diff[r][c] = current_row_sum
            
    # Then, compute prefix sums along columns
    for c in range(n):
        current_col_sum = 0
        for r in range(n):
            current_col_sum += diff[r][c]
            res[r][c] = current_col_sum
            
    return res
