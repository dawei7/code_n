"""Project Euler Problem 530: GCD of Divisors.

Find F(10^15), where F(k) = sum_{n=1..k} sum_{d|n} gcd(d, n/d).
"""

from array import array
from math import isqrt
from typing import Dict, List, Tuple


def _sieve_phi_tau(n: int) -> Tuple[array, array]:
    phi = array("I", [0]) * (n + 1)
    tau = array("H", [0]) * (n + 1)
    lp = array("I", [0]) * (n + 1)
    exp = array("B", [0]) * (n + 1)
    primes: List[int] = []

    phi[1] = 1
    tau[1] = 1

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            phi[i] = i - 1
            tau[i] = 2
            exp[i] = 1

        for p in primes:
            ip = i * p
            if ip > n:
                break
            lp[ip] = p
            if i % p == 0:
                phi[ip] = phi[i] * p
                e = exp[i] + 1
                exp[ip] = e
                tau[ip] = (tau[i] // (exp[i] + 1)) * (e + 1)
                break
            else:
                phi[ip] = phi[i] * (p - 1)
                exp[ip] = 1
                tau[ip] = tau[i] * 2

    return phi, tau


def _divisor_summatory(n: int) -> int:
    s = isqrt(n)
    acc = 0
    for i in range(1, s + 1):
        acc += n // i
    return 2 * acc - s * s


def solve(limit_n: int = 10**15) -> int:
    """Compute F(N) using Dirichlet hyperbola method on Dirichlet convolution f = tau * b (where b(k^2) = phi(k))."""
    if limit_n <= 0:
        return 0

    k = isqrt(limit_n)
    l = limit_n // k
    tmax = isqrt(l)

    phi, tau = _sieve_phi_tau(k)

    phi_prefix = array("Q", [0]) * (k + 1)
    running = 0
    for i in range(1, k + 1):
        running += phi[i]
        phi_prefix[i] = running

    phi_small = [0] * (tmax + 1)
    for t in range(1, tmax + 1):
        phi_small[t] = phi[t]
    del phi

    sum1 = 0
    sum_tau = 0
    for i in range(1, k + 1):
        ti = tau[i]
        sum_tau += ti
        m = isqrt(limit_n // i)
        sum1 += ti * phi_prefix[m]

    cache: Dict[int, int] = {k: sum_tau}

    def d_func(x: int) -> int:
        v = cache.get(x)
        if v is not None:
            return v
        v = _divisor_summatory(x)
        cache[x] = v
        return v

    sum2 = 0
    for t in range(1, tmax + 1):
        sum2 += phi_small[t] * d_func(limit_n // (t * t))

    result = sum1 + sum2 - sum_tau * phi_prefix[tmax]
    return result


if __name__ == "__main__":
    print(solve())
