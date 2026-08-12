# Quadtree Encoding (a Simple Compression Algorithm) - Optimal Approach

## Algorithm Explanation

Find the minimal bit length of the quadtree encoding for the $2^{24} \times 2^{24}$ binary image $D_{24}$, where pixel $(x, y)$ is black iff $(x - 2^{23})^2 + (y - 2^{23})^2 \le 2^{46}$.

### Divide-and-Conquer Quadtree Decomposition:
1. **Quadtree Encoding Protocol**:
   - `0`: split $2^n \times 2^n$ region into $4$ sub-regions of $2^{n-1} \times 2^{n-1}$ (cost = $1$ bit + sub-region costs).
   - `10`: region is monochromatic black ($2$ bits).
   - `11`: region is monochromatic white ($2$ bits).
2. **Monochromatic Sub-region Pruning**:
   For any square region $[x_0, x_0 + 2^n - 1] \times [y_0, y_0 + 2^n - 1]$:
   - If all $4$ corners are inside the disk, the entire convex square is black ($2$ bits).
   - If all $4$ corners are outside the disk and the minimum distance from the disk center $(2^{23}, 2^{23})$ to the square exceeds radius $R = 2^{23}$, the entire square is white ($2$ bits).
   - Otherwise, the circle boundary intersects the square, requiring a split (`0`).
3. **Symmetry Acceleration**:
   By $4$-fold quadrant symmetry around the center $(2^{23}, 2^{23})$, subproblems are efficiently evaluated.
4. **Execution**:
   The minimal quadtree sequence length for $D_{24}$ is $3131359269$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^N)$ over boundary-intersecting quadtree nodes for $N = 24$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ recursion depth.
