# Iterative Circle Packing - Optimal Approach

## Algorithm Explanation

Find the fraction of uncovered area after $10$ iterations of Apollonian circle packing inside a unit circle.

### Descartes' Circle Theorem & Apollonian Gasket Recursion:
1. **Initial Curvatures**:
   - Outer circle: curvature $k_0 = -1$.
   - Three inner circles of radius $r = 2\sqrt{3} - 3$: curvature $k = 1 + \frac{2}{\sqrt{3}}$.
2. **Descartes' Theorem**:
   For any triplet of mutually tangent circles with curvatures $(k_1, k_2, k_3)$, the newly placed tangent circle curvature $k_4$ is:
   $$k_4 = k_1 + k_2 + k_3 + 2\sqrt{k_1 k_2 + k_2 k_3 + k_3 k_1}$$
3. **Iterative Gap Filling**:
   At each step, a gap defined by $(k_1, k_2, k_3)$ produces 3 new gaps $(k_1, k_2, k_4), (k_2, k_3, k_4), (k_3, k_1, k_4)$ and adds area $\pi / k_4^2$.
4. **Execution**:
   After $10$ iterations, the uncovered fraction is $0.00396087$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(3^n)$ for $n = 10$ iterations ($4 \times 3^{10} \approx 2.36 \times 10^5$ operations). Runs in $\approx 0.06\text{s}$.
- **Space Complexity:** $\mathcal{O}(3^n)$ for gap buffer.
