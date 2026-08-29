def solve(n: int = 47, mod: int = 3**15) -> int:
    """Find T(47) mod 3^15, the sum of all balanced numbers less than 10^47.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Balanced Numbers Definition:
       A k-digit integer is balanced if the sum of its first ceil(k/2) digits equals the sum
       of its last ceil(k/2) digits.
       - For even k = 2m: first m digits sum == last m digits sum.
       - For odd k = 2m - 1: first m-1 digits sum == last m-1 digits sum (middle digit is any 0..9).

    2. Digit Dynamic Programming for Half-Block Counts & Values:
       Let count[L][s][allow_zero] be the number of L-digit strings summing to s.
       Let val_sum[L][s][allow_zero] be the sum of numerical values of these L-digit strings modulo 3^15.
       State transitions:
           count[L][s] = sum_d count[L-1][s-d]
           val_sum[L][s] = sum_d (d * 10^(L-1) * count[L-1][s-d] + val_sum[L-1][s-d]).

    3. Combinatorial Product Assembly modulo 3^15:
       - For even k = 2m: Left block has no leading zero (allow_zero=0), Right block allows leading zero.
         Combined value = Left * 10^m + Right.
       - For odd k = 2m - 1: Combine (m-1)-digit Left and Right blocks with 10 middle digits (0..9).
       Summing T(47) mod 3^15 across all lengths k = 1..47 executes in ~0.01s.

    Complexity:
    -----------
    - Time Complexity: O(n^2 * 10) operations (~0.01s for n = 47).
    - Space Complexity: O(n^2) auxiliary DP table (~1 MB).
    """
    max_m = (n + 1) // 2
    max_sum = max_m * 9

    # DP tables for digit counts and value sums
    count = [[[0] * 2 for _ in range(max_sum + 1)] for _ in range(max_m + 1)]
    val_sum = [[[0] * 2 for _ in range(max_sum + 1)] for _ in range(max_m + 1)]

    count[0][0][0] = 1
    count[0][0][1] = 1

    # Precompute powers of 10 mod 3^15
    pow10 = [1] * (max_m + 2)
    for i in range(1, max_m + 2):
        pow10[i] = (pow10[i - 1] * 10) % mod

    # Fill half-block DP tables up to length max_m
    for L in range(1, max_m + 1):
        for s in range(L * 9 + 1):
            for az in (0, 1):
                min_d = 0 if az else 1
                c_total = 0
                v_total = 0
                for d in range(min_d, 10):
                    if s >= d:
                        prev_c = count[L - 1][s - d][1]
                        prev_v = val_sum[L - 1][s - d][1]
                        c_total = (c_total + prev_c) % mod
                        v_added = (
                            d * pow10[L - 1] % mod * prev_c + prev_v
                        ) % mod
                        v_total = (v_total + v_added) % mod
                count[L][s][az] = c_total
                val_sum[L][s][az] = v_total

    total_ans = 0
    sum_digits = sum(range(1, 10))

    # Assemble balanced numbers for each length k from 1 to n
    for k in range(1, n + 1):
        m = (k + 1) // 2
        if k % 2 == 0:
            p10 = pow10[m]
            for s in range(m * 9 + 1):
                cA = count[m][s][0]
                vA = val_sum[m][s][0]
                cB = count[m][s][1]
                vB = val_sum[m][s][1]
                if cA > 0 and cB > 0:
                    term = (vA * p10 % mod * cB + vB * cA) % mod
                    total_ans = (total_ans + term) % mod
        else:
            m_sub = m - 1
            p10_m = pow10[m]
            p10_mid = pow10[m - 1]
            if m_sub == 0:
                total_ans = (total_ans + sum_digits) % mod
            else:
                for s in range(m_sub * 9 + 1):
                    cA = count[m_sub][s][0]
                    vA = val_sum[m_sub][s][0]
                    cB = count[m_sub][s][1]
                    vB = val_sum[m_sub][s][1]
                    if cA > 0 and cB > 0:
                        base = (vA * p10_m % mod * cB + vB * cA) % mod
                        mid = (sum_digits * p10_mid % mod * cA % mod * cB) % mod
                        term = (10 * base + mid) % mod
                        total_ans = (total_ans + term) % mod

    # Return total sum T(47) mod 3^15
    return total_ans


if __name__ == "__main__":
    print(solve())
