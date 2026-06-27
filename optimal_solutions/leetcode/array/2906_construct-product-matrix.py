from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    n = rows * cols
    MOD = 12345
    
    # Flatten the grid into a 1D array for easier prefix/suffix calculation
    flat = [grid[r][c] for r in range(rows) for c in range(cols)]
    
    prefix = [1] * n
    suffix = [1] * n
    
    # Calculate prefix products
    curr = 1
    for i in range(n):
        prefix[i] = curr
        curr = (curr * flat[i]) % MOD
        
    # Calculate suffix products
    curr = 1
    for i in range(n - 1, -1, -1):
        suffix[i] = curr
        curr = (curr * flat[i]) % MOD
        
    # Construct the result matrix
    res = [[0] * cols for _ in range(rows)]
    for i in range(n):
        r, c = divmod(i, cols)
        res[r][c] = (prefix[i] * suffix[i]) % MOD
        
    return res
