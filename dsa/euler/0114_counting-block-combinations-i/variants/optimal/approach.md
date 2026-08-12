# Counting Block Combinations I - Optimal Approach

## Algorithm Explanation

Find the total number of ways to fill a row of length $N = 50$ units with red blocks of minimum length $m = 3$, separated by at least one grey square.

### Dynamic Programming Transition:
Let $DP[i]$ be the number of valid configurations for a row of length $i$:

1. Base case: $DP[0] = 1$.
2. Transitions for row length $i \in [1, N]$:
   - **Case A**: Position $i$ is a grey square: $DP[i-1]$.
   - **Case B**: A red block of length $L \ge m$ ends at position $i$:
     - If $i - L - 1 \ge 0$, the red block is preceded by a grey square at $i - L$, contributing $DP[i - L - 1]$.
     - If $i - L - 1 < 0$, the red block extends to the start of the row, contributing $1$.
3. Combined DP recurrence:
   $$DP[i] = DP[i-1] + \sum_{L=m}^{i-1} DP[i - L - 1] + 1$$

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 50$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - 1D DP table.
