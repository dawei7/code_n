"""Project Euler Problem 522: Hilbert's Blackout.

Find F(12344321) mod 135707531, where F(n) is the sum of the minimum number
of floor rewirings needed to make every floor reachable from any starting floor.
"""

from array import array

MOD = 135707531


def solve(n: int = 12344321, mod: int = MOD) -> int:
    """Compute F(n) mod mod using linear component expectation on functional digraphs."""
    if n <= 2:
        return 0

    total_z = (n % mod) * ((n - 1) % mod) % mod
    total_z = total_z * pow(n - 2, n - 1, mod) % mod

    inv = array("I", [0]) * (n + 1)
    inv[1] = 1
    fact_n = 1
    for i in range(2, n + 1):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod
        fact_n = (fact_n * i) % mod

    inv_fact = 1
    s_sum = 0

    for m in range(1, n - 1):
        inv_fact = (inv_fact * inv[m]) % mod
        if m >= 2:
            term = pow(m - 1, m, mod)
            term = (term * inv_fact) % mod
            term = (term * inv[n - m]) % mod
            s_sum = (s_sum + term) % mod

    extra_p = (fact_n * s_sum) % mod
    return (total_z + extra_p) % mod


if __name__ == "__main__":
    print(solve())
