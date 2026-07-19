def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    mid = n // 2
    
    # y_counts stores frequency of 0, 1, 2 in the Y shape
    # other_counts stores frequency of 0, 1, 2 in the rest of the grid
    y_counts = [0] * 3
    other_counts = [0] * 3
    
    y_cells = 0
    
    for r in range(n):
        for c in range(n):
            is_y = False
            # Condition for Y shape:
            # 1. Main diagonal: r == c (up to mid)
            # 2. Anti-diagonal: r + c == n - 1 (up to mid)
            # 3. Vertical stem: c == mid and r >= mid
            if (r <= mid and (r == c or r + c == n - 1)) or (r >= mid and c == mid):
                is_y = True
            
            if is_y:
                y_counts[grid[r][c]] += 1
                y_cells += 1
            else:
                other_counts[grid[r][c]] += 1
                
    total_cells = n * n
    other_cells = total_cells - y_cells
    
    min_ops = float('inf')
    
    # Try all combinations of v1 (value for Y) and v2 (value for others)
    # v1 != v2, where v1, v2 in {0, 1, 2}
    for v1 in range(3):
        for v2 in range(3):
            if v1 == v2:
                continue
            
            # Cost = (cells in Y not equal to v1) + (cells not in Y not equal to v2)
            cost = (y_cells - y_counts[v1]) + (other_cells - other_counts[v2])
            if cost < min_ops:
                min_ops = cost
                
    return int(min_ops)
