# Counting Summations - Optimal Approach

## Algorithm Explanation

Find the number of different ways $N = 100$ can be written as a sum of at least two positive integers (the partition function $p(100) - 1$).

### Dynamic Programming Formulation:
This is equivalent to the Unbounded Knapsack / Coin Change problem with coin denominations $\{1, 2, \dots, N - 1\}$:

1. Initialize `dp` table of size $N + 1$ with `dp[0] = 1`.
2. For each available term $c \in [1, N - 1]$:
   - Update `dp[i] += dp[i - c]` for $i \in [c, N]$.
3. Return `dp[100]`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 100$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - 1D DP table.
