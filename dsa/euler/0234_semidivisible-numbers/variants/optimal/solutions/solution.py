import math


def solve(limit: int = 999966663333) -> int:
    """Find the sum of all semidivisible numbers not exceeding limit.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Prime Square Intervals:
       For any non-square integer n in (p1^2, p2^2) where p1, p2 are consecutive primes:
           lps(n) = p1 (largest prime <= sqrt(n))
           ups(n) = p2 (smallest prime >= sqrt(n)).

    2. Semidivisibility Condition:
       n is semidivisible iff n is divisible by exactly one of {p1, p2}:
           n % p1 == 0 XOR n % p2 == 0.

    3. Arithmetic Progression Summation via Inclusion-Exclusion:
       Within the interval [L, R] = [p1^2 + 1, min(p2^2 - 1, limit)]:
           - Sum of multiples of p1: S(p1, L, R)
           - Sum of multiples of p2: S(p2, L, R)
           - Sum of multiples of both (p1 * p2): S(p1 * p2, L, R)
       Total sum contribution in [L, R]:
           Delta_Sum = S(p1, L, R) + S(p2, L, R) - 2 * S(p1 * p2, L, R).

    Complexity:
    -----------
    - Time Complexity: O(pi(sqrt(limit))) operations (< 0.1s for limit ~ 10^12).
    - Space Complexity: O(sqrt(limit)) prime sieve memory (~1 MB).
    """

    def sieve_primes(n: int) -> list[int]:
        is_p = bytearray([1]) * (n + 1)
        is_p[0] = is_p[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                is_p[i * i :: i] = b"\x00" * len(is_p[i * i :: i])
        return [i for i in range(2, n + 1) if is_p[i]]

    max_p = int(math.isqrt(limit)) + 1000
    primes = sieve_primes(max_p)

    def sum_multiples(k: int, L: int, R: int) -> int:
        if L > R:
            return 0
        start = ((L + k - 1) // k) * k
        end = (R // k) * k
        if start > end:
            return 0
        cnt = (end - start) // k + 1
        return cnt * (start + end) // 2

    total_sum = 0
    for idx in range(len(primes) - 1):
        p1 = primes[idx]
        p2 = primes[idx + 1]

        L = p1 * p1 + 1
        R = min(p2 * p2 - 1, limit)

        if L > R:
            if p1 * p1 > limit:
                break
            continue

        s1 = sum_multiples(p1, L, R)
        s2 = sum_multiples(p2, L, R)
        s12 = sum_multiples(p1 * p2, L, R)

        total_sum += s1 + s2 - 2 * s12
        if p1 * p1 >= limit:
            break

    return total_sum


if __name__ == "__main__":
    print(solve())
