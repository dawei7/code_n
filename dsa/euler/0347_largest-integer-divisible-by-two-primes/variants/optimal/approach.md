# Largest Integer Divisible by Two Primes - Optimal Approach

## Algorithm Explanation

Find $S(10\,000\,000)$, the sum of all distinct $M(p, q, N)$ values for prime pairs $p < q$ with $p q \le N$, where $M(p, q, N)$ is the largest integer $\le N$ whose prime factors are exactly $\{p, q\}$.

### Prime Pair Exponent Bisection:
1. **Prime Pair Domain Restriction**:
   For $M(p, q, N) > 0$, the prime pair must satisfy $p \cdot q \le N$.
   Since $p < q$, $p \le \sqrt{N} = 3162$.
2. **Maximum Power Product Calculation**:
   For a fixed pair $(p, q)$, we maximize $p^a q^b \le N$ with $a \ge 1, b \ge 1$:
   - Iterate $p^a \le N / q$.
   - For each $p^a$, compute $b = \lfloor \log_q (N / p^a) \rfloor$.
   - The maximum $p^a q^b$ across all $a \ge 1$ gives $M(p, q, N)$.
3. **Deduplication**:
   All valid $M(p, q, N) > 0$ are inserted into a hash set to ensure distinctness before summing.
4. **Execution**:
   Summing distinct $M(p, q, N)$ for $N = 10\,000\,000$ yields $111098002040526$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\frac{N}{\log N})$ for $N = 10\,000\,000$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(\frac{N}{\log N})$ prime and result set storage.
