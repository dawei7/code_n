"""Project Euler Problem 754: Product of Gauss Factorials.

Find G(10^8) modulo 1000000007, where G(n) = prod_{i=1}^n g(i) and g(i) is the Gauss
Factorial of i (product of positive integers <= i relatively prime to i).
"""

from typing import List, Tuple

_MOD = 1_000_000_007
_EXP_MOD = _MOD - 1


def _mobius_interval_aggregates(n: int) -> List[Tuple[int, int, int, int]]:
    mu = bytearray(n + 1)
    mu[1] = 1
    composite = bytearray(n + 1)
    primes: List[int] = []

    aggregates: List[Tuple[int, int, int, int]] = []
    lo = 1
    q = n
    hi = 1
    pos_product = 1
    neg_product = 1
    mu_sum = 1
    aggregates.append((q, pos_product, neg_product, mu_sum))

    lo = hi + 1
    if lo > n:
        return aggregates
    q = n // lo
    hi = n // q
    pos_product = 1
    neg_product = 1
    mu_sum = 0

    for x in range(2, n + 1):
        if not composite[x]:
            primes.append(x)
            mux = 2
            mu[x] = mux
        else:
            mux = mu[x]

        if mux == 1:
            pos_product = (pos_product * x) % _MOD
            mu_sum += 1
        elif mux == 2:
            neg_product = (neg_product * x) % _MOD
            mu_sum -= 1

        for p in primes:
            y = x * p
            if y > n:
                break
            composite[y] = 1
            if x % p == 0:
                break
            if mux == 1:
                mu[y] = 2
            elif mux == 2:
                mu[y] = 1

        if x == hi:
            aggregates.append((q, pos_product, neg_product, mu_sum))
            lo = hi + 1
            if lo > n:
                break
            q = n // lo
            hi = n // q
            pos_product = 1
            neg_product = 1
            mu_sum = 0

    return aggregates


def solve(limit: int = 100_000_000) -> int:
    """Compute G(limit) mod 1000000007 using Mobius quotient block aggregation."""
    aggregates = _mobius_interval_aggregates(limit)

    # Compute needed superfactorials
    keys = sorted({q - 1 for q, _, _, _ in aggregates if q > 1})
    superfactorial = {0: 1}
    pos = 0
    factorial = 1
    superfac = 1

    stop = keys[-1] if keys else 0
    for x in range(1, stop + 1):
        factorial = (factorial * x) % _MOD
        superfac = (superfac * factorial) % _MOD
        while pos < len(keys) and keys[pos] == x:
            superfactorial[x] = superfac
            pos += 1

    result = 1
    for q, pos_prod, neg_prod, mu_sum in aggregates:
        exponent = (q * (q - 1) // 2) % _EXP_MOD
        if exponent:
            result = (result * pow(pos_prod, exponent, _MOD)) % _MOD
            result = (result * pow(neg_prod, (-exponent) % _EXP_MOD, _MOD)) % _MOD

        sf_power = mu_sum % _EXP_MOD
        if sf_power and (q - 1) in superfactorial:
            result = (result * pow(superfactorial[q - 1], sf_power, _MOD)) % _MOD

    return result


if __name__ == "__main__":
    print(solve())
