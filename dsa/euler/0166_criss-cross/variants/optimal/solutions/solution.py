def solve() -> int:
    """Find number of ways to fill 4x4 grid with digits 0-9 such that rows, cols, diagonals sum to same value.
    
    Time Complexity: O(Sum_S |Tuples(S)|^2 * Bounded_i)
    Space Complexity: O(10^4)
    """
    tuples_by_sum = {}
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    tuples_by_sum.setdefault(a + b + c + d, []).append((a, b, c, d))

    count = 0

    for S, r1_list in tuples_by_sum.items():
        for (a, b, c, d) in r1_list:
            for (e, f, g, h) in r1_list:
                min_i = max(0, f + g - 9)
                max_i = min(9, f + g)
                for i in range(min_i, max_i + 1):
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

                    if (i + j + k + l == S and
                        m + n + o + p == S and
                        c + g + k + o == S and
                        a + f + k + p == S and
                        d + g + j + m == S):
                        count += 1

    return count
