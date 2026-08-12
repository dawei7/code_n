# Path Sum: Two Ways - Optimal Approach

## Algorithm Explanation

Find the minimal path sum from the top-left corner to the bottom-right corner in an $80 \times 80$ matrix, moving only **right** and **down**.

### Dynamic Programming Formulation:
Let $DP[r][c]$ be the minimal path sum from $(0, 0)$ to $(r, c)$:

1. Base cases:
   - First row: $DP[0][c] = DP[0][c-1] + \text{grid}[0][c]$
   - First column: $DP[r][0] = DP[r-1][0] + \text{grid}[r][0]$
2. Recurrence relation for $r \ge 1, c \ge 1$:
   $$DP[r][c] = \text{grid}[r][c] + \min(DP[r-1][c], DP[r][c-1])$$
3. $DP[R-1][C-1]$ gives the minimal path sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot C)$ where $R = C = 80$ ($6400$ operations). Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(R \cdot C)$ - Storage for matrix state.
