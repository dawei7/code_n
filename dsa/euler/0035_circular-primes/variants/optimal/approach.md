# Circular Primes - Optimal Approach

## Algorithm Explanation

A prime is **circular** if all cyclic digit rotations are also prime (e.g. $197, 971, 719$).

1. Generate boolean prime lookup array up to $N = 1000000$ using Sieve of Eratosthenes.
2. Build hash set `prime_set` of all primes below $1000000$.
3. For each prime $p \in \text{prime\_set}$:
   - Skip immediately if $p > 5$ contains even digits or $5$ (since a rotation ending in $0, 2, 4, 5, 6, 8$ is composite).
   - Test all cyclic rotations $s[i:] + s[:i]$.
   - If all rotations exist in `prime_set`, increment count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 1000000$. Runs in under $0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Prime set and sieve table.
