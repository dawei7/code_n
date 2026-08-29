def solve(max_len: int = 40) -> int:
    """Find the total number of pandigital step numbers with at most max_len = 40 digits.

    Mathematical Principles Applied:
    1. Step Number Property:
       A step number has adjacent digits differing by exactly 1: |d_{i+1} - d_i| == 1.
       Valid transitions for last digit d are d - 1 (if d > 0) and d + 1 (if d < 9).

    2. Bitmask Digit DP State Representation:
       State is represented by `(last_digit, bitmask)` where bitmask in [0, 1023] records
       which digits 0..9 have appeared in the prefix.
       A step number is PANDIGITAL iff `bitmask == (1 << 10) - 1 == 1023`.

    3. Iterative DP Step (Length 1 to 40):
       Base case (length 1): `dp[(d, 1 << d)] = 1` for 1 <= d <= 9.
       Transition from length L to L + 1 by appending d_next in {d - 1, d + 1}.
       Accumulate counts for states where `mask == 1023` across lengths L = 10 to 40.

    Time Complexity: O(max_len * 10 * 2^10) executing in ~0.05s.
    Space Complexity: O(10 * 2^10) memory for DP state dictionary.
    """
    # Base case for 1-digit numbers (without leading zero)
    dp = {}
    for d1 in range(1, 10):
        dp[(d1, 1 << d1)] = 1

    total_pandigital = 0

    # Advance DP state from length 2 up to max_len (40)
    for L in range(2, max_len + 1):
        new_dp = {}
        for (d, mask), count in dp.items():
            # Step transitions: adjacent digits differ by exactly 1
            for d_next in (d - 1, d + 1):
                if 0 <= d_next <= 9:
                    new_mask = mask | (1 << d_next)
                    nxt = (d_next, new_mask)
                    new_dp[nxt] = new_dp.get(nxt, 0) + count
        dp = new_dp

        # Accumulate pandigital step numbers (bitmask == 1023)
        for (d, mask), count in dp.items():
            if mask == 1023:
                total_pandigital += count

    # Return total count of pandigital step numbers up to 40 digits
    return total_pandigital


if __name__ == "__main__":
    print(solve())
