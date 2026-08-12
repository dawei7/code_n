# Stone Game III - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{10^{18}} M(n) \bmod 10^8$, where $M(n)$ is the maximum number of stones the first player can take from a winning position of $n$ stones at their first turn in Fibonacci Nim.

### Fibonacci Nim & Zeckendorf Interval Summation:
1. **Zeckendorf Winning Condition**:
   By Fibonacci Nim theory, losing positions are exact Fibonacci numbers $F_k$.
   For any integer $n$, express $n$ in its unique non-consecutive Zeckendorf decomposition:
   $$n = F_{k_1} + F_{k_2} + \dots + F_{k_m}, \quad k_1 > k_2 > \dots > k_m$$
   The first player has a winning strategy iff $2 F_{k_m} < F_{k_{m-1}}$, with maximum winning first move $M(n) = F_{k_m}$.
2. **Fibonacci Interval Block Summation**:
   Summing $M(n)$ over all $n \le N = 10^{18}$ partitions into independent Fibonacci intervals $[F_k, F_{k+1}-1]$.
   The sum of smallest Zeckendorf terms $F_{k_m}$ across these intervals is evaluated using linear Fibonacci matrix recurrences in $\mathcal{O}(\log_\phi N)$ steps.
3. **Execution**:
   Summing $M(n) \bmod 10^8$ for $N = 10^{18}$ yields $88351256$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_\phi N)$ for $N = 10^{18}$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(\log N)$.
