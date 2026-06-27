def solve(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    # Directions: (dr, dc)
    # 0: down-right, 1: down-left, 2: up-left, 3: up-right
    dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    
    # memo[r][c][dir] stores the length of the path of 1s starting at (r, c)
    memo = {}

    def get_len(r, c, d):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
            return 0
        if (r, c, d) in memo:
            return memo[(r, c, d)]
        
        dr, dc = dirs[d]
        res = 1 + get_len(r + dr, c + dc, d)
        memo[(r, c, d)] = res
        return res

    max_v = 0
    
    # A V-shape: 2 -> 1s -> 0 -> 1s -> 2
    # We iterate over every 0 as the vertex
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Try all 4 pairs of directions that form a V
                # Pairs: (down-right, up-left), (down-left, up-right), etc.
                # Actually, the path is 2 -> 1s -> 0 -> 1s -> 2
                # So we look for 1s ending at 0, and 1s starting at 0
                for d1 in range(4):
                    d2 = (d1 + 2) % 4
                    # Path 1: 2 -> 1s -> 0
                    # Path 2: 0 -> 1s -> 2
                    # To find 2 -> 1s -> 0, we look at the cell before 0 in direction d1
                    dr1, dc1 = dirs[d1]
                    pr, pc = r - dr1, c - dc1
                    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] == 1:
                        len1 = get_len(pr, pc, d1)
                        # Now look for 0 -> 1s -> 2
                        dr2, dc2 = dirs[d2]
                        nr, nc = r + dr2, c + dc2
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            len2 = get_len(nr, nc, d2)
                            # Check if the ends are 2s
                            end1_r, end1_c = pr + len1 * dr1, pc + len1 * dc1
                            end2_r, end2_c = nr + len2 * dr2, nc + len2 * dc2
                            
                            if (0 <= end1_r < rows and 0 <= end1_c < cols and grid[end1_r][end1_c] == 2 and
                                0 <= end2_r < rows and 0 <= end2_c < cols and grid[end2_r][end2_c] == 2):
                                max_v = max(max_v, len1 + len2 + 1)
            elif grid[r][c] == 2:
                # Handle case where V-shape might be just 2-0-2
                for d in range(4):
                    dr, dc = dirs[d]
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        # Look for another 2 on the other side of 0
                        d_opp = (d + 2) % 4
                        nnr, nnc = nr + dr, nc + dc
                        if 0 <= nnr < rows and 0 <= nnc < cols and grid[nnr][nnc] == 2:
                            max_v = max(max_v, 3)
                            
    return max_v
