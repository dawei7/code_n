def solve(grid: list[list[int]]) -> bool:
    if not grid or not grid[0]:
        return False
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Precompute 2D prefix sums
    pref = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            pref[r + 1][c + 1] = grid[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
            
    def get_sum(r1, c1, r2, c2):
        return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

    # There are several ways to partition a grid into 4 rectangles:
    # 1. 4 horizontal strips
    # 2. 4 vertical strips
    # 3. 2 horizontal, 2 vertical (various layouts)
    
    # Check 4 horizontal strips
    if rows >= 4:
        for i in range(rows - 3):
            for j in range(i + 1, rows - 2):
                for k in range(j + 1, rows - 1):
                    s1 = get_sum(0, 0, i, cols - 1)
                    s2 = get_sum(i + 1, 0, j, cols - 1)
                    s3 = get_sum(j + 1, 0, k, cols - 1)
                    s4 = get_sum(k + 1, 0, rows - 1, cols - 1)
                    if s1 == s2 == s3 == s4:
                        return True
                        
    # Check 4 vertical strips
    if cols >= 4:
        for i in range(cols - 3):
            for j in range(i + 1, cols - 2):
                for k in range(j + 1, cols - 1):
                    s1 = get_sum(0, 0, rows - 1, i)
                    s2 = get_sum(0, i + 1, rows - 1, j)
                    s3 = get_sum(0, j + 1, rows - 1, k)
                    s4 = get_sum(0, k + 1, rows - 1, cols - 1)
                    if s1 == s2 == s3 == s4:
                        return True

    # Check 2x2 grid layout (2 horizontal cuts, 1 vertical cut or vice versa)
    # This covers the most common partition types
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Top-left, Top-right, Bottom-left, Bottom-right
            s1 = get_sum(0, 0, r, c)
            s2 = get_sum(0, c + 1, r, cols - 1)
            s3 = get_sum(r + 1, 0, rows - 1, c)
            s4 = get_sum(r + 1, c + 1, rows - 1, cols - 1)
            if s1 == s2 == s3 == s4:
                return True
                
    return False
