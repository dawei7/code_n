"""Project Euler Problem 518: Prime Triples and Geometric Sequences.

Find S(10^8), where S(n) is the sum of (a + b + c) over all prime triples
a < b < c < n such that (a + 1), (b + 1), (c + 1) form a geometric sequence.
"""

import math


def solve(n: int = 10**8) -> int:
    """Compute S(n) by parameterizing geometric progressions (k*u^2, k*u*v, k*v^2) over coprime (u, v)."""
    is_prime = bytearray(b"\x01") * n
    is_prime[0] = is_prime[1] = 0
    limit_sqrt = math.isqrt(n)

    for i in range(2, limit_sqrt + 1):
        if is_prime[i]:
            is_prime[i * i : n : i] = b"\x00" * (
                ((n - 1 - i * i) // i) + 1
            )

    total = 0

    for v in range(2, limit_sqrt + 1):
        v2 = v * v
        for u in range(1, v):
            if math.gcd(u, v) != 1:
                continue
            u2 = u * u
            uv = u * v
            max_k = (n - 1) // v2

            for k in range(1, max_k + 1):
                c = k * v2 - 1
                if is_prime[c]:
                    a = k * u2 - 1
                    if is_prime[a]:
                        b = k * uv - 1
                        if is_prime[b]:
                            total += a + b + c

    return total


if __name__ == "__main__":
    print(solve())
