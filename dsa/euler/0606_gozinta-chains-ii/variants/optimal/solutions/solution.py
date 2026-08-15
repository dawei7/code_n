"""Project Euler Problem 606: Gozinta Chains II.

Find the last nine digits of S(10^36), where S(n) is the sum of all numbers k <= n
that have exactly 252 distinct gozinta chains.
"""

from typing import List, Tuple

_MOD = 1_000_000_000


def _isqrt(n: int) -> int:
    x = int(n**0.5)
    while (x + 1) * (x + 1) <= n:
        x += 1
    while x * x > n:
        x -= 1
    return x


def _icbrt(n: int) -> int:
    lo, hi = 0, 1
    while hi * hi * hi <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid * mid <= n:
            lo = mid
        else:
            hi = mid
    return lo


def _sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    bs = bytearray(b"\x01") * (limit + 1)
    bs[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if bs[p]:
            step = p
            start = p * p
            bs[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
        p += 1
    return [i for i in range(limit + 1) if bs[i]]


def _prime_cube_sums_lucy(
    n: int, primes: List[int], mod: int
) -> Tuple[List[int], List[int]]:
    r = _isqrt(n)
    v_keys = [n // i for i in range(1, r + 1)]
    last = v_keys[-1]
    for v in range(last - 1, 0, -1):
        v_keys.append(v)
    l_len = len(v_keys)

    s_arr = [0] * l_len
    for i, v in enumerate(v_keys):
        t = (v * (v + 1) // 2) % mod
        s_arr[i] = (t * t - 1) % mod

    def idx_small(x: int) -> int:
        return l_len - x

    for p in primes:
        p2 = p * p
        if p2 > n:
            break
        p3 = (p * p % mod) * p % mod
        sp = 0 if p == 2 else s_arr[idx_small(p - 1)]

        big_len = min(n // p2, r)
        for i in range(big_len):
            v = v_keys[i]
            denom_u = (i + 1) * p
            if denom_u <= r:
                su = s_arr[denom_u - 1]
            else:
                su = s_arr[idx_small(v // p)]
            diff = (su - sp) % mod
            s_arr[i] = (s_arr[i] - p3 * diff) % mod

        small_len = r - p2
        if small_len > 0:
            start = r
            end = r + small_len
            for j in range(start, end):
                v = v_keys[j]
                su = s_arr[idx_small(v // p)]
                diff = (su - sp) % mod
                s_arr[j] = (s_arr[j] - p3 * diff) % mod

    return v_keys, s_arr


def solve(n: int = 10**36) -> str:
    """Compute last 9 digits of S(n) using semiprime cube reduction and Lucy-Hedgehog cubic prime summatory sieve."""
    m = _icbrt(n)
    r = _isqrt(m)
    primes = _sieve_primes(r)

    v_keys, s_arr = _prime_cube_sums_lucy(m, primes, _MOD)
    l_len = len(v_keys)

    def idx_small(x: int) -> int:
        return l_len - x

    total = 0
    for p in primes:
        if m // p <= p:
            break
        sum_up_to_qmax = s_arr[p - 1]
        sum_up_to_p = s_arr[idx_small(p)]
        sum_q = (sum_up_to_qmax - sum_up_to_p) % _MOD
        p3 = (p * p % _MOD) * p % _MOD
        total = (total + p3 * sum_q) % _MOD

    digits = [(total // (10**i)) % 10 for i in range(8, -1, -1)]
    return "".join(str(d) for d in digits)


if __name__ == "__main__":
    print(solve())
