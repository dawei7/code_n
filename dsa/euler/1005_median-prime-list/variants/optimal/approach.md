# Median Prime List - Optimal Approach

## Algorithm Explanation

Find the median prime list of $2026$ in lexicographical order and return the last $9$ digits of the product of the primes.

1. Generate all prime numbers up to $2026$.
2. Recursively / dynamically find all increasing prime combinations summing to $2026$.
3. Sort combinations lexicographically and find the median tuple.
4. Compute product modulo $10^9$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^P)$ where $P$ is prime count up to $2026$.
- **Space Complexity:** $\mathcal{O}(P)$ - Memory stack.
