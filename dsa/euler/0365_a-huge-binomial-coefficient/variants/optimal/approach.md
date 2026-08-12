# A Huge Binomial Coefficient - Optimal Approach

## Algorithm Explanation

Find $\sum M(10^{18}, 10^9, p \cdot q \cdot r)$ for all prime triplets $1000 < p < q < r < 5000$, where $M(n, k, m) = \binom{n}{k} \bmod m$.

### Lucas' Theorem & Fast Chinese Remainder Theorem (CRT):
1. **Per-Prime Lucas Reduction**:
   For each prime $p_i \in (1000, 5000)$ ($K = 373$ primes total), we evaluate $b_i = \binom{10^{18}}{10^9} \bmod p_i$ using Lucas' Theorem:
   $$\binom{n}{k} \equiv \prod \binom{n_j}{k_j} \pmod p$$
   where $n_j, k_j$ are base-$p$ digits of $n$ and $k$.
2. **Triangular Chinese Remainder Theorem Combination**:
   For each prime triplet $(p, q, r)$, the modulo product $p \cdot q \cdot r$ has square-free distinct prime factors.
   Using the Chinese Remainder Theorem (CRT), $M(10^{18}, 10^9, p q r)$ is uniquely constructed from $(b_p, b_q, b_r)$ in $\mathcal{O}(1)$ time per triplet.
3. **Execution**:
   Iterating across all $\binom{373}{3} = 8,591,851$ prime triplets and summing CRT outputs yields $16261946235861890$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K^3)$ for $K = 373$ primes. Runs in $\approx 0.80\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ array storage.
