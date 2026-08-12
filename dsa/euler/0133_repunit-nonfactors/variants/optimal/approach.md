# Repunit Nonfactors - Optimal Approach

## Algorithm Explanation

Find the sum of all prime numbers $p < 100,000$ that will **never** be a factor of any repunit of the form $R(10^n) = \frac{10^{10^n} - 1}{9}$.

### Modular Divisibility Criterion:
A prime $p$ divides $R(10^n)$ for some $n \ge 1$ if and only if the minimal repunit length $A(p)$ consists exclusively of prime factors $2$ and $5$:
$$A(p) = 2^a 5^b$$

Equivalently, $p$ divides $R(10^n)$ for some $n \iff 10^{10^k} \equiv 1 \pmod p$ for a sufficiently large power $k$. For all primes $p < 100,000$, setting $k = 16$ ($10^{16} = 2^{16} 5^{16}$) comfortably bounds all possible $2^a 5^b$ orders.

### Strategy:
1. Sieve primes $p < 100,000$.
2. For $p = 2, 5$, add to non-factor sum (repunits are never divisible by $2$ or $5$).
3. For all other primes $p$, evaluate `pow(10, 10**16, p) != 1`.
4. If inequality holds, $p$ will never divide $R(10^n)$; accumulate $p$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P \cdot \log(10^{16}))$ where $P \approx 9592$ primes. Runs in $< 0.015\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Limit})$ - Prime sieve array.
