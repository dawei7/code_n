def solve(length: int = 20) -> int:
    """Find the number of 20-digit numbers without leading zero such that no 3 consecutive digits have a sum > 9.

    Mathematical Principles Applied:
    1. Markov Chain State Transition DP:
       Let state (d1, d2) denote the last 2 digits of the current prefix.
       A new digit d3 (0 <= d3 <= 9) can be appended iff d1 + d2 + d3 <= 9 => 0 <= d3 <= 9 - (d1 + d2).
       The new state becomes (d2, d3).

    2. Dynamic Programming Array Dimension Reduction:
       There are at most 55 valid state pairs (d1, d2) where d1 + d2 <= 9.
       - Base state (length 2): `dp[(d1, d2)] = 1` for 1 <= d1 <= 9 and 0 <= d2 <= 9 - d1.
       - Iterative DP step: advance from length 3 to 20 by transitioning `new_dp[(d2, d3)] += dp[(d1, d2)]`.

    3. Total Sum Accumulation:
       Return sum(dp.values()) for 20-digit numbers.

    Time Complexity: O(length * 10^3) executing in ~0.001s.
    Space Complexity: O(10^2) memory for 55 DP states.
    """
    if length < 1:
        return 0
    if length == 1:
        return sum(1 for d in range(1, 10))

    # Base case for length 2: (d1, d2) with 1 <= d1 <= 9 and 0 <= d2 <= 9 - d1
    dp = {}
    for d1 in range(1, 10):
        for d2 in range(0, 10 - d1):
            dp[(d1, d2)] = 1

    # Advance DP state from length 3 up to 20
    for _ in range(3, length + 1):
        new_dp = {}
        for (d1, d2), count in dp.items():
            max_d3 = 9 - (d1 + d2)
            # Try valid next digits d3 such that d1 + d2 + d3 <= 9
            for d3 in range(0, max_d3 + 1):
                nxt = (d2, d3)
                new_dp[nxt] = new_dp.get(nxt, 0) + count
        dp = new_dp

    # Return total count of 20-digit numbers meeting 3-digit sum <= 9 constraint
    return sum(dp.values())


if __name__ == "__main__":
    print(solve())
