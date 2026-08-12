def solve(days: int = 30) -> int:
    """Find number of prize-winning attendance strings of given length.
    
    Time Complexity: O(days)
    Space Complexity: O(1)
    """
    # dp[lates][consec_absent]
    dp = [[0] * 3 for _ in range(2)]
    dp[0][0] = 1

    for day in range(days):
        next_dp = [[0] * 3 for _ in range(2)]
        for lates in range(2):
            for a in range(3):
                count = dp[lates][a]
                if count == 0:
                    continue

                # 'O' - On time
                next_dp[lates][0] += count

                # 'L' - Late
                if lates == 0:
                    next_dp[1][0] += count

                # 'A' - Absent
                if a < 2:
                    next_dp[lates][a + 1] += count

        dp = next_dp

    return sum(dp[lates][a] for lates in range(2) for a in range(3))
