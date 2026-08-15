"""Project Euler Problem 405: A Rectangular Tiling.

Find f(10^k) for k = 10^18 modulo 17^7, where f(n) is the number of 4-tile meeting points in T(n).
"""


def solve(k_val: int = 10**18) -> int:
    """Compute f(10^k_val) mod 17^7 using Euler totient modular reduction and closed form."""
    mod = 17**7
    phi = mod - mod // 17
    inv15 = pow(15, -1, mod)

    # Reduction of n = 10^(k_val) mod phi(17^7)
    n_mod_phi = 1
    cur = 10 % phi
    e = k_val
    while e > 0:
        if e & 1:
            n_mod_phi = (n_mod_phi * cur) % phi
        cur = (cur * cur) % phi
        e >>= 1

    p2 = pow(2, n_mod_phi, mod)
    p4 = pow(4, n_mod_phi, mod)
    sign = 1  # 10^k is even for k >= 1

    # f(n) = (6 * 4^n - 20 * 2^n + 15 - (-1)^n) / 15
    num = (6 * p4 - 20 * p2 + 15 - sign) % mod
    ans = (num * inv15) % mod

    return ans


if __name__ == "__main__":
    print(solve())
