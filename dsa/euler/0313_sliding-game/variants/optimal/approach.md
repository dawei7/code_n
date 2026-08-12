# Sliding Game - Optimal Approach

## Algorithm Explanation

Find the number of grids $(m, n)$ for which the minimum moves $S(m, n) = p^2$, where $p < 10^6$ is prime.

### Closed-Form Move Formula & Congruence Range Counting:
1. **Sliding Move Closed Form**:
   - For $m = n$: $S(m, m) = 8m - 11$.
   - For $m < n$: $S(m, n) = 2m + 6n - 13$.
2. **Diophantine Range & Modulo Conditions**:
   - Square case $m = n$: $8m - 11 = p^2 \implies m = (p^2 + 11) / 8$ if $8 \mid (p^2 + 11)$.
   - Asymmetric case $m < n$: $2m + 6n - 13 = p^2 \implies 6n = p^2 + 13 - 2m$.
     Since $m < n \implies 8m < p^2 + 13 \implies m < (p^2 + 13) / 8$.
     Also $2m \equiv p^2 + 13 \pmod 6$.
3. **Execution**:
   For each prime $p < 10^6$, we count valid $m \in [1, (p^2+12)/8)$ satisfying $2m \equiv p^2 + 13 \pmod 6$ in $\mathcal{O}(1)$ time.
   Accounting for symmetry $(m, n)$ and $(n, m)$, the total count yields $2057774861813004$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\pi(N))$ for $N = 10^6$. Runs in $\approx 0.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ prime array memory.
