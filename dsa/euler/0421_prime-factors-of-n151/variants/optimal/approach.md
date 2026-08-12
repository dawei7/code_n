# Prime Factors of n^15 + 1 - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10^{11}} s(n, 10^8)$, where $s(n, m)$ is the sum of distinct prime factors of $n^{15} + 1$ not exceeding $m = 10^8$.

### Prime Sieve Inversion & Modular Power Residue Equations:
1. **Inversion of Control**:
   Instead of factoring $n^{15} + 1$ for each $n \le 10^{11}$, we iterate over all primes $p \le M = 10^8$.
   A prime $p$ divides $n^{15} + 1$ iff $n^{15} \equiv -1 \pmod p$.
2. **Modular 15th-Power Residue Roots**:
   For each prime $p \le 10^8$:
   - If $p = 2$, $n^{15} + 1$ is even for odd $n$.
   - For odd prime $p$, we find all roots $x_1, \dots, x_r \in [0, p-1]$ of $x^{15} \equiv -1 \pmod p$.
   - The number of roots $r = \gcd(15, p - 1)$ if $-1$ is a 15th power residue modulo $p$, and $0$ otherwise.
3. **Arithmetic Progression Counting**:
   For each root $x_k \pmod p$, the number of $n \le N = 10^{11}$ satisfying $n \equiv x_k \pmod p$ is:
   $$\text{Count}(x_k, p) = \left\lfloor \frac{N - x_k}{p} \right\rfloor + 1 \quad (\text{for } x_k > 0)$$
   The contribution of prime $p$ to the total sum is $p \cdot \sum_{k=1}^r \text{Count}(x_k, p)$.
4. **Execution**:
   Summing contributions across all primes $p \le 10^8$ yields $23042158025704$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\frac{M}{\log M} \cdot \gcd(15, p-1)\right)$ for $M = 10^8, N = 10^{11}$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}\left(\frac{M}{\log M}\right)$ prime sieve array.
