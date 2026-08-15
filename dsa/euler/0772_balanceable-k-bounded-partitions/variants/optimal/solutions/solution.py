"""Project Euler Problem 772: Balanceable k-bounded Partitions.

Find f(10^8) modulo 10^9+7, where f(k) = 2 * LCM(1, 2, ..., k) is the smallest integer N
all of whose k-bounded partitions are balanceable.
"""

_MOD = 1_000_000_007


def solve(k: int = 100_000_000) -> int:
    """Compute f(k) = 2 * LCM(1, 2, ..., k) mod 10^9+7 using an odd-sieve bytearray."""
    if k <= 1:
        return 2 % _MOD

    sieve = bytearray(b"\x01") * ((k >> 1) + 1)
    lim = int(k**0.5) >> 1
    for i in range(1, lim + 1):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) >> 1
            sieve[start::p] = b"\x00" * ((len(sieve) - start - 1) // p + 1)

    ans = 2
    p2 = 1
    while p2 * 2 <= k:
        p2 *= 2
    ans = (ans * p2) % _MOD

    for i in range(1, len(sieve)):
        if sieve[i]:
            p = 2 * i + 1
            if p > k:
                continue
            pp = p
            while pp * p <= k:
                pp *= p
            ans = (ans * pp) % _MOD

    return ans


if __name__ == "__main__":
    print(solve())
