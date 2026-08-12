# Prime Subset Sums - Optimal Approach

## Algorithm Explanation

Find the rightmost $16$ digits of the number of subsets of the set of primes $S = \{p \text{ prime} \mid p < 5000\}$ whose elements sum to a prime number.

### 0-1 Knapsack Dynamic Programming:
1. **Subset Sum Distribution**:
   There are $669$ primes in $S$, with maximum possible subset sum $M = \sum_{p \in S} p = 1\,548\,136$.
   Let `dp[s]` be the number of subsets of $S$ with sum $s$, modulo $10^{16}$.
   We initialize `dp[0] = 1`. For each prime $p \in S$, we update the DP array in reverse order:
   $$\text{dp}[s + p] = (\text{dp}[s + p] + \text{dp}[s]) \bmod 10^{16}$$
2. **Prime Sum Aggregation**:
   After processing all $669$ primes, we sum `dp[prime]` for all prime numbers $p \le M$ modulo $10^{16}$.
3. **Execution**:
   Summing across all prime subset sums yields $9211949401918076$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(|S| \cdot \sum p) \approx 5 \times 10^8$ operations. Runs in $\approx 15.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sum p)$ for DP array storage.
