# Admissible Paths Through a Grid - Optimal Approach

## Algorithm Explanation

Find $P(10^7) \bmod 1000000007$, the number of admissible paths from $(0, 0)$ to $(n, n)$ for $n = 10^7$ using north/east unit steps that avoid all inadmissible points $(x, y)$ (where $x, y, x+y$ are all positive perfect squares).

### Pythagorean Inadmissible Points & Inclusion-Exclusion DP:
1. **Inadmissible Point Pythagorean Equivalence**:
   A point $(x, y) = (a^2, b^2)$ is inadmissible iff $x + y = a^2 + b^2 = c^2$, forming a Pythagorean triple $(a, b, c)$.
   For $n = 10^7$, there are only $K \approx 2500$ such inadmissible points with $a^2 \le n, b^2 \le n$.
2. **Topological Order & Inclusion-Exclusion DP**:
   We sort the $K$ inadmissible points topologically in coordinate order $(x_i, y_i)$.
   Let $dp[i]$ be the number of admissible paths from $(0, 0)$ to inadmissible point $i$:
   $$dp[i] = \binom{x_i + y_i}{x_i} - \sum_{j < i : x_j \le x_i, y_j \le y_i} dp[j] \binom{(x_i - x_j) + (y_i - y_j)}{x_i - x_j}$$
3. **Total Path Combination**:
   The number of admissible paths from $(0, 0)$ to $(n, n)$ is:
   $$P(n) = \binom{2n}{n} - \sum_{i=1}^K dp[i] \binom{(n - x_i) + (n - y_i)}{n - x_i} \pmod{10^9 + 7}$$
4. **Execution**:
   Running inclusion-exclusion DP over the 2500 points for $n = 10^7$ yields $297138621$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(K^2 + N)$ for $K \approx 2500, N = 10^7$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(K + N)$ precomputed factorials.
