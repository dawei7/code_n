# Triominoes - Optimal Approach

## Algorithm Explanation

Find the total number of ways to tile a $9 \times 12$ grid using the $6$ possible orientations of triominoes (straight $3 \times 1$ and $L$-triominoes).

### Broken-Profile Bitmask Dynamic Programming:
Process grid cells sequentially in row-major order $(r, c)$ from cell $0$ to $R \times C - 1$ ($R = 12, C = 9$):

1. **Active Window Bitmask**:
   A bitmask `mask` tracks the occupancy status of the active window of size $(2C + 1)$ cells ahead of the current cell $(r, c)$.
2. **Cell Transition**:
   - If the current cell is already covered (`mask & 1 == 1`), advance to cell $(r, c+1)$ with `mask >> 1`.
   - If the current cell is empty (`mask & 1 == 0`), attempt to place each of the $6$ triomino shapes rooted at $(r, c)$:
     1. Horizontal straight: $(0,0), (0,1), (0,2)$
     2. Vertical straight: $(0,0), (1,0), (2,0)$
     3. $L$-shape 1: $(0,0), (1,0), (0,1)$
     4. $L$-shape 2: $(0,0), (1,0), (1,1)$
     5. $L$-shape 3: $(0,0), (0,1), (1,1)$
     6. $L$-shape 4: $(0,0), (1,0), (1,-1)$
3. **Memoized Recursion**:
   Memoize state key `(cell, mask)` to avoid re-evaluating duplicate profiles.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot C \cdot 2^{2C})$ where $R = 12, C = 9$. Runs in $\approx 1.2\text{s}$.
- **Space Complexity:** $\mathcal{O}(R \cdot C \cdot 2^{2C})$ - State memoization dictionary.
