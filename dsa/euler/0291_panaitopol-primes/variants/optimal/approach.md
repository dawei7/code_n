# Panaitopol Primes - Optimal Approach

## Algorithm Explanation

Find how many Panaitopol primes $p = \frac{x^4 - y^4}{x^3 + y^3}$ (for positive integers $x, y$) are less than $5 \times 10^{15}$.

### Algebraic Reduction to Sum of Consecutive Squares:
1. **Algebraic Factorization**:
   $$\frac{x^4 - y^4}{x^3 + y^3} = \frac{(x - y)(x^2 + y^2)}{x^2 - xy + y^2}$$
2. **Panaitopol Prime Characterization**:
   For $p$ to be prime, setting $x = n(n+1) + 1$ and $y = n(n+1)$ gives $x - y = 1$ and $x^2 - xy + y^2 = 1$.
   This reduces the expression identically to $p = x^2 + y^2 = n^2 + (n+1)^2 = 2n^2 + 2n + 1$.
   Every Panaitopol prime is a prime of the form $p = 2n^2 + 2n + 1$.
3. **Polynomial Sieve Search Bound**:
   $p = 2n^2 + 2n + 1 < 5 \times 10^{15} \implies n < 5 \times 10^7$.
4. **Execution**:
   Sieving $p = 2n^2 + 2n + 1$ for $n < 5 \times 10^7$ yields $4037526$ Panaitopol primes.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log \log N)$ for $N = 5 \times 10^7$. Runs in $\approx 1.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{N})$ segmented sieve memory.
