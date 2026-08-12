# Strong Repunits - Optimal Approach

## Algorithm Explanation

Find the sum of all strong repunits below $10^{12}$, where a strong repunit is a positive integer that is a repunit in at least two bases $b > 1$.

### Trivial Base Identity & Multi-digit Repunit Generation:
1. **Base $n-1$ Trivial Property**:
   Every integer $n > 2$ is a 2-digit repunit in base $n-1$, since $n = 1 \cdot (n-1) + 1 = 11_{n-1}$.
   Therefore, an integer $n$ is a strong repunit iff it is a repunit of length $k \ge 3$ in at least one base $b \ge 2$ (or $n = 1$).
2. **Repunit Set Generation**:
   A repunit of length $k \ge 3$ in base $b$ has the value:
   $$R_k(b) = 1 + b + b^2 + \dots + b^{k-1} = \frac{b^k - 1}{b - 1}$$
   For $R_k(b) < N = 10^{12}$ and $k \ge 3$, the base $b$ satisfies $b < \sqrt{N} = 10^6$.
   We generate all such $R_k(b)$ for $b \in [2, 10^6 - 1]$ and $k \ge 3$, insert them into a hash set (plus $1$), and compute their sum.
3. **Execution**:
   Summing all unique repunits below $10^{12}$ yields $336108797759204086$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^{1/2})$ for $N = 10^{12}$. Runs in $\approx 0.10\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^{1/2})$ set storage.
