"""Project Euler Problem 711: Binary Blackboard.

Find S(12345678) mod 1000000007, where S(N) is the sum of all n <= 2^N for which Eric
(the second player) can guarantee winning in the binary blackboard game.
"""

_MOD = 1_000_000_007
_INV3 = pow(3, _MOD - 2, _MOD)
_INV7 = pow(7, _MOD - 2, _MOD)


def solve(n: int = 12_345_678) -> int:
    """Compute S(N) modulo 1000000007 using base-4 combinatorial sum reduction."""
    if n % 2 == 0:
        m = n // 2
        k_bound = m - 1
        a_pow8 = (pow(8, m, _MOD) - 1) * _INV7 % _MOD if m > 0 else 0
        pow4m = pow(4, m, _MOD)
        b = ((pow(4, m + 1, _MOD) - 4) * _INV3 - m) % _MOD
    else:
        m = (n - 1) // 2
        k_bound = m
        a_pow8 = (pow(8, m + 1, _MOD) - 1) * _INV7 % _MOD
        pow4m = 0
        b = ((pow(4, m + 1, _MOD) - 4) * _INV3 - m) % _MOD

    t = 0
    s = 0
    pow2 = 1
    pow4 = 1

    for _ in range(k_bound):
        add = (pow2 + 2) * pow4 % _MOD
        t = (t + t + add) % _MOD
        s += t
        if s >= _MOD:
            s -= _MOD
        pow2 = (pow2 + pow2) % _MOD
        pow4 = (pow4 * 4) % _MOD

    a = (a_pow8 + s) % _MOD
    return (a + pow4m + b) % _MOD


if __name__ == "__main__":
    print(solve())
