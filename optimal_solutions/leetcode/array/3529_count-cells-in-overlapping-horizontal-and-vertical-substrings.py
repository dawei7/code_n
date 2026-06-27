from typing import List

def solve(grid: List[List[str]], pattern: str) -> int:
    if not grid or not grid[0] or not pattern:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    p_len = len(pattern)
    
    # horizontal_mask[r][c] is True if grid[r][c] is part of a horizontal pattern
    horizontal_mask = [[False for _ in range(cols)] for _ in range(rows)]
    # vertical_mask[r][c] is True if grid[r][c] is part of a vertical pattern
    vertical_mask = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Check horizontal patterns
    if cols >= p_len:
        for r in range(rows):
            for c in range(cols - p_len + 1):
                match = True
                for k in range(p_len):
                    if grid[r][c + k] != pattern[k]:
                        match = False
                        break
                if match:
                    for k in range(p_len):
                        horizontal_mask[r][c + k] = True
                        
    # Check vertical patterns
    if rows >= p_len:
        for c in range(cols):
            for r in range(rows - p_len + 1):
                match = True
                for k in range(p_len):
                    if grid[r + k][c] != pattern[k]:
                        match = False
                        break
                if match:
                    for k in range(p_len):
                        vertical_mask[r + k][c] = True
                        
    # Count intersections
    count = 0
    for r in range(rows):
        for c in range(cols):
            if horizontal_mask[r][c] and vertical_mask[r][c]:
                count += 1
                
    return count
