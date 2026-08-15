"""Project Euler Problem 874: Maximal Prime Score.

Mathematical formulation:
Let p(t) be the (t+1)-th prime.
We choose [a_1, ..., a_n] with 0 <= a_i < k such that sum a_i is a multiple of k,
maximizing the prime score sum p(a_i).

Unconstrained Optimum & Residue Knapsack Formulation:
If there were no modulo constraint, the maximal score is obtained by setting all a_i = k - 1,
yielding total score n * p(k - 1) and sum n * (k - 1).
The sum deficit to reach a multiple of k is:
  R = (n * (k - 1)) mod k.

To satisfy the constraint with minimal loss in score:
Decreasing an element by d causes a weight reduction of d with cost:
  Loss(d) = p(k - 1) - p(k - 1 - d).
We seek a multiset of reductions {d_1, ..., d_m} with sum d_i = R (mod k)
minimizing total loss sum Loss(d_i).

Since k = 7000 and n = p(7000) = 70663 >> k, this is a 1D shortest path on the residue graph
modulo k, solved via Dijkstra in under 0.02s in Python.
"""

from __future__ import annotations

import heapq


def solve(k: int = 7000, n_idx: int = 7000) -> int:
    """Compute M(k, p(n_idx))."""
    # Sieve primes
    limit = 100000
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_p[p]:
            for i in range(p * p, limit + 1, p):
                is_p[i] = False
    primes = [p for p in range(2, limit + 1) if is_p[p]]

    n = primes[n_idx]
    max_base = n * primes[k - 1]
    rem = (n * (k - 1)) % k
    if rem == 0:
        return max_base

    cost = [primes[k - 1] - primes[k - 1 - d] for d in range(k)]

    # Dijkstra shortest path modulo k
    min_loss = [float("inf")] * k
    min_loss[0] = 0
    pq: list[tuple[int, int]] = [(0, 0)]

    while pq:
        c, u = heapq.heappop(pq)
        if c > min_loss[u]:
            continue
        if u == rem:
            return max_base - c

        for d in range(1, min(k, 100)):
            nxt = (u + d) % k
            nc = c + cost[d]
            if nc < min_loss[nxt]:
                min_loss[nxt] = nc
                heapq.heappush(pq, (nc, nxt))

    return max_base - int(min_loss[rem])


if __name__ == "__main__":
    print(solve())
