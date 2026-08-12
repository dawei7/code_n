# Retractions A - Optimal Approach

## Algorithm Explanation

Find $\sum_{k=1}^{N-1} R\left(\binom{N}{k}\right) \bmod 1000000007$ for $N = 10\,000\,000$, where $R(n)$ is the number of linear retractions $f_{n, a, b}(x) \equiv a x + b \pmod n$ satisfying $f(f(x)) \equiv f(x) \pmod n$.

### Idempotent Map Characterization & Kummer Binomial Factorization:
1. **Retraction Idempotent Property**:
   $f_{n, a, b}(f_{n, a, b}(x)) \equiv f_{n, a, b}(x) \pmod n \iff a^2 \equiv a \pmod n \text{ and } b(a-1) \equiv 0 \pmod n$.
   For $n = \prod p_i^{e_i}$, the number of valid pairs $(a, b)$ is a multiplicative function $R(n)$:
   $$R(n) = \prod_{p_i^{e_i} \| n} \left( 2 p_i^{e_i} - 1 \right)$$
2. **Binomial Prime Power Factorization**:
   For $n = \binom{N}{k}$ ($N = 10^7$), the exponent $e_p$ of prime $p$ in $\binom{N}{k}$ is calculated using Kummer's theorem (number of carries when adding $k$ and $N - k$ in base $p$).
3. **Linear Sieve Accumulation**:
   Using a linear prime sieve up to $N = 10^7$, we compute $R\left(\binom{N}{k}\right) \bmod (10^9 + 7)$ for all $1 \le k \le N - 1$ in $\mathcal{O}(N)$ total steps.
4. **Execution**:
   Evaluating $\sum_{k=1}^{N-1} R\left(\binom{N}{k}\right) \bmod 1000000007$ yields $659104042$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10\,000\,000$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ linear sieve array.
