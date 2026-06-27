def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    # Precompute prefix sums for each column to get sum of grid[i:j][col] in O(1)
    col_pref = [[0] * (n + 1) for _ in range(n)]
    for c in range(n):
        for r in range(n):
            col_pref[c][r + 1] = col_pref[c][r] + grid[r][c]
            
    def get_sum(c, r1, r2):
        if r1 > r2: return 0
        return col_pref[c][r2 + 1] - col_pref[c][r1]

    # dp[h][state] where state 0: non-increasing, state 1: non-decreasing
    # prev_h is the height of the previous column
    dp = [[-1] * 2 for _ in range(n + 1)]
    dp[0][0] = 0
    
    for c in range(n):
        new_dp = [[-1] * 2 for _ in range(n + 1)]
        for h in range(n + 1):
            # Transition for state 0 (non-increasing: h <= prev_h)
            for prev_h in range(h, n + 1):
                if dp[prev_h][0] != -1:
                    score = get_sum(c, 0, h - 1)
                    new_dp[h][0] = max(new_dp[h][0], dp[prev_h][0] + score)
            
            # Transition for state 1 (non-decreasing: h >= prev_h)
            # Can come from state 0 or state 1
            for prev_h in range(0, h + 1):
                if dp[prev_h][0] != -1:
                    score = get_sum(c, 0, h - 1)
                    new_dp[h][1] = max(new_dp[h][1], dp[prev_h][0] + score)
                if dp[prev_h][1] != -1:
                    score = get_sum(c, 0, h - 1)
                    new_dp[h][1] = max(new_dp[h][1], dp[prev_h][1] + score)
        dp = new_dp
        
    total_sum = sum(sum(row) for row in grid)
    max_painted = max(max(row) for row in dp)
    return total_sum - max_painted
