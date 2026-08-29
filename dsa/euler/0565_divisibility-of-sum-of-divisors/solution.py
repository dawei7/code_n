"""Project Euler Problem 565: Divisibility of Sum of Divisors.

Find S(10^11, 2017), where S(n, d) is the sum of integers i <= n such that d | sigma(i).
"""

import bisect
import math
from typing import List, Tuple


def _triangular(n: int) -> int:
    return n * (n + 1) // 2


def _prime_factors(n: int) -> List[int]:
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def _primes_upto(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * ((limit - start) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def _multiplicative_order(
    base: int, modulo: int, order_factors: List[int]
) -> int:
    order = modulo - 1
    residue = base % modulo
    for factor in order_factors:
        while order % factor == 0 and pow(residue, order // factor, modulo) == 1:
            order //= factor
    return order


def _minus_one_primes(
    limit: int, modulo: int, small_primes: List[int]
) -> List[int]:
    max_k = (limit + 1) // modulo
    if max_k <= 0:
        return []
    sieve = bytearray(b"\x01") * (max_k + 1)
    sieve[0] = 0
    for p in small_primes:
        if p == modulo:
            continue
        residue = pow(modulo % p, -1, p)
        min_k = (p * p + 1 + modulo - 1) // modulo
        if residue < min_k:
            residue += ((min_k - residue + p - 1) // p) * p
        if residue <= max_k:
            sieve[residue::p] = b"\x00" * ((max_k - residue) // p + 1)
    return [modulo * k - 1 for k in range(1, max_k + 1) if sieve[k]]


def _trigger_powers(
    limit: int,
    modulo: int,
    small_primes: List[int],
    order_factors: List[int],
) -> List[Tuple[int, int]]:
    events = []
    for q in small_primes:
        if q == modulo:
            continue
        residue = q % modulo
        if residue == 1:
            continue
        order = _multiplicative_order(q, modulo, order_factors)
        power = 1
        exponent = 0
        while power <= limit // q:
            power *= q
            exponent += 1
            if (exponent + 1) % order == 0:
                if not (order == 2 and exponent == 1):
                    events.append((q, power))
    events.sort(key=lambda event: event[1])
    return events


def _single_event_sum(limit: int, q: int, q_power: int) -> int:
    m = limit // q_power
    return q_power * (_triangular(m) - q * _triangular(m // q))


def _pair_event_sum(
    limit: int,
    q: int,
    q_power: int,
    r: int,
    r_power: int,
) -> int:
    base = q_power * r_power
    m = limit // base
    return base * (
        _triangular(m)
        - q * _triangular(m // q)
        - r * _triangular(m // r)
        + q * r * _triangular(m // (q * r))
    )


def solve(limit: int = 100_000_000_000, modulo: int = 2017) -> int:
    """Compute S(limit, modulo) using arithmetic progression sieve and inclusion-exclusion."""
    small_primes = _primes_upto(math.isqrt(limit))
    order_factors = _prime_factors(modulo - 1)

    linear_events = _minus_one_primes(limit, modulo, small_primes)
    higher_events = _trigger_powers(
        limit, modulo, small_primes, order_factors
    )

    total = 0
    for q in linear_events:
        total += _single_event_sum(limit, q, q)
    for q, q_power in higher_events:
        total += _single_event_sum(limit, q, q_power)

    for i, q in enumerate(linear_events):
        if q * q > limit:
            break
        end = bisect.bisect_right(linear_events, limit // q)
        for r in linear_events[i + 1 : end]:
            total -= _pair_event_sum(limit, q, q, r, r)

    for q, q_power in higher_events:
        end = bisect.bisect_right(linear_events, limit // q_power)
        for r in linear_events[:end]:
            if r != q:
                total -= _pair_event_sum(limit, q, q_power, r, r)

    for i, (q, q_power) in enumerate(higher_events):
        if q_power * q_power > limit:
            break
        for r, r_power in higher_events[i + 1 :]:
            if q_power * r_power > limit:
                break
            if q != r:
                total -= _pair_event_sum(
                    limit, q, q_power, r, r_power
                )

    return total


if __name__ == "__main__":
    print(solve())
