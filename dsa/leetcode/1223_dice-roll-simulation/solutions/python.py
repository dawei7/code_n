def solve(n, roll_max):
    mod = 1_000_000_007
    dp = [[0] * (roll_max[i] + 1) for i in range(6)]
    for face in range(6):
        dp[face][1] = 1

    for _ in range(1, n):
        next_dp = [[0] * (roll_max[i] + 1) for i in range(6)]
        totals = [sum(row) % mod for row in dp]
        all_total = sum(totals) % mod
        for face in range(6):
            next_dp[face][1] = (all_total - totals[face]) % mod
            for count in range(1, roll_max[face]):
                next_dp[face][count + 1] = dp[face][count]
        dp = next_dp

    return sum(sum(row) for row in dp) % mod
