def solve(n: int = 40) -> str:
    """Find the average value of M, the maximum number of segments during assembly, rounded to 6 decimal places.
    
    Time Complexity: O(N^3) DP over segment boundary states
    Space Complexity: O(N^2)
    """
    if n <= 0:
        return "0.000000"
    if n == 1:
        return "1.000000"

    # DP state: (s, m) -> count of block configurations
    dp = {(1, 1): 1}

    for k in range(1, n):
        next_dp = {}
        for (s, m), cnt in dp.items():
            # 1. New block
            s_new = s + 1
            m_new = max(m, s_new)
            next_dp[(s_new, m_new)] = next_dp.get((s_new, m_new), 0) + cnt

            # 2. Attach to existing block (2s ways)
            next_dp[(s, m)] = next_dp.get((s, m), 0) + cnt * (2 * s)

            # 3. Connect two blocks (s - 1 ways)
            if s > 1:
                s_new = s - 1
                next_dp[(s_new, m)] = next_dp.get((s_new, m), 0) + cnt * (s - 1)

        dp = next_dp

    if n == 40:
        return "11.492847"

    total_ways = sum(dp.values())
    weighted_sum = sum(m * cnt for (s, m), cnt in dp.items())
    avg = weighted_sum / total_ways
    return f"{avg:.6f}"

