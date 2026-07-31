def solve(grid: list[list[int]]) -> int:
    extras: list[tuple[int, int]] = []
    empty: list[tuple[int, int]] = []

    for row in range(3):
        for col in range(3):
            stones = grid[row][col]
            if stones == 0:
                empty.append((row, col))
            else:
                extras.extend([(row, col)] * (stones - 1))

    k = len(empty)
    dp = [float("inf")] * (1 << k)
    dp[0] = 0

    for mask in range(1 << k):
        extra_index = mask.bit_count()
        if extra_index == k:
            continue

        source_row, source_col = extras[extra_index]
        for target_index, (target_row, target_col) in enumerate(empty):
            if mask & (1 << target_index):
                continue
            next_mask = mask | (1 << target_index)
            distance = abs(source_row - target_row) + abs(source_col - target_col)
            dp[next_mask] = min(dp[next_mask], dp[mask] + distance)

    return dp[-1]
