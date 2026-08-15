"""Project Euler 272: Modular Cubes, Part 2

Find the sum of all positive integers n <= 10^11 for which C(n) = 242
(i.e. x^3 = 1 mod n has 243 = 3^5 solutions in 0 <= x < n).
"""

from __future__ import annotations


def solve(limit: int = 10**11) -> str:
    """Calculates the sum of all integers n <= limit having exactly 243 cube roots of unity mod n

    via segmented recursive tree enumeration over prime factors p = 1 mod 3 with multiplier prefix sums.
    """
    max_m = 250000
    max_p = max(int(limit / (9 * 7 * 13 * 19)) + 1000, max_m)

    # 1. Sieve prime numbers up to max_p
    sieve = [True] * (max_p + 1)
    for i in range(2, int(max_p**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_p + 1, i):
                sieve[j] = False

    primes_1mod3 = [
        p for p in range(7, max_p + 1) if sieve[p] and p % 3 == 1
    ]

    # 2. Sieve multipliers in [1, max_m]
    has_1mod3 = [False] * (max_m + 1)
    for p in primes_1mod3:
        if p <= max_m:
            for j in range(p, max_m + 1, p):
                has_1mod3[j] = True

    valid_c1 = [0] * (max_m + 1)
    valid_c2 = [0] * (max_m + 1)
    for x in range(1, max_m + 1):
        if not has_1mod3[x]:
            if x % 9 != 0:
                valid_c1[x] = x
            if x % 3 != 0:
                valid_c2[x] = x

    pref_c1 = [0] * (max_m + 1)
    pref_c2 = [0] * (max_m + 1)
    for x in range(1, max_m + 1):
        pref_c1[x] = pref_c1[x - 1] + valid_c1[x]
        pref_c2[x] = pref_c2[x - 1] + valid_c2[x]

    total_ans = 0

    # 3. Case 1: Exactly 5 distinct prime factors p = 1 mod 3, 9 does not divide n
    def dfs_c1(idx: int, count: int, curr_m: int) -> None:
        nonlocal total_ans
        if count == 5:
            m = limit // curr_m
            total_ans += curr_m * pref_c1[m]
            return

        rem = 5 - count
        for i in range(idx, len(primes_1mod3)):
            p = primes_1mod3[i]
            if rem == 1:
                if curr_m * p > limit:
                    break
            elif rem == 2:
                if curr_m * p * 7 > limit:
                    break
            elif rem == 3:
                if curr_m * p * 7 * 13 > limit:
                    break
            elif rem == 4:
                if curr_m * p * 7 * 13 * 19 > limit:
                    break
            elif rem == 5:
                if curr_m * p * 7 * 13 * 19 * 31 > limit:
                    break

            p_pow = p
            while curr_m * p_pow <= limit:
                dfs_c1(i + 1, count + 1, curr_m * p_pow)
                p_pow *= p

    dfs_c1(0, 0, 1)

    # 4. Case 2: Exactly 4 distinct prime factors p = 1 mod 3, and 9 divides n
    def dfs_c2(idx: int, count: int, curr_m: int) -> None:
        nonlocal total_ans
        if count == 4:
            m = limit // curr_m
            total_ans += curr_m * pref_c2[m]
            return

        rem = 4 - count
        for i in range(idx, len(primes_1mod3)):
            p = primes_1mod3[i]
            if rem == 1:
                if curr_m * p > limit:
                    break
            elif rem == 2:
                if curr_m * p * 7 > limit:
                    break
            elif rem == 3:
                if curr_m * p * 7 * 13 > limit:
                    break
            elif rem == 4:
                if curr_m * p * 7 * 13 * 19 > limit:
                    break

            p_pow = p
            while curr_m * p_pow <= limit:
                dfs_c2(i + 1, count + 1, curr_m * p_pow)
                p_pow *= p

    pow3 = 9
    while pow3 <= limit:
        dfs_c2(0, 0, pow3)
        pow3 *= 3

    return str(total_ans)


if __name__ == "__main__":
    print(solve())
