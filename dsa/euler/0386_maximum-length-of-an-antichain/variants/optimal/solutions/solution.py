"""Project Euler Problem 386: Maximum Length of an Antichain.

Find sum_{n=1..10^8} N(n), where N(n) is the maximum length of an antichain of the divisor poset
of n.
"""

from array import array
from bisect import bisect_left
from functools import lru_cache
from math import isqrt
from typing import Dict, List, Set, Tuple


def _prime_sieve(n_val: int) -> Tuple[array, array]:
    """Return (primes, pi_small) up to n_val using an odd-only sieve."""
    if n_val < 2:
        return array("I"), array("I", [0]) * (n_val + 1)

    size = n_val // 2
    sieve = bytearray(b"\x01") * size
    sieve[0] = 0

    r = isqrt(n_val)
    for p in range(3, r + 1, 2):
        if sieve[p // 2]:
            start = p * p
            step = 2 * p
            sieve[start // 2 :: p] = b"\x00" * (((n_val - start) // step) + 1)

    primes = array("I", [2])
    for i in range(1, size):
        if sieve[i]:
            primes.append(2 * i + 1)

    pi_small = array("I", [0]) * (n_val + 1)
    cnt = 0
    for x in range(2, n_val + 1):
        if x == 2:
            cnt = 1
        elif (x & 1) and sieve[x // 2]:
            cnt += 1
        pi_small[x] = cnt
    return primes, pi_small


def iroot(n_val: int, k_val: int) -> int:
    """Return floor(n_val^(1/k_val))."""
    if k_val <= 1 or n_val < 2:
        return n_val
    if k_val == 2:
        return isqrt(n_val)
    x = int(n_val ** (1.0 / k_val))
    while (x + 1) ** k_val <= n_val:
        x += 1
    while x**k_val > n_val:
        x -= 1
    return x


def antichain_width(exps: Tuple[int, ...]) -> int:
    """Compute max coefficient of prod (1 + x + ... + x^{a_i}) via polynomial convolution DP."""
    if not exps:
        return 1
    dp = [1]
    for a in exps:
        new = [0] * (len(dp) + a)
        window = 0
        for k in range(len(new)):
            if k < len(dp):
                window += dp[k]
            if k - (a + 1) >= 0:
                window -= dp[k - (a + 1)]
            new[k] = window
        dp = new
    return max(dp)


def solve(limit: int = 100_000_000) -> int:
    """Compute sum_{n=1..limit} N(n) using prime pattern factorization and Lehmer pi counting."""
    sieve_max = 1_000_000
    primes, pi_small = _prime_sieve(sieve_max)

    phi_cache: Dict[Tuple[int, int], int] = {}

    def phi(x: int, s: int) -> int:
        if s == 0:
            return x
        if s == 1:
            return x - (x // 2)
        if x < 200_000 and s < 100:
            key = (x, s)
            if key in phi_cache:
                return phi_cache[key]
            v = phi(x, s - 1) - phi(x // primes[s - 1], s - 1)
            phi_cache[key] = v
            return v
        return phi(x, s - 1) - phi(x // primes[s - 1], s - 1)

    @lru_cache(maxsize=None)
    def lehmer_pi(x: int) -> int:
        if x <= sieve_max:
            return pi_small[x]
        a = lehmer_pi(iroot(x, 4))
        b = lehmer_pi(isqrt(x))
        c = lehmer_pi(iroot(x, 3))
        res = phi(x, a) + (b + a - 2) * (b - a + 1) // 2
        for i in range(a + 1, b + 1):
            p = primes[i - 1]
            w = x // p
            res -= lehmer_pi(w)
            if i <= c:
                lim = lehmer_pi(isqrt(w))
                for j in range(i, lim + 1):
                    res -= lehmer_pi(w // primes[j - 1]) - (j - 1)
        return res

    def pi_count(x: int) -> int:
        if x <= 1:
            return 0
        if x <= sieve_max:
            return pi_small[x]
        return lehmer_pi(x)

    def generate_patterns(lim: int) -> List[Tuple[int, ...]]:
        base_primes = [int(p) for p in primes[:15]]
        patterns: Set[Tuple[int, ...]] = set()

        def dfs(
            idx_prime: int, last_exp: int, cur_val: int, exps: List[int]
        ) -> None:
            patterns.add(tuple(exps))
            if idx_prime >= len(base_primes):
                return
            p = base_primes[idx_prime]
            for e in range(1, last_exp + 1):
                nxt = cur_val * (p**e)
                if nxt > lim:
                    break
                exps.append(e)
                dfs(idx_prime + 1, e, nxt, exps)
                exps.pop()

        dfs(0, 60, 1, [])
        patterns.discard(())
        return sorted(patterns, key=lambda t: (len(t), t))

    def minimal_product(exps: Tuple[int, ...], excluded: Set[int]) -> int:
        prod = 1
        idx = 0
        for e in exps:
            while idx < len(primes) and int(primes[idx]) in excluded:
                idx += 1
            if idx >= len(primes):
                return 10**30
            prod *= int(primes[idx]) ** e
            idx += 1
        return prod

    def count_numbers_for_pattern(exps: Tuple[int, ...], lim: int) -> int:
        r = len(exps)
        if r == 0:
            return 1
        if r == 1:
            return pi_count(iroot(lim, exps[0]))

        exps = tuple(sorted(exps, reverse=True))
        used: List[int] = []
        used_set: Set[int] = set()

        def rec(pos: int, curr_lim: int, last_in_group: int) -> int:
            if pos == r - 1:
                e = exps[pos]
                lo = (
                    last_in_group
                    if (pos > 0 and exps[pos] == exps[pos - 1])
                    else 1
                )
                max_p = iroot(curr_lim, e)
                if max_p <= lo:
                    return 0
                cnt = pi_count(max_p) - pi_count(lo)
                for u in used:
                    if lo < u <= max_p:
                        cnt -= 1
                return cnt

            e = exps[pos]
            rem_same = 1
            while pos + rem_same < r and exps[pos + rem_same] == e:
                rem_same += 1

            other_exps = exps[pos + rem_same :]
            min_other = minimal_product(other_exps, used_set)
            if min_other > curr_lim:
                return 0

            max_p = iroot(curr_lim // min_other, e * rem_same)
            start = (
                last_in_group + 1
                if (pos > 0 and exps[pos] == exps[pos - 1])
                else 2
            )
            if start > max_p:
                return 0

            idx_start = bisect_left(primes, start)
            total = 0
            for i in range(idx_start, len(primes)):
                p = int(primes[i])
                if p > max_p:
                    break
                if p in used_set:
                    continue
                p_pow = p**e
                if p_pow > curr_lim:
                    break

                min_rest = minimal_product(exps[pos + 1 :], used_set | {p})
                if p_pow * min_rest > curr_lim:
                    continue

                used.append(p)
                used_set.add(p)
                next_last = p if (pos + 1 < r and exps[pos + 1] == e) else 0
                total += rec(pos + 1, curr_lim // p_pow, next_last)
                used_set.remove(p)
                used.pop()

            return total

        return rec(0, lim, 0)

    total_antichain = 1  # n = 1, N(1) = 1
    for pattern in generate_patterns(limit):
        width = antichain_width(pattern)
        count = count_numbers_for_pattern(pattern, limit)
        total_antichain += width * count

    return total_antichain


if __name__ == "__main__":
    print(solve())
