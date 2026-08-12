# Path Sum: Three Ways - Optimal Approach

## Algorithm Explanation

Find the minimal path sum starting from any cell in the leftmost column to any cell in the rightmost column in an $80 \times 80$ matrix, moving **up**, **down**, or **right**.

### Column-by-Column Dynamic Programming:
Let $Cost[r]$ store the minimum path sum to reach row $r$ in column $c-1$:

For each column $c = 1 \dots C-1$:
1. Initialize candidate cost from left: `next_cost[r] = Cost[r] + grid[r][c]`.
2. Forward sweep (Top-to-Bottom):
   $$\text{next\_cost}[r] = \min(\text{next\_cost}[r], \text{next\_cost}[r-1] + \text{grid}[r][c])$$
3. Backward sweep (Bottom-to-Top):
   $$\text{next\_cost}[r] = \min(\text{next\_cost}[r], \text{next\_cost}[r+1] + \text{grid}[r][c])$$
4. Update $Cost \leftarrow \text{next\_cost}$.

Return $\min(Cost)$ after processing column $C-1$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot C)$ where $R = C = 80$. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(R)$ - Column cost vector.
