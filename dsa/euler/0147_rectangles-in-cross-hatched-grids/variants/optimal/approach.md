# Rectangles in Cross-hatched Grids - Optimal Approach

## Algorithm Explanation

Find the total number of rectangles that can be situated within all cross-hatched grids up to $47 \times 43$ (for all grid dimensions $1 \le w \le 47$ and $1 \le h \le 43$).

### Combinatorial Decomposition:
For a grid of size $w \times h$, rectangles belong to two disjoint categories:

1. **Axis-Aligned Rectangles**:
   $$\text{Axis-aligned}(w, h) = \binom{w+1}{2} \binom{h+1}{2} = \frac{w(w+1)}{2} \times \frac{h(h+1)}{2}$$

2. **Diagonal (Cross-Hatched) Rectangles**:
   Assuming $w \ge h$ (wlog):
   $$\text{Diagonal}(w, h) = \frac{h \left[ (2w - h)(4h^2 - 1) - 3 \right]}{6}$$

### Closed-Form Accumulation:
Sum $\text{Axis-aligned}(w, h) + \text{Diagonal}(\max(w, h), \min(w, h))$ across all grid dimensions $w \in [1, 47]$ and $h \in [1, 43]$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(W \cdot H)$ where $W = 47, H = 43$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
