# Largest Product in a Grid - Optimal Approach

## Algorithm Explanation

We search a $20 \times 20$ grid for the greatest product of $4$ adjacent numbers in any straight line (horizontal, vertical, or diagonal).

1. Parse the string representation into a 2D integer grid $[20][20]$.
2. Iterate through every cell $(r, c)$.
3. Check four directional vectors of length $4$:
   - **Horizontal**: $(r, c \dots c+3)$
   - **Vertical**: $(r \dots r+3, c)$
   - **Main Diagonal**: $(r \dots r+3, c \dots c+3)$
   - **Anti Diagonal**: $(r \dots r+3, c \dots c-3)$
4. Maintain and return the maximum product seen.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot C)$ where $R = C = 20$.
- **Space Complexity:** $\mathcal{O}(R \cdot C)$ - 2D grid allocation.
