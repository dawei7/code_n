def solve(
    l: int,
    n: int,
    k: int,
    position: list[int],
    time: list[int],
) -> int:
    prefix_time = [0]
    for value in time:
        prefix_time.append(prefix_time[-1] + value)

    infinity = 10**30
    dp = [[[infinity] * (k + 1) for _ in range(k + 1)] for _ in range(n)]
    dp[0][0][0] = 0

    for current in range(n - 1):
        for removed in range(k + 1):
            for before in range(k + 1):
                cost = dp[current][removed][before]
                if cost == infinity:
                    continue

                rate = prefix_time[current + 1] - prefix_time[current - before]
                max_skipped = min(k - removed, n - 2 - current)

                for skipped in range(max_skipped + 1):
                    next_sign = current + skipped + 1
                    total = cost + (position[next_sign] - position[current]) * rate
                    dp[next_sign][removed + skipped][skipped] = min(
                        dp[next_sign][removed + skipped][skipped],
                        total,
                    )

    return min(dp[n - 1][k])
