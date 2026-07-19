def solve(grid: list[list[int]]) -> list[int]:
    n = len(grid)
    n_squared = n * n
    
    # Using a frequency array to track occurrences
    # Size is n^2 + 1 to accommodate values from 1 to n^2
    counts = [0] * (n_squared + 1)
    
    for row in grid:
        for val in row:
            counts[val] += 1
            
    repeated = -1
    missing = -1
    
    for i in range(1, n_squared + 1):
        if counts[i] == 2:
            repeated = i
        elif counts[i] == 0:
            missing = i
            
    return [repeated, missing]
