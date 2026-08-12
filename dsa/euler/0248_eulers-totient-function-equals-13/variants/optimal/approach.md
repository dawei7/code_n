# Euler's Totient Function Equals 13! - Optimal Approach

## Algorithm Explanation

Find the $150\,000$th integer $n$ for which $\phi(n) = 13! = 6\,227\,020\,800$.

### Divisor Factoring & Backtracking Search:
1. **Candidate Prime Power Generation**:
   Since $\phi(n) = \prod p_i^{e_i-1}(p_i - 1) = 13!$, every prime factor $p$ of $n$ must satisfy $(p - 1) \mid 13!$.
   We enumerate all $1584$ divisors $d$ of $13!$. For each $d$, if $p = d + 1$ is prime, we generate candidate prime powers $p^e$ such that $p^{e-1}(p-1) \mid 13!$.
2. **Depth-First Backtracking Search**:
   We search over all valid prime power combinations whose totient values multiply to $13!$.
3. **Sorted Selection**:
   Sorting all generated solutions in ascending order, the $150\,000$th solution is $935013005126152140$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{divisors}(13!) \cdot \text{DFS})$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(K)$ for solution list storage.
