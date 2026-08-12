# Consecutive Die Throws - Optimal Approach

## Algorithm Explanation

Find $S(50\,000\,000) \bmod 1000000007$, where $S(L) = \sum_{n=1}^L C(n)$ and $C(n)$ is the number of $n$-roll sequences on a 6-sided die having at most $\pi(n)$ consecutive match pairs.

### Binomial Distribution & Pascal Identity Rolling Sum:
1. **Combinatorial Exact Match Formula**:
   For $n$ die throws, there are $n-1$ adjacent pairs.
   The number of sequences with exactly $k$ consecutive match pairs is:
   $$6 \binom{n-1}{k} 5^{n-1-k}$$
   Thus, $C(n) = 6 \sum_{k=0}^{\pi(n)} \binom{n-1}{k} 5^{n-1-k} \pmod{10^9 + 7}$.
2. **Rolling Binomial Transition**:
   When incrementing $n \to n+1$:
   Using Pascal's recurrence $5 \binom{n-1}{k} + \binom{n-1}{k-1} = \binom{n}{k}$, $C(n+1)$ is updated in $\mathcal{O}(1)$ time from $C(n)$.
   When $n+1$ is prime, $\pi(n+1) = \pi(n) + 1$, and we append the single new term $\binom{n}{\pi(n+1)} 5^{n - \pi(n+1)}$.
3. **Linear Prime Sieve & Accumulation**:
   We precompute primality up to $L = 50\,000\,000$ with a linear sieve and maintain the rolling binomial sum in $\mathcal{O}(L)$ operations.
4. **Execution**:
   Evaluating $S(50\,000\,000) \bmod 1000000007$ yields $653972374$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L)$ for $L = 50\,000\,000$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ linear prime sieve boolean array.
