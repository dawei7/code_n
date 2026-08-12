# Counting Rectangles - Optimal Approach

## Algorithm Explanation

Find the area $W \times H$ of a rectangular grid that contains closest to $2,000,000$ total sub-rectangles.

### Combinatorial Sub-rectangle Formula
For a grid of dimensions $W \times H$, choosing $2$ vertical lines out of $W+1$ and $2$ horizontal lines out of $H+1$ yields:
$$\text{Rectangles}(W, H) = \binom{W+1}{2} \times \binom{H+1}{2} = \frac{W(W+1)}{2} \cdot \frac{H(H+1)}{2}$$

### Search Strategy:
1. Iterate grid width $W \in [1, 2000]$.
2. Iterate height $H \in [1, W]$.
3. Calculate sub-rectangle count and difference $|\text{Rectangles}(W, H) - 2000000|$.
4. Break inner loop early when count exceeds target.
5. Track and return area $W \times H$ for minimum difference.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(W \cdot H)$ where $W \le 2000, H \le 2000$. Runs in $< 0.01\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
