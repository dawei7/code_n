"""Project Euler Problem 427: n-sequences.

Find f(7_500_000) mod 1_000_000_009, where f(n) is the sum of L(S) over all n-sequences S,
and L(S) is the length of the longest contiguous run of equal elements in S.
"""

from array import array

MOD = 1_000_000_009


def solve(n: int = 7_500_000, mod: int = MOD) -> int:
    """Compute f(n) mod mod using generating function closed-form coefficients and harmonic sum."""
    if n <= 0:
        return 0

    n_mod = n % mod
    a_mod = (1 - n_mod) % mod

    fac = array("I", [1]) * (n + 1)
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % mod

    ifac = array("I", [0]) * (n + 1)
    ifac[n] = pow(int(fac[n]), mod - 2, mod)
    for i in range(n, 0, -1):
        ifac[i - 1] = (ifac[i] * i) % mod

    a_arr = array("I", [0]) * (n + 1)
    b_arr = array("I", [0]) * (n + 1)
    pow_n = 1
    pow_a = 1
    for i in range(0, n + 1):
        if i == 0:
            pow_n = 1
            pow_a = 1
        else:
            pow_n = (pow_n * n_mod) % mod
            pow_a = (pow_a * a_mod) % mod
        a_arr[i] = (pow_n * ifac[i]) % mod
        b_arr[i] = (pow_a * ifac[i]) % mod

    del ifac

    sum_ak = 0
    fac_local = fac
    a_local = a_arr
    b_local = b_arr

    for k in range(2, n + 1):
        q = n // k
        km1 = k - 1

        m = n
        idx = n
        res = 0

        for t in range(q):
            bt = b_local[t]

            tmp = (fac_local[idx] * a_local[m]) % mod
            res += (tmp * bt) % mod

            tmp2 = (fac_local[idx - k] * a_local[m - k]) % mod
            res -= (tmp2 * bt) % mod

            m -= k
            idx -= km1

        tmp = (fac_local[idx] * a_local[m]) % mod
        res += (tmp * b_local[q]) % mod

        sum_ak += res % mod
        if (k & 1023) == 0:
            sum_ak %= mod

    sum_ak %= mod
    return (pow(n_mod, n + 1, mod) - sum_ak) % mod


if __name__ == "__main__":
    print(solve())
