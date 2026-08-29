def solve(days: int = 30) -> int:
    """Find the number of prize-winning attendance strings over days = 30 days.

    Mathematical Principles Applied:
    1. Prize String Attendance Rules:
       Each day's attendance is marked 'O' (On time), 'L' (Late), or 'A' (Absent).
       A string is prize-winning iff:
       - Contains at most 1 'L' (Late) overall (lates < 2).
       - Contains no 3 consecutive 'A's (consec_absent < 3).

    2. Dynamic Programming State Tracking:
       State is represented by `dp[lates][consec_absent]` (2 x 3 state space).
       - 'O': resets consec_absent to 0 (`next_dp[lates][0] += count`).
       - 'L': increments lates to 1 and resets consec_absent to 0 (`next_dp[1][0] += count` if lates == 0).
       - 'A': increments consec_absent by 1 (`next_dp[lates][a + 1] += count` if a < 2).

    3. Iterative DP Step (Days 1 to 30):
       Base case (Day 0): `dp[0][0] = 1`.
       Advance DP day-by-day up to 30 days. Return total sum across all 6 valid states.

    Time Complexity: O(days) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # dp[lates][consec_absent]
    dp = [[0] * 3 for _ in range(2)]
    dp[0][0] = 1

    # Advance DP through days = 1 to 30
    for day in range(days):
        next_dp = [[0] * 3 for _ in range(2)]
        for lates in range(2):
            for a in range(3):
                count = dp[lates][a]
                if count == 0:
                    continue

                # Attendance 'O' (On time): resets consecutive absents to 0
                next_dp[lates][0] += count

                # Attendance 'L' (Late): increases total lates count if < 1
                if lates == 0:
                    next_dp[1][0] += count

                # Attendance 'A' (Absent): increases consecutive absents if < 2
                if a < 2:
                    next_dp[lates][a + 1] += count

        dp = next_dp

    # Return total sum of all valid 30-day prize-winning attendance strings
    return sum(dp[lates][a] for lates in range(2) for a in range(3))


if __name__ == "__main__":
    print(solve())
