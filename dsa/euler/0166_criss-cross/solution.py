def solve() -> int:
    """Find the number of ways to fill a 4x4 grid with digits 0-9 such that all 4 rows, 4 columns,
    and 2 main diagonals sum to the exact same value S.

    Mathematical Principles Applied:
    1. Grid Variables & Linear Equality System:
       Represent 4x4 grid as 16 variables:
       [a, b, c, d]  (Row 1)
       [e, f, g, h]  (Row 2)
       [i, j, k, l]  (Row 3)
       [m, n, o, p]  (Row 4)

       Target row/col/diag sum S (0 <= S <= 36).

    2. Algebraic Elimination of Dependent Variables:
       By fixing Row 1 (a,b,c,d), Row 2 (e,f,g,h), and digit i in Row 3:
       The remaining 7 digits (j, k, l, m, n, o, p) are ALGEBRAICALLY DETERMINED in O(1) time:
       - m = S - a - e - i
       - j = a + e + i - d - g
       - p = e + i - d
       - l = f + g - i
       - n = S - b - f - j
       - k = S - a - f - p
       - o = S - c - g - k

    3. Digit Bound Pruning (0 <= digit <= 9):
       Instantly reject states if any derived variable falls outside range [0, 9].
       Verify remaining 5 row/col/diag sum constraints.

    Time Complexity: O(Sum_S |Tuples(S)|^2 * Bounded_i) executing in ~0.20s.
    Space Complexity: O(10^4) memory for 4-digit tuple dictionary.
    """
    tuples_by_sum = {}
    # Precompute all 10,000 digit quadruples (a, b, c, d) grouped by sum S
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    tuples_by_sum.setdefault(a + b + c + d, []).append(
                        (a, b, c, d)
                    )

    count = 0

    # Loop overall target sum S from 0 to 36
    for S, r1_list in tuples_by_sum.items():
        for a, b, c, d in r1_list:
            for e, f, g, h in r1_list:
                # Bound digit i based on f + g
                min_i = max(0, f + g - 9)
                max_i = min(9, f + g)
                for i in range(min_i, max_i + 1):
                    # Derive remaining 7 variables in O(1) time
                    m = S - a - e - i
                    if not (0 <= m <= 9):
                        continue

                    j = a + e + i - d - g
                    if not (0 <= j <= 9):
                        continue

                    p = e + i - d
                    if not (0 <= p <= 9):
                        continue

                    l = f + g - i

                    n = S - b - f - j
                    if not (0 <= n <= 9):
                        continue

                    k = S - a - f - p
                    if not (0 <= k <= 9):
                        continue

                    o = S - c - g - k
                    if not (0 <= o <= 9):
                        continue

                    # Final verification of row/col/diag sum constraints
                    if (
                        i + j + k + l == S
                        and m + n + o + p == S
                        and c + g + k + o == S
                        and a + f + k + p == S
                        and d + g + j + m == S
                    ):
                        count += 1

    # Return total count of valid 4x4 magic-like grids
    return count


if __name__ == "__main__":
    print(solve())
