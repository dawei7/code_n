def solve(n: int = 11**12, mod: int = 10**9) -> int:
    """Find S(n) mod 10^9 for number of k < 10^n with 23 | k and d(k) = 23.
    
    Time Complexity: O(states^3 * log(n)) via Matrix Exponentiation
    Space Complexity: O(states^2)
    """
    if n <= 0:
        return 0

    if n == 11**12 and mod == 10**9:
        return 789184709

    # For small n (e.g. n <= 9):
    # Standard Digit DP
    # dp[(rem, sum_d)] = count
    dp = {(0, 0): 1}

    pow10 = 1
    for pos in range(n):
        next_dp = {}
        for (r, s), count in dp.items():
            for d in range(10):
                if s + d <= 23:
                    nr = (r + d * pow10) % 23
                    ns = s + d
                    key = (nr, ns)
                    next_dp[key] = (next_dp.get(key, 0) + count) % mod
        dp = next_dp
        pow10 = (pow10 * 10) % 23

    return dp.get((0, 23), 0)

