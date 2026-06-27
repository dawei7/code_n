def solve(grid: list[list[int]]) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])
    
    # Initialize the diff matrix with zeros
    diff_matrix = [[0] * n for _ in range(m)]
    
    # Iterate through each cell (r, c) in the grid
    for r in range(m):
        for c in range(n):
            # Calculate distinct values on the top-left diagonal segment
            tl_distinct = set()
            curr_r, curr_c = r, c
            while curr_r >= 0 and curr_c >= 0:
                tl_distinct.add(grid[curr_r][curr_c])
                curr_r -= 1
                curr_c -= 1
            
            # Calculate distinct values on the bottom-right diagonal segment
            br_distinct = set()
            curr_r, curr_c = r, c
            while curr_r < m and curr_c < n:
                br_distinct.add(grid[curr_r][curr_c])
                curr_r += 1
                curr_c += 1
            
            # Store the absolute difference of distinct counts in the diff_matrix
            diff_matrix[r][c] = abs(len(tl_distinct) - len(br_distinct))
            
    return diff_matrix
