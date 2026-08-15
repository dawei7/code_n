"""Project Euler Problem 604: Convex Path in Square.

Find F(10^18), where F(N) is the maximum number of lattice points in an N x N square
that a strictly convex increasing function can pass through.
"""

from typing import List


def _sieve_totient(limit: int) -> List[int]:
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi


def solve(n: int = 10**18) -> int:
    """Compute F(N) using Farey sequence primitive vector greedy packing with Euler totient sieve."""
    max_k = int(4 * (n ** (1 / 3))) + 1000
    phi = _sieve_totient(max_k)

    cur_x = 1
    cur_count = 1
    k = 2

    while True:
        k += 1
        num_pairs = phi[k]
        sum_x = (k * num_pairs) // 2
        if cur_x + sum_x <= n:
            cur_x += sum_x
            cur_count += num_pairs
        else:
            rem = n - cur_x
            extra = (2 * rem) // k
            return cur_count + extra + 1


if __name__ == "__main__":
    print(solve())
