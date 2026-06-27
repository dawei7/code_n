def get_area(grid, r1, r2, c1, c2):
    min_r, max_r = float('inf'), float('-inf')
    min_c, max_c = float('inf'), float('-inf')
    found = False
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 1:
                found = True
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    if not found:
        return 0
    return (max_r - min_r + 1) * (max_c - min_c + 1)

def solve(grid):
    m, n = len(grid), len(grid[0])
    ans = float('inf')

    # Case 1: Three horizontal strips
    for i in range(m):
        for j in range(i + 1, m - 1):
            ans = min(ans, get_area(grid, 0, i, 0, n - 1) + 
                           get_area(grid, i + 1, j, 0, n - 1) + 
                           get_area(grid, j + 1, m - 1, 0, n - 1))

    # Case 2: Three vertical strips
    for i in range(n):
        for j in range(i + 1, n - 1):
            ans = min(ans, get_area(grid, 0, m - 1, 0, i) + 
                           get_area(grid, 0, m - 1, i + 1, j) + 
                           get_area(grid, 0, m - 1, j + 1, n - 1))

    # Case 3: One horizontal cut, then one vertical cut in one of the halves
    for i in range(m - 1):
        # Top half split vertically
        for j in range(n - 1):
            ans = min(ans, get_area(grid, 0, i, 0, j) + 
                           get_area(grid, 0, i, j + 1, n - 1) + 
                           get_area(grid, i + 1, m - 1, 0, n - 1))
        # Bottom half split vertically
        for j in range(n - 1):
            ans = min(ans, get_area(grid, 0, i, 0, n - 1) + 
                           get_area(grid, i + 1, m - 1, 0, j) + 
                           get_area(grid, i + 1, m - 1, j + 1, n - 1))

    # Case 4: One vertical cut, then one horizontal cut in one of the halves
    for i in range(n - 1):
        # Left half split horizontally
        for j in range(m - 1):
            ans = min(ans, get_area(grid, 0, j, 0, i) + 
                           get_area(grid, j + 1, m - 1, 0, i) + 
                           get_area(grid, 0, m - 1, i + 1, n - 1))
        # Right half split horizontally
        for j in range(m - 1):
            ans = min(ans, get_area(grid, 0, m - 1, 0, i) + 
                           get_area(grid, 0, j, i + 1, n - 1) + 
                           get_area(grid, j + 1, m - 1, i + 1, n - 1))

    return ans
