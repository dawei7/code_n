# Maximum Path Sum I - Optimal Approach

## Algorithm Explanation

To find the maximum total path sum from the top to the bottom of a number triangle, we use **Bottom-Up Dynamic Programming**:

1. Parse the triangle into a 2D grid.
2. Start from the second-to-last row $r = R - 2$ and move upwards to $r = 0$.
3. For each element $(r, c)$, update its value by adding the maximum of its two adjacent children in the row below:
   $$\text{grid}[r][c] \leftarrow \text{grid}[r][c] + \max(\text{grid}[r+1][c], \text{grid}[r+1][c+1])$$
4. After processing all rows, the apex `grid[0][0]` holds the maximum path sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R^2)$ where $R = 15$ rows.
- **Space Complexity:** $\mathcal{O}(R^2)$ - In-place triangle grid state.
