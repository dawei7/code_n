# Resilience - Optimal Approach

## Algorithm Explanation

Find the smallest denominator $d$ having resilience $R(d) = \frac{\phi(d)}{d - 1} < \frac{15499}{94744}$.

### Primorial Multiples & Euler's Totient Minimization:
1. **Ratio Minimization**:
   The ratio $\frac{\phi(d)}{d} = \prod_{p \mid d} \left(1 - \frac{1}{p}\right)$ is minimized when $d$ contains all consecutive smallest prime factors starting from $2$.
   Hence, $d$ must be a primorial $P_k = \prod_{i=1}^k p_i$ or a small integer multiple $d = m \cdot P_k$.
2. **Sequential Multiple Search**:
   Iterating primorials $P_k = 2, 6, 30, 210, 2310, \dots$ and their multiples $m \in [1, p_{k+1}]$, we test $R(d) < \frac{15499}{94744}$.
3. **Execution**:
   The smallest valid denominator is $d = 4 \times (2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 \times 23) = 892371480$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(k \cdot p_{k+1})$ for $k = 9$ primes. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
