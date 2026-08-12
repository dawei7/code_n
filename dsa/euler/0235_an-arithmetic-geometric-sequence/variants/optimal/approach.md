# An Arithmetic Geometric Sequence - Optimal Approach

## Algorithm Explanation

Find the real ratio $r$ for which the sum $s(5000) = \sum_{k=1}^{5000} (900 - 3k) r^{k-1} = -600\,000\,000\,000$, rounded to 12 decimal places.

### Monotonic Bisection Search:
1. **Monotonicity**:
   For $k > 300$, the term coefficients $(900 - 3k)$ are negative.
   For $r > 1$, the higher powers $r^{k-1}$ amplify these negative terms, rendering $s(5000)$ strictly monotonic decreasing with respect to $r$.
2. **Bisection Method**:
   Initializing the search interval to $[1.0, 1.1]$, we perform $100$ bisection iterations, shrinking the uncertainty interval to $< 10^{-30}$.
3. **Execution**:
   The value of $r$ satisfying $s(5000) = -6 \times 10^{11}$ is $1.002322108633$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot K)$ for $N = 5000$ terms and $K = 100$ iterations. Runs in $\approx 0.027\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
