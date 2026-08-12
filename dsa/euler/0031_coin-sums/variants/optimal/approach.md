# Coin Sums - Optimal Approach

## Algorithm Explanation

We calculate the number of combinations to form $T = 200\text{p}$ using coin denominations $C = \{1, 2, 5, 10, 20, 50, 100, 200\}$.

Using 1D Dynamic Programming:
1. Initialize DP array `dp` of size $T + 1$ with zeroes, setting base case `dp[0] = 1`.
2. For each coin denomination $c \in C$:
   - Transition relation for $i \in [c, T]$: `dp[i] += dp[i - c]`.
3. Return `dp[200]`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(|C| \cdot T)$ where $|C| = 8$ and $T = 200$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(T)$ - 1D DP table.
