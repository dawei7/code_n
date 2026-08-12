# Counting Block Combinations II - Optimal Approach

## Algorithm Explanation

Find the least row length $n$ for which the fill-count function $F(m, n)$ with minimum block size $m = 50$ first exceeds $1,000,000$.

### Dynamic Programming Formulation:
Generalizing the block recurrence from Problem 114 for arbitrary minimum block size $m$:
$$F(m, i) = F(m, i-1) + \sum_{L=m}^{i-1} F(m, i - L - 1) + 1$$

Iterate row length $n = m, m+1 \dots$, evaluate $F(50, n)$, and return $n$ when $F(50, n) > 1,000,000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N \approx 170$. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - DP state table.
