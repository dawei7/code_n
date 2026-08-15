"""Project Euler Problem 731: A Stoneham Number.

Find A(10^16), the 10 decimal digits starting from the (10^16)-th digit of
A = sum_{i=1}^inf 1 / (3^i * 10^(3^i)).
"""

from decimal import Decimal, getcontext


def solve(n: int = 10_000_000_000_000_000) -> str:
    """Compute A(n) using BBP-style modular exponentiation on the Stoneham constant series."""
    getcontext().prec = 100
    frac = Decimal(0)

    i = 1
    while True:
        pow3 = 3**i
        if pow3 <= n - 1:
            exp = n - 1 - pow3
            rem = pow(10, exp, pow3)
            frac += Decimal(rem) / Decimal(pow3)
        else:
            diff = pow3 - (n - 1)
            if diff > 60:
                break
            term = Decimal(1) / (Decimal(pow3) * (Decimal(10) ** diff))
            frac += term
        i += 1

    frac = frac - int(frac)
    digits = int(frac * Decimal(10**10))
    return f"{digits:010d}"


if __name__ == "__main__":
    print(solve())
