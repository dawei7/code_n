"""Project Euler Problem 609: pi Sequences.

Find P(10^8) mod 1000000007, where P(n) is the product of all non-zero counts p(n, k)
of pi-sequences u with u_0 <= n having exactly k non-prime elements.
"""

from typing import List

_MOD = 1_000_000_007


def solve(n: int = 100_000_000) -> int:
    """Compute P(n) modulo 1000000007 by sieving primes and grouping trajectories by prime-interval runs."""
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : n + 1 : i] = b"\x00" * (
                ((n - i * i) // i) + 1
            )

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    num_primes = len(primes)

    small_pi = [0] * (num_primes + 1)
    c = 0
    for i in range(1, num_primes + 1):
        if is_prime[i]:
            c += 1
        small_pi[i] = c

    chain_info: List[List[int]] = [[] for _ in range(num_primes + 1)]
    for x in range(1, num_primes + 1):
        curr = x
        nonp = []
        cnt = 0
        while curr >= 1:
            if not is_prime[curr]:
                cnt += 1
            nonp.append(cnt)
            curr = small_pi[curr]
        chain_info[x] = nonp

    counts = [0] * 35
    for i in range(1, num_primes + 1):
        p_curr = primes[i - 1]
        p_next = primes[i] if i < num_primes else n + 1
        comp_count = p_next - p_curr - 1

        for c_val in chain_info[i]:
            counts[c_val] += 1
            if comp_count > 0:
                counts[1 + c_val] += comp_count

    prod = 1
    for k in range(len(counts)):
        if counts[k] > 0:
            prod = (prod * (counts[k] % _MOD)) % _MOD

    return prod


if __name__ == "__main__":
    print(solve())
