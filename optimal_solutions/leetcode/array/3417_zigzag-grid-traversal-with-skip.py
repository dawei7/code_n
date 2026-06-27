from typing import List

def solve(grid: List[List[int]]) -> List[int]:
    result = []
    take = True
    
    for r in range(len(grid)):
        # Determine the range based on row index
        # Even rows: left to right (0 to n-1)
        # Odd rows: right to left (n-1 to 0)
        if r % 2 == 0:
            cols = range(len(grid[r]))
        else:
            cols = range(len(grid[r]) - 1, -1, -1)
            
        for c in cols:
            if take:
                result.append(grid[r][c])
            take = not take
            
    return result
