"""Project Euler Problem 744: What? Where? When?.

Find f(10^11, 0.4999) rounded to 10 decimal places, where f(n, p) is the probability
that the game ends normally (the RED card is never drawn before reaching n points).
"""

from decimal import Decimal, getcontext
import math


def _normal_cdf(z: float) -> float:
    return 0.5 * math.erfc(-z / math.sqrt(2))


def _normal_sf(z: float) -> float:
    return 0.5 * math.erfc(z / math.sqrt(2))


def solve(n: int = 100_000_000_000, p_val: float = 0.4999) -> str:
    """Compute f(n, p) using regularized incomplete beta / normal CDF tail decomposition."""
    if n <= 20:
        getcontext().prec = 50
        p = Decimal(str(p_val))
        q = Decimal(1) - p
        total = Decimal(0)
        for k in range(n, 2 * n):
            comb = math.comb(k - 1, n - 1)
            prob = Decimal(comb) * (p**n * q ** (k - n) + q**n * p ** (k - n))
            factor = Decimal(2 * n + 1 - k) / Decimal(2 * n + 1)
            total += prob * factor
        return f"{total:.10f}"

    n2 = 2 * n
    mu = n2 * p_val
    sigma = math.sqrt(n2 * p_val * (1.0 - p_val))

    z_high = (n + 0.5 - mu) / sigma
    p_high = _normal_sf(z_high)

    z_low = (n - 0.5 - mu) / sigma
    p_low = _normal_cdf(z_low)

    term = (p_high / p_val) + (p_low / (1.0 - p_val))
    ans = 1.0 - (n / (2.0 * n + 1.0)) * term
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
