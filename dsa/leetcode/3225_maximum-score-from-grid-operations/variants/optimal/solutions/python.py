def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    height_count = n + 1

    col_prefix = [[0] * height_count for _ in range(n)]
    for col in range(n):
        for row in range(n):
            col_prefix[col][row + 1] = col_prefix[col][row] + grid[row][col]

    def column_score(col: int, height: int, neighbor_height: int) -> int:
        if neighbor_height <= height:
            return 0
        return col_prefix[col][neighbor_height] - col_prefix[col][height]

    if n == 1:
        return 0

    dp = [[-10**30] * height_count for _ in range(height_count)]
    for h0 in range(height_count):
        for h1 in range(height_count):
            dp[h0][h1] = column_score(0, h0, h1)

    for col in range(1, n - 1):
        new_dp = [[-10**30] * height_count for _ in range(height_count)]
        pref = col_prefix[col]

        for current in range(height_count):
            best_prev_at_most = [-10**30] * height_count
            running = -10**30
            for previous in range(height_count):
                running = max(running, dp[previous][current])
                best_prev_at_most[previous] = running

            best_prev_more = [-10**30] * (height_count + 1)
            running = -10**30
            for previous in range(height_count - 1, -1, -1):
                extra = pref[previous] - pref[current] if previous > current else 0
                running = max(running, dp[previous][current] + extra)
                best_prev_more[previous] = running

            for next_height in range(height_count):
                from_left_neighbor = best_prev_at_most[next_height] + column_score(col, current, next_height)
                from_right_neighbor = best_prev_more[next_height + 1]
                new_dp[current][next_height] = max(from_left_neighbor, from_right_neighbor)

        dp = new_dp

    answer = 0
    last_col = n - 1
    for previous in range(height_count):
        for current in range(height_count):
            answer = max(answer, dp[previous][current] + column_score(last_col, current, previous))
    return answer
