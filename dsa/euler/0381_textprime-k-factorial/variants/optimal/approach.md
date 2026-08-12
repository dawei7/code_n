# (prime-k) Factorial - Optimal Approach

## Algorithm Explanation

Find $\sum S(p)$ for all primes $5 \le p < 10^8$, where $S(p) = \sum_{k=1}^5 (p-k)! \bmod p$.

### Wilson's Theorem & Modular Inverse Simplification:
1. **Wilson's Theorem Reductions**:
   By Wilson's Theorem: $(p-1)! \equiv -1 \pmod p$.
   Subsequent terms satisfy:
   - $(p-2)! \equiv 1 \pmod p$.
   - $(p-3)! \equiv \frac{p-1}{2} \equiv -\frac{1}{2} \pmod p$.
   - $(p-4)! \equiv \frac{1}{6} \pmod p$.
   - $(p-5)! \equiv -\frac{1}{24} \pmod p$.
2. **Rational Sum Closed-Form**:
   Summing the five terms modulo $p$:
   $$S(p) \equiv -1 + 1 - \frac{1}{2} + \frac{1}{6} - \frac{1}{24} \equiv -\frac{3}{8} \pmod p$$
   Thus, for every prime $p \ge 5$:
   $$S(p) = (-3 \cdot 8^{-1}) \bmod p = (p - (3 \cdot 8^{-1} \bmod p)) \bmod p$$
3. **Execution**:
   Using a linear prime sieve up to $10^8$, we evaluate $S(p)$ in $\mathcal{O}(1)$ per prime using modular inverse of $8 \pmod p$.
   Summing across all primes $5 \le p < 10^8$ yields $139602943319822$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N / \log N)$ for $N = 10^8$. Runs in $\approx 0.40\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ prime bitarray.
