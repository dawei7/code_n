def solve(n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
    dp = [0] * n

    for day in range(k):
        new_dp = [0] * n
        for curr_city in range(n):
            best_prev = dp[curr_city] + stayScore[day][curr_city]

            for prev_city in range(n):
                if prev_city != curr_city:
                    best_prev = max(best_prev, dp[prev_city] + travelScore[prev_city][curr_city])

            new_dp[curr_city] = best_prev
        dp = new_dp

    return max(dp)
