def solve(seats):
    rows = len(seats)
    cols = len(seats[0]) if rows else 0
    valid_by_row = []
    for r in range(rows):
        blocked = 0
        for c in range(cols):
            if seats[r][c] == "#":
                blocked |= 1 << c
        masks = []
        for mask in range(1 << cols):
            if mask & blocked or mask & (mask << 1):
                continue
            masks.append(mask)
        valid_by_row.append(masks)

    dp = {0: 0}
    for masks in valid_by_row:
        next_dp = {}
        for mask in masks:
            count = mask.bit_count()
            best = 0
            for prev, value in dp.items():
                if mask & (prev << 1) or mask & (prev >> 1):
                    continue
                best = max(best, value + count)
            next_dp[mask] = best
        dp = next_dp
    return max(dp.values(), default=0)
