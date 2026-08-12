def solve(
    shots: int = 50, target_scored: int = 20, target_prob: float = 0.02
) -> str:
    """Find q > 50 such that the probability of scoring exactly 20 points in 50 shots is 0.02, rounded to 10 decimal places.
    
    Time Complexity: O(shots^2 * log_2(1/eps))
    Space Complexity: O(shots)
    """

    def prob_20(q):
        dp = [0.0] * (shots + 1)
        dp[0] = 1.0
        for x in range(1, shots + 1):
            p_score = 1.0 - x / q
            p_miss = x / q
            next_dp = [0.0] * (shots + 1)
            next_dp[0] = dp[0] * p_miss
            for k in range(1, min(x + 1, shots + 1)):
                next_dp[k] = dp[k] * p_miss + dp[k - 1] * p_score
            dp = next_dp
        return dp[target_scored]

    lo = 50.0000000000001
    hi = 100.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if prob_20(mid) < target_prob:
            hi = mid
        else:
            lo = mid

    return f"{lo:.10f}"
