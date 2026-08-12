def solve(max_len: int = 40) -> int:
    """Find number of pandigital step numbers less than 10^max_len.
    
    Time Complexity: O(max_len * 10 * 2^10)
    Space Complexity: O(10 * 2^10)
    """
    dp = {}
    for d1 in range(1, 10):
        dp[(d1, 1 << d1)] = 1

    total_pandigital = 0

    for L in range(2, max_len + 1):
        new_dp = {}
        for (d, mask), count in dp.items():
            for d_next in (d - 1, d + 1):
                if 0 <= d_next <= 9:
                    new_mask = mask | (1 << d_next)
                    nxt = (d_next, new_mask)
                    new_dp[nxt] = new_dp.get(nxt, 0) + count
        dp = new_dp

        for (d, mask), count in dp.items():
            if mask == 1023:
                total_pandigital += count

    return total_pandigital
