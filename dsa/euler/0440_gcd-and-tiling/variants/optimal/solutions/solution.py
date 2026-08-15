"""Project Euler Problem 440: GCD and Tiling.

Find S(2000) mod 987898789, where S(L) = sum_{a,b,c <= L} gcd(T(c^a), T(c^b))
and T(n) is the number of tilings of a 1 x n board with 1x2 and 1x1 blocks.
"""

from typing import List, Tuple

MOD = 987_898_789
P = 10


def _mobius_upto(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: List[int] = []
    is_comp = [False] * (n + 1)

    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            is_comp[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]
    return mu


def _counts_n_and_rest(l_val: int) -> Tuple[List[int], int]:
    mu = _mobius_upto(l_val)
    f = [0] * (l_val + 1)
    for n in range(1, l_val + 1):
        s = 0
        for d in range(1, n + 1, 2):
            md = mu[d]
            if md:
                t = (n // d + 1) // 2
                s += md * t * t
        f[n] = s

    n_arr = [0] * (l_val + 1)
    sum_n = 0
    for g in range(1, l_val + 1):
        v = f[l_val // g]
        n_arr[g] = v
        sum_n += v

    rest = l_val * l_val - sum_n
    return n_arr, rest


def _u_small_mod_upto(l_val: int, mod: int) -> List[int]:
    u = [0] * (l_val + 2)
    u[0] = 0
    u[1] = 1
    for i in range(2, l_val + 2):
        u[i] = (P * u[i - 1] + u[i - 2]) % mod
    return u


def _mul_pair(
    a0: int, a1: int, b0: int, b1: int, mod: int
) -> Tuple[int, int]:
    t = (b1 - P * b0) % mod
    w0 = (a1 * b0 + a0 * t) % mod
    w1 = (a1 * b1 + a0 * b0) % mod
    return w0, w1


def _sq_pair(a0: int, a1: int, mod: int) -> Tuple[int, int]:
    v = (2 * a1 - P * a0) % mod
    w0 = (a0 * v) % mod
    w1 = (a1 * a1 + a0 * a0) % mod
    return w0, w1


def _pow_pair_by_bits(
    base0: int, base1: int, bits_lsb_to_msb: List[int], mod: int
) -> Tuple[int, int]:
    r0, r1 = 0, 1
    b0, b1 = base0, base1
    last = len(bits_lsb_to_msb) - 1

    for i, bit in enumerate(bits_lsb_to_msb):
        if bit:
            r0, r1 = _mul_pair(r0, r1, b0, b1, mod)
        if i != last:
            b0, b1 = _sq_pair(b0, b1, mod)
    return r0, r1


def solve(l_limit: int = 2000, mod: int = MOD) -> int:
    """Compute S(l_limit) mod mod using Lucas sequence strong divisibility and fast matrix power steps."""
    n_arr, rest = _counts_n_and_rest(l_limit)
    u_small = _u_small_mod_upto(l_limit, mod)

    n_mod = [0] * (l_limit + 1)
    for g in range(1, l_limit + 1):
        n_mod[g] = n_arr[g] % mod

    rest_mod = rest % mod
    u2 = u_small[2]

    total = 0
    for c in range(1, l_limit + 1):
        bits: List[int] = []
        x = c
        while x > 0:
            bits.append(x & 1)
            x >>= 1

        pair0, pair1 = u_small[c], u_small[c + 1]
        small = 1 if (c & 1) == 0 else u2
        contrib = (rest_mod * small) % mod

        for g in range(1, l_limit + 1):
            contrib = (contrib + n_mod[g] * pair1) % mod
            pair0, pair1 = _pow_pair_by_bits(pair0, pair1, bits, mod)

        total = (total + contrib) % mod

    return total


if __name__ == "__main__":
    print(solve())
