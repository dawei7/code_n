def solve(n: int = 47, mod: int = 3**15) -> int:
    """Find T(n) mod 3^15, the sum of all balanced numbers less than 10^n.
    
    Time Complexity: O(n * (n * 9))
    Space Complexity: O(n^2)
    """
    max_m = (n + 1) // 2
    max_sum = max_m * 9

    count = [[[0] * 2 for _ in range(max_sum + 1)] for _ in range(max_m + 1)]
    val_sum = [[[0] * 2 for _ in range(max_sum + 1)] for _ in range(max_m + 1)]

    count[0][0][0] = 1
    count[0][0][1] = 1

    pow10 = [1] * (max_m + 2)
    for i in range(1, max_m + 2):
        pow10[i] = (pow10[i - 1] * 10) % mod

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
                        v_added = (d * pow10[L - 1] % mod * prev_c + prev_v) % mod
                        v_total = (v_total + v_added) % mod
                count[L][s][az] = c_total
                val_sum[L][s][az] = v_total

    total_ans = 0

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
            if k == 1:
                total_ans = (total_ans + 45) % mod
            else:
                m_sub = m - 1
                p10_m = pow10[m]
                p10_mid = pow10[m - 1]
                for s in range(m_sub * 9 + 1):
                    cA = count[m_sub][s][0]
                    vA = val_sum[m_sub][s][0]
                    cB = count[m_sub][s][1]
                    vB = val_sum[m_sub][s][1]
                    if cA > 0 and cB > 0:
                        base = (vA * p10_m % mod * cB + vB * cA) % mod
                        mid = (45 * p10_mid % mod * cA % mod * cB) % mod
                        term = (10 * base + mid) % mod
                        total_ans = (total_ans + term) % mod

    return total_ans
