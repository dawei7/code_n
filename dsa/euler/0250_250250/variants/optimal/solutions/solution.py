def solve(limit: int = 250250, mod: int = 10**16) -> int:
    """Find the number of non-empty subsets of {1^1, ..., limit^limit} whose sum is divisible by 250.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Modular Periodicity of k^k mod 250:
       Since 250 = 2 * 5^3:
           lambda(250) = lcm(phi(2), phi(125)) = lcm(1, 100) = 100.
       The sequence k^k mod 250 is strictly periodic with period lcm(250, 100) = 500.

    2. Frequency Counting:
       We count the occurrences of each residue r in [0, 249] among the limit elements.

    3. Dynamic Programming Modulo 250:
       Let dp[s] be the number of subsets whose sum modulo 250 is s.
       - Initialize dp[0] = 1.
       - Elements with residue r = 0 multiply the subset count by 2^{count[0]}.
       - For each non-zero residue r with frequency count[r], we update:
           dp[s + r mod 250] = (dp[s + r mod 250] + dp[s]) mod 10^16.

    4. Non-Empty Subset Result:
       The number of non-empty subsets with sum divisible by 250 is (dp[0] - 1) mod 10^16.

    Complexity:
    -----------
    - Time Complexity: O(500 + 250 * limit) (~5.0 seconds).
    - Space Complexity: O(250) DP array.
    """
    if limit < 1:
        return 0

    counts = [0] * 250
    full_periods = limit // 500
    for i in range(1, 501):
        counts[pow(i, i, 250)] += full_periods
    for i in range(1, limit % 500 + 1):
        counts[pow(i, i, 250)] += 1

    dp = [0] * 250
    dp[0] = 1

    for r in range(250):
        cnt = counts[r]
        if cnt == 0:
            continue
        if r == 0:
            mult = pow(2, cnt, mod)
            dp = [(x * mult) % mod for x in dp]
            continue

        for _ in range(cnt):
            nxt = list(dp)
            for i in range(250):
                target = (i + r) % 250
                nv = nxt[target] + dp[i]
                nxt[target] = nv if nv < mod else (nv % mod)
            dp = nxt

    return (dp[0] - 1) % mod


if __name__ == "__main__":
    print(solve())
