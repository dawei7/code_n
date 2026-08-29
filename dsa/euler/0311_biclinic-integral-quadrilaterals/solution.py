"""Project Euler 311: Biclinic Integral Quadrilaterals

Find B(10000000000), the number of distinct biclinic integral quadrilaterals ABCD
satisfying AB^2 + BC^2 + CD^2 + AD^2 <= 10^10.
"""

from __future__ import annotations

import bisect
import math


def solve(limit_n: int = 10_000_000_000) -> str:
    """Calculates B(limit_n) using Fermat's two-square representation theorem,

    combinatorial decomposition binom(M(n), 3), and prime power structure summation.
    """
    max_n = limit_n // 4  # 2,500,000,000

    # 1. Precompute primes == 1 mod 4 up to max_prime
    max_prime = 100_000_000
    sieve = [True] * (max_prime + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_prime)) + 1):
        if sieve[i]:
            sieve[i * i : max_prime + 1 : i] = [False] * len(
                sieve[i * i : max_prime + 1 : i]
            )
    primes1 = [i for i, is_p in enumerate(sieve) if is_p and i % 4 == 1]

    # 2. Precompute F(L): number of odd integers S <= L with all prime factors == 3 mod 4
    max_l = int(math.isqrt(max_n // 325)) + 100
    is_valid_s = [False] * (max_l + 1)
    for s in range(1, max_l + 1, 2):
        temp = s
        valid = True
        d = 3
        while d * d <= temp:
            if temp % d == 0:
                if d % 4 != 3:
                    valid = False
                    break
                while temp % d == 0:
                    temp //= d
            d += 2
        if temp > 1 and temp % 4 != 3:
            valid = False
        is_valid_s[s] = valid

    f_arr = [0] * (max_l + 1)
    for s in range(1, max_l + 1):
        f_arr[s] = f_arr[s - 1] + (1 if is_valid_s[s] else 0)

    # Helper to count (cnt_even, cnt_odd) for any K = max_n // P
    def get_cnt_as(k_val: int) -> tuple[int, int]:
        cnt_even = 0
        cnt_odd = 0
        a = 0
        pow2 = 1
        while pow2 <= k_val:
            l_val = int(math.isqrt(k_val // pow2))
            num_s = f_arr[l_val]
            if a % 2 == 0:
                cnt_even += num_s
            else:
                cnt_odd += num_s
            a += 1
            pow2 *= 2
        return cnt_even, cnt_odd

    # Precompute H(K) table
    max_k_table = 2_500_000
    h_table = [0] * (max_k_table + 1)
    for k_val in range(1, max_k_table + 1):
        ce, co = get_cnt_as(k_val)
        h_table[k_val] = ce + co

    def safe_h(k_val: int) -> int:
        if k_val <= max_k_table:
            return h_table[k_val]
        ce, co = get_cnt_as(k_val)
        return ce + co

    # Function to sum H(target // p) for p in (p_min, p_max]
    def sum_h_over_primes(
        p_min: int, p_max: int, target: int, exclude_p: int | None = None
    ) -> int:
        if p_min >= p_max:
            return 0
        res = 0
        cur_high = p_max
        for k_val in range(1, 101):
            cur_low = max(p_min, target // (k_val + 1))
            if cur_low >= cur_high:
                break
            idx_high = bisect.bisect_right(primes1, cur_high)
            idx_low = bisect.bisect_right(primes1, cur_low)
            num_p = idx_high - idx_low
            if exclude_p and cur_low < exclude_p <= cur_high:
                num_p -= 1
            if num_p > 0:
                res += safe_h(k_val) * num_p
            cur_high = cur_low
            if cur_high <= p_min:
                break
        if cur_high > p_min:
            idx_start = bisect.bisect_right(primes1, p_min)
            idx_end = bisect.bisect_right(primes1, cur_high)
            for k_idx in range(idx_start, idx_end):
                p = primes1[k_idx]
                if p != exclude_p:
                    res += safe_h(target // p)
        return res

    total_b = 0

    # 1. Triples p1 < p2 < p3 (D = 8, c = 4):
    for i in range(len(primes1)):
        p1 = primes1[i]
        if p1 * p1 * p1 > max_n:
            break
        for j in range(i + 1, len(primes1)):
            p2 = primes1[j]
            if p1 * p2 * p2 > max_n:
                break
            target = max_n // (p1 * p2)
            total_b += 4 * sum_h_over_primes(p2, target, target)

    # 2. Quads p1 < p2 < p3 < p4 (D = 16, c = 56):
    for i in range(len(primes1)):
        p1 = primes1[i]
        if p1**4 > max_n:
            break
        for j in range(i + 1, len(primes1)):
            p2 = primes1[j]
            if p1 * p2**3 > max_n:
                break
            for k in range(j + 1, len(primes1)):
                p3 = primes1[k]
                if p1 * p2 * p3**2 > max_n:
                    break
                target = max_n // (p1 * p2 * p3)
                total_b += 56 * sum_h_over_primes(p3, target, target)

    # 3. 5 distinct primes (D = 32, c = 560):
    for i in range(len(primes1)):
        p1 = primes1[i]
        if p1**5 > max_n:
            break
        for j in range(i + 1, len(primes1)):
            p2 = primes1[j]
            if p1 * p2**4 > max_n:
                break
            for k in range(j + 1, len(primes1)):
                p3 = primes1[k]
                if p1 * p2 * p3**3 > max_n:
                    break
                for l in range(k + 1, len(primes1)):
                    p4 = primes1[l]
                    if p1 * p2 * p3 * p4**2 > max_n:
                        break
                    target = max_n // (p1 * p2 * p3 * p4)
                    total_b += 560 * sum_h_over_primes(p4, target, target)

    # 4. Configurations p1^2 * p2 (D = 6, c = 1):
    for p1 in primes1:
        if p1 * p1 > max_n:
            break
        target = max_n // (p1 * p1)
        total_b += 1 * sum_h_over_primes(0, target, target, exclude_p=p1)

    # 5. Configurations p1^2 * p2 * p3 (D = 12, c = 20):
    for p1 in primes1:
        if p1 * p1 * 5 * 13 > max_n:
            break
        p1_sq = p1 * p1
        for j in range(len(primes1)):
            p2 = primes1[j]
            if p2 == p1:
                continue
            if p1_sq * p2 * p2 > max_n:
                break
            target = max_n // (p1_sq * p2)
            total_b += 20 * sum_h_over_primes(p2, target, target, exclude_p=p1)

    # 6. Configurations p1^2 * p2^2 (D = 9, c_even = 4, c_odd = 10):
    for i in range(len(primes1)):
        p1 = primes1[i]
        if p1**4 > max_n:
            break
        for j in range(i + 1, len(primes1)):
            p2 = primes1[j]
            if p1 * p1 * p2 * p2 > max_n:
                break
            ce, co = get_cnt_as(max_n // (p1 * p1 * p2 * p2))
            total_b += 4 * ce + 10 * co

    # 7. Configurations p1^3 * p2 (D = 8, c = 4):
    for p1 in primes1:
        if p1**3 * 5 > max_n:
            break
        target = max_n // (p1**3)
        total_b += 4 * sum_h_over_primes(0, target, target, exclude_p=p1)

    # 8. Configurations p1^4 * p2 (D = 10, c = 10):
    for p1 in primes1:
        if p1**4 * 5 > max_n:
            break
        target = max_n // (p1**4)
        total_b += 10 * sum_h_over_primes(0, target, target, exclude_p=p1)

    # 9. Configurations p1^2 * p2^2 * p3 (D = 18, c = 84):
    for i in range(len(primes1)):
        p1 = primes1[i]
        if p1**4 * 5 > max_n:
            break
        for j in range(i + 1, len(primes1)):
            p2 = primes1[j]
            if p1 * p1 * p2 * p2 * 5 > max_n:
                break
            target = max_n // (p1 * p1 * p2 * p2)
            total_b += 84 * sum_h_over_primes(0, target, target, exclude_p=p1)
            if p1 <= target:
                total_b -= 84 * safe_h(target // p1)
            if p2 <= target:
                total_b -= 84 * safe_h(target // p2)

    # 10. Configurations p1^2 * p2 * p3 * p4 (D = 24, c = 220):
    for p1 in primes1:
        if p1 * p1 * 5 * 13 * 17 > max_n:
            break
        p1_sq = p1 * p1
        for j in range(len(primes1)):
            p2 = primes1[j]
            if p2 == p1:
                continue
            if p1_sq * p2**3 > max_n:
                break
            for k in range(j + 1, len(primes1)):
                p3 = primes1[k]
                if p3 == p1:
                    continue
                if p1_sq * p2 * p3**2 > max_n:
                    break
                target = max_n // (p1_sq * p2 * p3)
                total_b += 220 * sum_h_over_primes(
                    p3, target, target, exclude_p=p1
                )

    # 11. Configurations p1^3 * p2 * p3 (D = 16, c = 56):
    for p1 in primes1:
        if p1**3 * 5 * 13 > max_n:
            break
        p1_cube = p1**3
        for j in range(len(primes1)):
            p2 = primes1[j]
            if p2 == p1:
                continue
            if p1_cube * p2 * p2 > max_n:
                break
            target = max_n // (p1_cube * p2)
            total_b += 56 * sum_h_over_primes(p2, target, target, exclude_p=p1)

    # 12. Single prime powers p1^k for k >= 5:
    for p1 in primes1:
        if p1**5 > max_n:
            break
        p_pow = p1**5
        k = 5
        while p_pow <= max_n:
            d_val = k + 1
            if k % 2 == 0:
                m_even = (d_val - 1) // 2
                c_even = (
                    m_even * (m_even - 1) * (m_even - 2) // 6
                    if m_even >= 3
                    else 0
                )
                m_odd = (d_val - 1) // 2
                c_odd = (
                    (m_odd + 1) * m_odd * (m_odd - 1) // 6
                    if m_odd + 1 >= 3
                    else 0
                )
                ce, co = get_cnt_as(max_n // p_pow)
                total_b += c_even * ce + c_odd * co
            else:
                m_val = d_val // 2
                c_val = (
                    m_val * (m_val - 1) * (m_val - 2) // 6 if m_val >= 3 else 0
                )
                ce, co = get_cnt_as(max_n // p_pow)
                total_b += c_val * (ce + co)
            k += 1
            p_pow *= p1

    return str(total_b)


if __name__ == "__main__":
    print(solve())
