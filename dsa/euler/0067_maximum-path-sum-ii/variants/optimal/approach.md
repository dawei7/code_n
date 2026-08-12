# Maximum Path Sum II - Optimal Approach

## Algorithm Explanation

Find the maximum total path sum from top to bottom in a $100$-row number triangle (`triangle.txt`).

### Dynamic Programming Transition:
With $2^{99}$ potential paths, brute-force search is impossible. We use **Bottom-Up Dynamic Programming**:

1. Parse the $100$-row triangle into a 2D integer list `grid`.
2. Move upwards from the $99^{\text{th}}$ row $r = R - 2$ to the top $r = 0$.
3. Update each cell $(r, c)$ by adding the maximum of its two children below:
   $$\text{grid}[r][c] \leftarrow \text{grid}[r][c] + \max(\text{grid}[r+1][c], \text{grid}[r+1][c+1])$$
4. The top cell `grid[0][0]` yields the global maximum path sum.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R^2)$ where $R = 100$ rows ($5050$ total entries). Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(R^2)$ - Storage for 2D triangle state.
