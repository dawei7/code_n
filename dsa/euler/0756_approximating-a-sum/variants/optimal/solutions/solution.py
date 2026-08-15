"""Project Euler Problem 756: Approximating a Sum.

Find E(Delta | phi(k), 12345678, 12345) rounded to 6 places after the decimal point,
where Delta is the error of the random Riemann sum approximation.
"""

from array import array
import math


def _totients_up_to(n: int) -> array:
    phi = array("I", [0]) * (n + 1)
    if n >= 1:
        phi[1] = 1

    primes = []
    for i in range(2, n + 1):
        if phi[i] == 0:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            ip = i * p
            if ip > n:
                break
            if i % p == 0:
                phi[ip] = phi[i] * p
                break
            else:
                phi[ip] = phi[i] * (p - 1)
    return phi


def _cutoff_index(n: int, m: int, eps: float = 1e-10) -> int:
    limit = n - m
    if limit <= 0:
        return 0

    w = (n - m) / n
    for k in range(1, limit + 1):
        remaining = limit - k
        nk = n - k
        if nk <= m:
            w_next = 0.0
        else:
            w_next = w * (nk - m) / nk

        if n * remaining * w_next < eps:
            return k
        w = w_next

    return limit


def solve(n: int = 12_345_678, m: int = 12_345) -> str:
    """Compute E(Delta | phi(k), n, m) using hyper-geometric ratio weight recurrence."""
    limit = max(0, n - m)
    upto = min(limit, _cutoff_index(n, m))
    phi = _totients_up_to(upto)

    w = (n - m) / n if n > 0 else 0.0
    total = 0.0

    for k in range(1, upto + 1):
        total += float(phi[k]) * w
        nk = n - k
        if nk <= m:
            break
        w *= (nk - m) / nk

    return f"{total:.6f}"


if __name__ == "__main__":
    print(solve())
