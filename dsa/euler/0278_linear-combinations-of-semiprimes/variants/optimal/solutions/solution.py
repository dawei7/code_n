"""Project Euler 278: Linear Combinations of Semiprimes

Find sum of f(p*q, p*r, q*r) for all prime triples p < q < r < 5000,
where f is the Frobenius number of the three pairwise products.
"""

from __future__ import annotations


def solve(limit: int = 5000) -> str:
    """Calculates the sum of Frobenius numbers f(pq, pr, qr) = 2pqr - pq - qr - rp across all prime

    triples p < q < r < limit using 1D middle-prime prefix/suffix factorization.
    """
    # 1. Sieve primes below limit
    sieve = [True] * limit
    primes: list[int] = []
    for i in range(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                sieve[j] = False

    n = len(primes)
    total_frobenius = 0

    # 2. Iterate over the middle prime q = primes[j]
    for j in range(1, n - 1):
        q = primes[j]
        left_p = primes[:j]
        right_r = primes[j + 1 :]

        sum_p = sum(left_p)
        count_p = len(left_p)

        sum_r = sum(right_r)
        count_r = len(right_r)

        # Closed-form expansion of 2pqr - pq - qr - rp:
        term_pqr = 2 * q * sum_p * sum_r
        term_pq = q * sum_p * count_r
        term_qr = q * count_p * sum_r
        term_pr = sum_p * sum_r

        total_frobenius += term_pqr - term_pq - term_qr - term_pr

    return str(total_frobenius)


if __name__ == "__main__":
    print(solve())
