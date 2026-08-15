"""Project Euler Problem 354: Distances in a Bee's Honeycomb.

Find the number of L <= 5 * 10^11 such that B(L) = 450.
"""

import math


def solve(limit_l: int = 500000000000, target_b: int = 450) -> int:
    """Count L <= limit_l such that B(L) == target_b on the honeycomb lattice."""
    n_max = (limit_l * limit_l) // 3

    # Smallest N0 is 7^4 * 13^4 * 19^2 = 24754593841
    min_n0 = 7**4 * 13**4 * 19**2
    m_max = int(math.isqrt(n_max // min_n0)) + 100

    # Max prime == 1 mod 3 needed in N0
    max_p = int(math.isqrt(n_max // (7**4 * 13**4))) + 1000

    # Sieve primes up to max_p
    p_sieve = bytearray([1]) * (max_p + 1)
    p_sieve[0] = p_sieve[1] = 0
    for i in range(2, int(math.isqrt(max_p)) + 1):
        if p_sieve[i]:
            p_sieve[i * i : max_p + 1 : i] = bytearray(len(range(i * i, max_p + 1, i)))

    p1_list = [p for p in range(7, max_p + 1) if p_sieve[p] and p % 3 == 1]

    # Precompute F(X): count of integers <= X whose prime factors are all == 2 mod 3
    valid_m = bytearray([1]) * (m_max + 1)
    valid_m[0] = 0
    valid_m[3 : m_max + 1 : 3] = bytearray(len(range(3, m_max + 1, 3)))
    for p in p1_list:
        if p > m_max:
            break
        valid_m[p : m_max + 1 : p] = bytearray(len(range(p, m_max + 1, p)))

    f_prefix = [0] * (m_max + 1)
    running = 0
    for i in range(1, m_max + 1):
        if valid_m[i]:
            running += 1
        f_prefix[i] = running

    def count_for_n0(n0: int) -> int:
        cnt = 0
        cur = n0
        while cur <= n_max:
            limit = math.isqrt(n_max // cur)
            cnt += f_prefix[limit]
            cur *= 3
        return cnt

    total_count = 0

    # Case 1: p1^74 - 7^74 > n_max (0 candidates)

    # Case 2: p1^24 * p2^2 (p1 != p2)
    for p1 in p1_list:
        p1_24 = p1**24
        if p1_24 > n_max:
            break
        for p2 in p1_list:
            if p1 == p2:
                continue
            n0 = p1_24 * (p2**2)
            if n0 > n_max:
                break
            total_count += count_for_n0(n0)

    # Case 3: p1^14 * p2^4 (p1 != p2)
    for p1 in p1_list:
        p1_14 = p1**14
        if p1_14 > n_max:
            break
        for p2 in p1_list:
            if p1 == p2:
                continue
            n0 = p1_14 * (p2**4)
            if n0 > n_max:
                break
            total_count += count_for_n0(n0)

    # Case 4: p1^4 * p2^4 * p3^2 (p1, p2, p3 distinct, p1 < p2)
    for i in range(len(p1_list)):
        p1 = p1_list[i]
        p1_4 = p1**4
        if p1_4 * (p1_list[i + 1] ** 4) * (7**2) > n_max:
            break
        for j in range(i + 1, len(p1_list)):
            p2 = p1_list[j]
            p12 = p1_4 * (p2**4)
            if p12 * (7**2) > n_max:
                break
            for p3 in p1_list:
                if p3 == p1 or p3 == p2:
                    continue
                n0 = p12 * (p3**2)
                if n0 > n_max:
                    break
                total_count += count_for_n0(n0)

    return total_count


if __name__ == "__main__":
    print(solve())
