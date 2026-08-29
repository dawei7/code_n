"""Project Euler Problem 479: Roots on the Rise.

Find S(10^6) mod 1_000_000_007, where S(n) = sum_{p=1..n} sum_{k=1..n} (a_k+b_k)^p (b_k+c_k)^p (c_k+a_k)^p
for the roots a_k, b_k, c_k of 1/x = (k/x)^2 (k + x^2) - kx.
"""

MOD = 1_000_000_007


def solve(n: int = 10**6, mod: int = MOD) -> int:
    """Compute S(n) mod mod using Vieta's identity (a+b)(b+c)(c+a) = 1 - k^2 and geometric series."""
    total = 0
    for k in range(2, n + 1):
        t_val = (1 - k * k) % mod
        geom = (
            t_val
            * (pow(t_val, n, mod) - 1)
            % mod
            * pow(t_val - 1, mod - 2, mod)
            % mod
        )
        total = (total + geom) % mod

    return total


if __name__ == "__main__":
    print(solve())
