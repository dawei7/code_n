"""Project Euler Problem 658: Incomplete Words II.

Find S(10^7, 10^12) mod 1000000007, where S(k, n) = sum_{alpha=1}^k I(alpha, n).
"""

from array import array

_MOD = 1_000_000_007


def solve(k: int = 10_000_000, n: int = 1_000_000_000_000) -> int:
    """Compute S(k, n) modulo 1000000007 using the binomial generating function hockey-stick reduction and linear multiplicative sieve."""
    if k <= 0:
        return 0

    limit = k - 1
    e = (n + 1) % (_MOD - 1)

    inv = array("I", [0]) * (k + 2)
    inv[1] = 1
    mmod = _MOD
    for i in range(2, k + 2):
        inv[i] = (mmod - (mmod // i) * inv[mmod % i] % mmod) % mmod

    spf = array("I", [0]) * (limit + 1)
    powe = array("I", [0]) * (limit + 1)
    powe[0] = 0
    if limit >= 1:
        powe[1] = 1

    primes = []
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            powe[i] = pow(i, e, mmod)
        pi = powe[i]
        si = spf[i]
        for p in primes:
            v = i * p
            if v > limit:
                break
            spf[v] = p
            powe[v] = (pi * powe[p]) % mmod
            if p == si:
                break

    inv2 = (mmod + 1) // 2
    inv2pow = inv2
    neg2 = mmod - 2
    k1 = k + 1
    s_sign = 1 if (k & 1) else (mmod - 1)

    term = 1
    t_sum = 1
    n1 = (n + 1) % mmod

    ans = 0
    for m in range(0, limit + 1):
        if m == 0:
            g_val = 1
        elif m == 1:
            g_val = n1
        else:
            g_val = ((powe[m] - 1) % mmod) * inv[m - 1] % mmod

        a_val = (1 - (inv2pow * ((1 - s_sign * t_sum) % mmod) % mmod)) % mmod
        ans = (ans + g_val * a_val) % mmod

        if m == limit:
            break

        term = term * (k1 - m) % mmod
        term = term * inv[m + 1] % mmod
        term = term * neg2 % mmod
        t_sum = (t_sum + term) % mmod

        inv2pow = (inv2pow * inv2) % mmod

    return ans


if __name__ == "__main__":
    print(solve())
