# Digital Root Sums of Factorisations - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=2}^{999,999} \operatorname{mdrs}(n)$, where $\operatorname{mdrs}(n)$ is the maximum sum of digital roots across all non-trivial factorisations of $n = f_1 \times f_2 \times \dots \times f_k$ ($f_i > 1$).

### Digital Root & Dynamic Programming Recurrence:
The digital root $dr(n)$ in base $10$ is:
$$dr(n) = 1 + (n - 1) \bmod 9 \quad (n \ge 1)$$

For a number $n$, its maximum digital root sum satisfies the DP recurrence:
$$\operatorname{mdrs}(n) = \max \left( dr(n), \max_{i \cdot j = n, i, j > 1} (\operatorname{mdrs}(i) + \operatorname{mdrs}(j)) \right)$$

### Sieve-like Forward Transition:
1. Initialize array `mdrs[n] = 1 + (n - 1) % 9` for all $2 \le n < 10^6$.
2. For each factor $i \in [2, 10^6)$:
   - For each factor $j \in [2, \lfloor (10^6 - 1) / i \rfloor]$:
     $$\text{mdrs}[i \cdot j] = \max(\text{mdrs}[i \cdot j], \text{mdrs}[i] + \text{mdrs}[j])$$
3. Return $\sum_{n=2}^{999,999} \text{mdrs}[n]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log N)$ sieve pass ($N = 10^6$). Runs in $\approx 2.2\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Integer DP array memory.
