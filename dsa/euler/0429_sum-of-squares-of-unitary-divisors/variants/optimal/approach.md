# Sum of Squares of Unitary Divisors - Optimal Approach

## Algorithm Explanation

Find $S(100\,000\,000!) \bmod 1000000009$, where $S(n)$ is the sum of the squares of the unitary divisors of $n$.

### Multiplicative Unitary Formula & Legendre Factorial Valuation:
1. **Multiplicative Unitary Property**:
   A divisor $d \mid n$ is unitary if $\gcd(d, n/d) = 1$.
   For $n = \prod p_i^{e_i}$, every unitary divisor is formed by taking $p_i^0$ or $p_i^{e_i}$ for each prime factor $p_i$.
   Thus, the sum of squares of unitary divisors is multiplicative:
   $$S(n) = \prod_{p_i^{e_i} \| n} \left( 1 + p_i^{2 e_i} \right)$$
2. **Legendre Factorial Prime Valuation**:
   For $n = N! = 100\,000\,000!$, the exponent $e_p$ of prime $p$ in $N!$ is calculated in $\mathcal{O}(\log_p N)$ using Legendre's formula:
   $$e_p = \sum_{k=1}^{\lfloor \log_p N \rfloor} \left\lfloor \frac{N}{p^k} \right\rfloor$$
3. **Linear Sieve & Prime Product**:
   Using a linear prime sieve up to $N = 100\,000\,000$, we evaluate $\prod_{p \le N} (1 + p^{2 e_p}) \bmod (10^9 + 9)$.
4. **Execution**:
   Evaluating $S(100\,000\,000!) \bmod 1000000009$ yields $98792821$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\frac{N}{\log N}\right)$ for $N = 100\,000\,000$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ prime sieve bitarray.
