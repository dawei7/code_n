# Singleton Difference - Optimal Approach

## Algorithm Explanation

Find the number of positive integers $n < 50,000,000$ for which the equation $x^2 - y^2 - z^2 = n$ has **exactly one** solution $(x, y, z)$ in positive integers in arithmetic progression.

### Prime Number Theory Classification:
From Problem 135, $x^2 - y^2 - z^2 = n \iff n = a \cdot u$ where $(a + u) \equiv 0 \pmod 4$ and $u < 3a$.

Analyzing the unique factorization requirement, $n < 50,000,000$ has a unique solution if and only if $n \in \{4, 16\}$ or belongs to one of three distinct odd-prime forms:

1. **Form 1**: $n = p$ where $p$ is a prime and $p \equiv 3 \pmod 4$.
2. **Form 2**: $n = 4p$ where $p$ is an odd prime ($p > 2$).
3. **Form 3**: $n = 16p$ where $p$ is an odd prime ($p > 2$).
4. **Special Powers**: $n = 4$ and $n = 16$.

### Sieve Strategy:
1. Construct a prime sieve up to $N = 50,000,000$.
2. Single-pass count:
   - Include special values $n = 4$ and $n = 16$.
   - For every prime $p < N$, check $p \equiv 3 \pmod 4$.
   - For odd prime $p < N/4$, increment count.
   - For odd prime $p < N/16$, increment count.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ sieve and linear pass where $N = 50,000,000$. Runs in $< 1.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Boolean prime array.
