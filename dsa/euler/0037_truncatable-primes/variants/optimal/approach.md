# Truncatable Primes - Optimal Approach

## Algorithm Explanation

A prime is **truncatable** if removing digits continuously from left to right or right to left leaves a prime number at every stage (excluding single-digit primes $2, 3, 5, 7$).

1. Generate boolean prime lookup and hash set `prime_set` up to $N = 1000000$ using Sieve of Eratosthenes.
2. Iterate candidate primes $p \ge 11$.
3. Check left-to-right truncations $s[i:] \in \text{prime\_set}$ for $0 \le i < L$.
4. Check right-to-left truncations $s[:i] \in \text{prime\_set}$ for $1 \le i \le L$.
5. Stop when $11$ valid truncatable primes are found and return their sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ where $N = 1000000$. Runs in $< 0.2\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Prime sieve table and set.
